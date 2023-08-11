# #
# # import requests
# #
# # def extract_bird_songs(url):
# #     bird_songs = []
# #
# #     # Send a GET request to the API endpoint
# #     response = requests.get(url)
# #
# #     # Check if the request was successful
# #     if response.status_code == 200:
# #         # Get the JSON data from the response
# #         data = response.json()
# #
# #         # Extract bird songs from the JSON data
# #         for recording in data['recordings']:
# #             bird_songs.append(recording['file'])
# #
# #     return bird_songs
# #
# # # API endpoint url
# # api_url = "https://xeno-canto.org/api/2/recordings"
# #
# # # Extract bird songs
# # bird_songs_list = extract_bird_songs(api_url)
# #
# # # Print the list of bird songs
# # for song_url in bird_songs_list:
# #     print(song_url)
# #     print("complete")
#
# # import requests
# # from bs4 import BeautifulSoup
# # import os
# #
# #
# # def extract_bird_songs(url):
# #     # Send an HTTP request to the website
# #     response = requests.get(url)
# #
# #     if response.status_code != 200:
# #         print("Failed to fetch the webpage.")
# #         return
# #
# #     # Parse the HTML content using BeautifulSoup
# #     soup = BeautifulSoup(response.text, 'html.parser')
# #
# #     # Find all links to bird song recordings
# #     bird_songs = []
# #     for link in soup.find_all('a', href=True):
# #         href = link.get('href')
# #         if "download" in href and "type=3" in href:
# #             bird_songs.append(href)
# #
# #     return bird_songs
# #
# #
# # def download_bird_songs(bird_songs):
# #     # Create a directory to store the downloaded bird songs
# #     if not os.path.exists("bird_songs"):
# #         os.makedirs("bird_songs")
# #
# #     # Download the bird songs
# #     for idx, song_url in enumerate(bird_songs, start=1):
# #         response = requests.get(song_url)
# #         if response.status_code == 200:
# #             file_name = f"bird_song_{idx}.mp3"
# #             with open(os.path.join("bird_songs", file_name), 'wb') as f:
# #                 f.write(response.content)
# #             print(f"Downloaded {file_name}")
# #         else:
# #             print(f"Failed to download {song_url}")
# #
# #
# # if __name__ == "__main__":
# #     # Replace the URL below with the desired Xeno-Canto page
# #     xeno_canto_url = "https://xeno-canto.org/api/2/recordings"
# #
# #     bird_songs = extract_bird_songs(xeno_canto_url)
# #     if bird_songs:
# #         download_bird_songs(bird_songs)
#
# import requests
#
#
# def get_all_bird_songs():
#     base_url = "https://xeno-canto.org/explore?query=since:31&dir=0&order=xc"
#     all_bird_songs = []
#     page = 1
#
#     while True:
#         url = f"{base_url}?page={page}"
#         response = requests.get(url)
#
#         if response.status_code == 200:
#             data = response.json()
#             recordings = data['recordings']
#
#             if not recordings:
#                 break
#
#             for recording in recordings:
#                 bird_song_url = recording['file']
#                 all_bird_songs.append(bird_song_url)
#
#             page += 1
#         else:
#             print(f"Error while fetching data from page {page}")
#             break
#
#     return all_bird_songs
#
#
# if __name__ == "__main__":
#     bird_songs = get_all_bird_songs()
#     print(f"Total bird songs: {len(bird_songs)}")
#     for index, song_url in enumerate(bird_songs, start=1):
#         print(f"{index}. {song_url}")