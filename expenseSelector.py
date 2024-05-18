import requests
from bs4 import BeautifulSoup
import csv


print("Select which registry cost-quality ratio that you would prefer.")
print("1. Expensive - high quality items.")
print("2. Balanced - quality-to-price ratio")
print("3. Cost-Effective - better price-to-performance")
print()
choice = input("Enter your choice 1, 2, or 3. ")

if choice == '1':
    print("Expensive - high quality items.")
    print()
    print("Great! You selected the Expensive choice.")
    print()
elif choice == '2':
    print("Balanced - quality-to-price ratio")
    print()
    print("Great! You selected the Balanced choice.")
    print()
elif choice == '3':
    print("Cost-Effective - better price-to-performance")
    print()
    print("Great! You selected Cost-Effective choice.")
    print()
else:
    print("Oops! Wrong choice. Please select 1, 2, or 3.")
    print()


# Target URL
url = "https://www.target.com/c/strollers-travel-gear-baby/-/N-5xtc3"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the product listings
product_listings = soup.find_all("div", class_="styles__StyledDiv-sc-fw90uk-0 fHlewe")

#
# Needs API call.
#

# Open a CSV file for writing
with open("baby_strollers2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Product Name", "Price", "Rating"])

    # Loop through each product listing and extract the relevant data
    for listing in product_listings:
        product_name = listing.find("h2", class_="h-padding-a-tight")
        price = listing.find("span", class_="h-text-bold")
        rating = listing.find("span", class_="h-display-inline-block")
        writer.writerow([product_name, price, rating])