 # introduction to web scraping
 """
# Extracting information from a website by using BeautifulSoup and parsing the html and xml code of the webpages
#
# # installation of BeautifulSoup
# pip install beautifulsoup4
# # import libarires
# from bs4 import Beautifulsoup # imports libary
# import requests/ pip install requests # fetches the tml content
# url = https://www.thenetnaija.net/videos/movies
"""

 from bs4 import BeautifulSoup
 import requests

 url = 'https://xeno-canto.org'
 response =requests.get(url)

 # Get title of website
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('title')
print(title)
#
# #todays activity
# """
# extract all bird species from this website url https://xeno-canto.org
# and generate the csv file or the JSON file format  for te bird species family and more
# extract all bird sungs from this website https://xeno-canto.org
# use this API to get data. the endpoint for the website is at https://https://xeno-canto.org/api/2/recordings.
# """
# # send work on gitub
# """
# git config --global "username"
# git config --global "useremail"
#
# srart
# git init
# git clone url
#
# to create a branch
# git branch "trevor"
# git checkout "trevor"
#
# git add .
#
# git commit -m "add html file"
# git push
#
# git status
#
# go to use this template
# ""

from bs4 import BeautifulSoup
import requests         #  fetches the HTML content from a webpage
import json

def get_bird_species_data(query):
     url = f"https://xeno-canto.org/api/2/recordings?query={query}"
     response = requests.get(url)

     if response.status_code == 200:
         data = response.json()
         bird_species_list = []

         for recording in data['recordings']:
             species_name = recording['en']
             family_name = f"{recording['gen']} {recording['sp']}"
             locality = recording['loc']
             country = recording['cnt']

             # Append the information to the list in the form of a dictionary.
             bird_species_list.append({
                 'species_name': species_name,
                 'family_name': family_name,
                 'locality': locality,
                 'country': country,
             })

         return bird_species_list
     else:
         print(f"Failed to fetch data. Status code: {response.status_code}")
         return []

 if __name__ == "__main__":
     # Get data for bird species in Uganda
     query = "cnt:Uganda"
     bird_species_data = get_bird_species_data(query)

     if bird_species_data:
         json_filename = "bird_species.json"
         with open(json_filename, 'w') as json_file:
             json.dump(bird_species_data, json_file, indent=4)
         print(f"Data saved to {json_filename}.")
     else:
         print("No data retrieved.")


# 2. Extract all the bird songs from the website.

def get_all_bird_songs():
    base_url = "https://xeno-canto.org/api/2/recordings"
    page = 1
    bird_songs = []

    while True:
        url = f"{base_url}?query=X&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_recordings = int(data['numRecordings'])
            num_pages = int(data['numPages'])

            for recording in data['recordings']:
                bird_songs.append({
                    'song_name': recording['en'],
                    'bird_family': f"{recording['gen']} {recording['sp']}",
                    'locality': recording['loc'],
                    'country': recording['cnt'],
                    'audio_url': recording['file']
                })

            if len(bird_songs) >= total_recordings:
                break

            page += 1
        else:
            print(f"Failed to fetch data for page {page}. Status code: {response.status_code}")
            break

    return bird_songs

if __name__ == "__main__":
    bird_songs_data = get_all_bird_songs()

    if bird_songs_data:
        json_filename = "bird_songs.json"
        with open(json_filename, 'w') as json_file:
            json.dump(bird_songs_data, json_file, indent=4)
        print(f"Data saved to {json_filename}.")
    else:
        print("No data retrieved.")

