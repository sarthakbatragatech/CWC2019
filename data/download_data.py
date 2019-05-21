# https://github.com/hardikvasa/google-images-download
from google_images_download import google_images_download
from squads import all_squads

response = google_images_download.googleimagesdownload()

for squad in all_squads:
    for player in squad:

        arguments = {
            'keywords': player + ' cricketer',
            'limit': 5,
            'print_urls': True,
            'image_directory': player
            # 'no_download': 'nd'
            }

        absolute_image_paths = response.download(arguments)
        # print(arguments)
