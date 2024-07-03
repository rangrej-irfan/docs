
ssh ask-privacera "mkdir -p ~/discussion_leaderboard"
rsync -avz src run_leader_board.sh ask-privacera:~/discussion_leaderboard
ssh ask-privacera "cd ~/discussion_leaderboard && ./run_leader_board.sh"
