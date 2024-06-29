import os
import re


# This script lists all images in the "docs/images" folder that are not used in any of the .md files in the "docs" folder.

# Function to list all image files in the "docs/images" folder
def list_images(folder):
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg']
    return [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in image_extensions]

# Function to list all .md files in "docs" and its subfolders
def list_md_files(folder):
    md_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

# Function to check if an image is used in any of the .md files
def is_image_used(image, md_files, images_folder):
    image_path = os.path.relpath(os.path.join(images_folder, image), os.path.dirname(md_files[0]))
    for md_file in md_files:
        with open(md_file, 'r') as file:
            content = file.read()
            if re.search(r'!\[.*\]\(.*{}.*\)'.format(re.escape(image)), content):
                return True
    return False

# Main function to list unused images
def list_unused_images():
    images_folder = 'docs/images'
    docs_folder = 'docs'

    images = list_images(images_folder)
    md_files = list_md_files(docs_folder)
    unused_images = [img for img in images if not is_image_used(img, md_files, images_folder)]

    return unused_images

if __name__ == "__main__":
    unused_images = list_unused_images()
    print("Unused images:")
    for img in unused_images:
        print(img)
