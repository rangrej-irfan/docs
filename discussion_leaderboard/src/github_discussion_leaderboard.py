
import configparser

# Load properties from file
config = configparser.ConfigParser()
config.read('github_configs_dont_commit.properties')

# Assign values from properties file to variables
DISCUSSION_CATEGORY = config['DEFAULT']['DISCUSSION_CATEGORY']
IGNORED_USERS = config['DEFAULT']['IGNORED_USERS'].strip().split(',')  # assuming multiple ignored users are comma-separated
GITHUB_TOKEN = config['DEFAULT']['GITHUB_TOKEN']
GITHUB_REPO = config['DEFAULT']['GITHUB_REPO']

DEBUG = False
X=1
Y=2
Z=3

def test_github_token():
    url = 'https://api.github.com/user'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        print("Token is valid. Authenticated user information:")
        print(user_info)
    else:
        print(f"Failed to authenticate. Status code: {response.status_code}")
        print(response.json())

def test_repo_read_permissions():
    owner, repo = GITHUB_REPO.split('/')
    url = f'https://api.github.com/repos/{owner}/{repo}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repo_info = response.json()
        print("Token has read permissions on the repository. Repository information:")
        print(repo_info)
    else:
        print(f"Failed to read the repository. Status code: {response.status_code}")
        print(response.json())

def summary():
    """
    Summary:
    This script creates a Streamlit application to display a leaderboard for GitHub discussion contributions.
    It tracks weekly and all-time scores based on user activities such as asking questions, providing feedback,
    and reacting to posts. The leaderboard is updated weekly and displays:

    1. Top 5 all-time leaders.
    2. A bar chart showing weekly aggregate scores.
    3. Weekly scores in sections, with the latest week on top.
    4. A full list of participants sorted by total score from high to low.

    Main Functions:
    - fetch_discussion_categories: Fetches discussion categories from a GitHub repository.
    - fetch_comments_and_replies: Fetches comments and replies for a given discussion.
    - fetch_discussions_by_category: Fetches discussions by category from a GitHub repository.
    - get_week_bucket: Determines the week bucket for a given date.
    - calculate_scores: Calculates scores for each user based on their activities.
    - display_leaderboard: Displays the leaderboard in various sections.
    - main: Main function to run the Streamlit app and update the leaderboard.
    """
    pass


import os
import requests
from collections import defaultdict
import streamlit as st
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Global variables
# DISCUSSION_CATEGORY = 'documentation-comments'
# DEBUG = True  # Set to False to disable debugging print statements
# X = 1  # Points for thumbs up/down
# Y = 2  # Points for asking a question or giving feedback
# Z = 3  # Points for responding back
# IGNORED_USERS = ['giscus']  # List of users to ignore

# Fetch the token from an environment variable
# GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
# GITHUB_REPO = os.getenv('GITHUB_REPO')  # Ensure this is set in your environment variables


headers = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'Content-Type': 'application/json'
}

def fetch_discussion_categories(owner, repo):
    """
    Fetches discussion categories from a GitHub repository.

    Args:
        owner (str): GitHub repository owner.
        repo (str): GitHub repository name.

    Returns:
        dict: JSON response with discussion categories.
    """
    query = """
    {
      repository(owner: "%s", name: "%s") {
        discussionCategories(first: 10) {
          nodes {
            id
            name
          }
        }
      }
    }
    """ % (owner, repo)

    response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed with status code {response.status_code}. {response.json()}")

def fetch_comments_and_replies(discussion_id):
    """
    Fetches comments and replies for a given discussion.

    Args:
        discussion_id (str): ID of the discussion.

    Returns:
        list: List of comments and replies.
    """
    comments = []
    cursor = None
    while True:
        query = """
        {
          node(id: "%s") {
            ... on Discussion {
              comments(first: 50, after: %s) {
                pageInfo {
                  endCursor
                  hasNextPage
                }
                nodes {
                  id
                  bodyText
                  author {
                    login
                  }
                  createdAt
                  reactions(first: 50) {
                    nodes {
                      content
                    }
                  }
                  replies(first: 50) {
                    nodes {
                      id
                      bodyText
                      author {
                        login
                      }
                      createdAt
                      reactions(first: 50) {
                        nodes {
                          content
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        """ % (discussion_id, f'"{cursor}"' if cursor else "null")

        response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
        if response.status_code == 200:
            data = response.json()
            comments.extend(data['data']['node']['comments']['nodes'])
            page_info = data['data']['node']['comments']['pageInfo']
            if page_info['hasNextPage']:
                cursor = page_info['endCursor']
            else:
                break
        else:
            raise Exception(f"Query failed with status code {response.status_code}. {response.json()}")
    return comments

def fetch_discussions_by_category(owner, repo, category_id):
    """
    Fetches discussions by category from a GitHub repository.

    Args:
        owner (str): GitHub repository owner.
        repo (str): GitHub repository name.
        category_id (str): ID of the discussion category.

    Returns:
        list: List of discussions.
    """
    discussions = []
    cursor = None
    while True:
        query = """
        {
          repository(owner: "%s", name: "%s") {
            discussions(first: 10, categoryId: "%s", after: %s) {
              pageInfo {
                endCursor
                hasNextPage
              }
              nodes {
                id
                title
                author {
                  login
                }
                createdAt
                reactions(first: 50) {
                  nodes {
                    content
                  }
                }
              }
            }
          }
        }
        """ % (owner, repo, category_id, f'"{cursor}"' if cursor else "null")

        response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
        if response.status_code == 200:
            data = response.json()
            discussions_batch = data['data']['repository']['discussions']['nodes']
            for discussion in discussions_batch:
                discussion_id = discussion['id']
                if DEBUG:
                    st.write(f"Processing Discussion ID: {discussion_id}")
                discussion['comments'] = fetch_comments_and_replies(discussion_id)
                discussions.append(discussion)
            page_info = data['data']['repository']['discussions']['pageInfo']
            if page_info['hasNextPage']:
                cursor = page_info['endCursor']
            else:
                break
        else:
            raise Exception(f"Query failed with status code {response.status_code}. {response.json()}")
    return discussions

def get_week_bucket(date_str):
    """
    Determines the week bucket for a given date.

    Args:
        date_str (str): Date string in ISO format.

    Returns:
        str: Week bucket in the format 'Month Day, Year'.
    """
    date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    # Find the previous Sunday
    sunday = date - timedelta(days=date.weekday() + 1) if date.weekday() != 6 else date
    return sunday.strftime('%b %d, %Y')

def calculate_scores(discussions):
    """
    Calculates scores for each user based on their activities.

    Args:
        discussions (list): List of discussions with comments and replies.

    Returns:
        dict: Weekly scores for each user.
    """
    weekly_scores = defaultdict(lambda: defaultdict(int))
    for discussion in discussions:
        seen_users = set()  # Track users who have replied in this discussion
        for comment in discussion['comments']:  # These are the questions
            question_author = comment['author']['login']
            comment_week = get_week_bucket(comment['createdAt'])
            #print(f"Question Author: {question_author}, Week: {comment_week}")
            if question_author not in IGNORED_USERS:
                #                print(f"Ignored Question ID: {comment['id']}, Text: {comment['bodyText']}, Author: {question_author} (ignored user), Week: {comment_week}")
                #                continue
                points_for_question = Y + sum(1 for reaction in comment['reactions']['nodes'] if reaction['content'] in ['THUMBS_UP', 'THUMBS_DOWN']) * X
                weekly_scores[comment_week][question_author] += points_for_question
            if DEBUG:
                st.write(f"Question ID: {comment['id']}, Text: {comment['bodyText']}, Author: {question_author}, Points for Question: {points_for_question}, Week: {comment_week}")
            for reply in comment['replies']['nodes']:  # These are the replies
                reply_author = reply['author']['login']
                reply_week = get_week_bucket(reply['createdAt'])
                #print(f"Reply Author: {reply_author}, Week: {reply_week}")
                # if reply_author in IGNORED_USERS:
                #     print(f"Ignored Reply ID: {reply['id']}, Text: {reply['bodyText']}, Author: {reply_author} (ignored user), Week: {reply_week}")
                #     continue
                if reply_author == question_author:
                    if DEBUG:
                        st.write(f"Ignored Reply ID: {reply['id']}, Text: {reply['bodyText']}, Author: {reply_author} (replied to own question), Week: {reply_week}")
                    continue
                if reply_author not in seen_users and reply_author not in IGNORED_USERS:
                    points_for_reply = Z + sum(1 for reaction in reply['reactions']['nodes'] if reaction['content'] in ['THUMBS_UP', 'THUMBS_DOWN']) * X
                    weekly_scores[reply_week][reply_author] += points_for_reply
                    seen_users.add(reply_author)
                    if DEBUG:
                        st.write(f"Reply ID: {reply['id']}, Text: {reply['bodyText']}, Author: {reply_author}, Points for Reply: {points_for_reply}, Week: {reply_week}")
                else:
                    if DEBUG:
                        st.write(f"Ignored Reply ID: {reply['id']}, Text: {reply['bodyText']}, Author: {reply_author} (already participated), Week: {reply_week}")

    return weekly_scores

def display_leaderboard(weekly_scores):
    """
    Displays the leaderboard in various sections.

    Args:
        weekly_scores (dict): Weekly scores for each user.
    """
    st.title('Document Feedback Leaderboard')

    # Calculate all-time scores
    all_time_scores = defaultdict(int)
    for week, scores in weekly_scores.items():
        for user, score in scores.items():
            all_time_scores[user] += score

    # Display top 5 all-time leaders
    st.header('All Time Top 5 Leaders')
    all_time_leaderboard = sorted(all_time_scores.items(), key=lambda x: x[1], reverse=True)[:5]
    for rank, (user, score) in enumerate(all_time_leaderboard, 1):
        st.write(f'{rank}. {user} - {score} points')

    # Weekly Trends
    st.header('Weekly Trends')

    # Aggregate weekly scores
    weekly_aggregate_scores = {week: sum(scores.values()) for week, scores in weekly_scores.items()}

    # Plot bar chart
    weeks = list(weekly_aggregate_scores.keys())
    scores = list(weekly_aggregate_scores.values())
    plt.figure(figsize=(10, 5))
    bars = plt.bar(weeks, scores, color='skyblue')
    plt.xlabel('Week')
    plt.ylabel('Total Points')
    plt.title('Weekly Aggregate Scores')
    plt.xticks(rotation=45)

    # Adding value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height}', ha='center', va='bottom')

    st.pyplot(plt)

    # Display weekly scores in sections
    sorted_weeks = sorted(weekly_scores.keys(), key=lambda x: datetime.strptime(x, '%b %d, %Y'), reverse=True)
    for week in sorted_weeks:
        st.header(f"Week of {week}")
        leaderboard = sorted(weekly_scores[week].items(), key=lambda x: x[1], reverse=True)
        for rank, (user, score) in enumerate(leaderboard, 1):
            st.write(f'{rank}. {user} - {score} points')

    # Display full score list
    st.header('All Participants - Full Score List')
    full_leaderboard = sorted(all_time_scores.items(), key=lambda x: x[1], reverse=True)
    for rank, (user, score) in enumerate(full_leaderboard, 1):
        st.write(f'{rank}. {user} - {score} points')

def update_leaderboard(placeholder):
    """
    Function to fetch data and update the leaderboard on load.
    """
    with placeholder.container():
        owner, repo = GITHUB_REPO.split('/')
        categories_result = fetch_discussion_categories(owner, repo)
        categories = categories_result['data']['repository']['discussionCategories']['nodes']

        # Use the global variable DISCUSSION_CATEGORY
        category_id = None
        for category in categories:
            if category['name'] == DISCUSSION_CATEGORY:
                category_id = category['id']
                break

        if category_id:
            discussions_result = fetch_discussions_by_category(owner, repo, category_id)
            discussions = discussions_result
            weekly_scores = calculate_scores(discussions)
            display_leaderboard(weekly_scores)
        else:
            st.error(f'Category "{DISCUSSION_CATEGORY}" not found')

def main():
    """
    Main function to run the Streamlit app and update the leaderboard.
    """
    placeholder = st.empty()
    st.sidebar.button('Update Leaderboard', on_click=update_leaderboard, args=(placeholder,))
    update_leaderboard(placeholder)  # Update leaderboard on load

if __name__ == '__main__':
    main()
