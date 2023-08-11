# import requests
# from bs4 import BeautifulSoup
#
#
# def extract_bird_species(url):
#     bird_species = []
#
#     # Send a GET request to the url
#     response = requests.get(url)
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the content of the webpage using BeautifulSoup
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # Find all the links on the page
#         links = soup.find_all('a', href=True)
#
#         # Extract bird species from the links
#         for link in links:
#             href = link['href']
#             if "/species/" in href:
#                 species = href.split("/")[-1]
#                 bird_species.append(species)
#
#     return bird_species

#
# # website url
# url = "https://xeno-canto.org"
#
# # Extract bird species
# species_list = extract_bird_species(url)
#
# # Print the list of bird species
# for species in species_list:
#     print(species)

import requests
from bs4 import BeautifulSoup
import csv

def extract_bird_species(url):
    bird_species = []

    # Send a GET request to the url
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the links on the page
        links = soup.find_all('a', href=True)

        # Extract bird species from the links
        for link in links:
            href = link['href']
            if "/species/" in href:
                species = href.split("/")[-1]
                bird_species.append(species)

    return bird_species

# website url
url = "https://xeno-canto.org/collection/species/latest"

# Extract bird species
species_list = extract_bird_species(url)

# Print the list of bird species
for species in species_list:
    print(species)

# Convert the species list to a CSV file
csv_filename = "species.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Bird Species'])
    writer.writerows([[species] for species in species_list])

print(f"CSV file '{csv_filename}' has been created.")
