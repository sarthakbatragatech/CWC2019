# https://github.com/hardikvasa/google-images-download
from google_images_download import google_images_download
from squads import all_squads

response = google_images_download.googleimagesdownload()

# Download image data for all 10 teams
for squad in all_squads:
    # Each player's data is stored in a folder named after him
    for player in squad:

        arguments = {
            'keywords': player + ' cricketer',
            'limit': 25,
            'print_urls': True,
            'image_directory': player
            # 'no_download': 'nd'
            }

        absolute_image_paths = response.download(arguments)
        # print(arguments)

        print(f'Finished downloading data for {player}')

    print(f'Finished downloading data for {squad}')

print("Finished downloading data for all squads")
