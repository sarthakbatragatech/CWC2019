# https://github.com/hardikvasa/google-images-download
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

india_squad = ['Virat Kohli', 'Rohit Sharma', 'Shikhar Dhawan']

for player in india_squad:

    arguments = {
        'keywords': player,
        'limit': 5,
        'print_urls': True,
        # 'no_download': 'nd'
        }

    absolute_image_paths = response.download(arguments)
    print(arguments)
