# This script fetches data from the Google Books API and prints the status code of the response.

# Importing the requests library to handle HTTP requests.
import requests
import json

# This URL is for the Google Books API, specifically querying for books related to "python".
book_url = "https://www.googleapis.com/books/v1/volumes?q=python"

# Sending a GET request to the specified URL.
response = requests.get(book_url)

# Printing the status code of the response to check if the request was successful.
print(f"Status Code: {response.status_code}")

# # If the request was successful (status code 200), it prints the response data.
# if response.status_code == 200:
#     book_info = response.json()
#     # print(book_info)
#     print(json.dumps(book_info, indent=2))  # Pretty print the JSON response

book_info = response.json()
items = book_info.get('items', [])
# Loop through each item in the items list and print the title and authors.

if items:
    book = items[0]  # Get the first book item
    volume_info = book.get('volumeInfo', {})
    
    for key , value in volume_info.items():
        print(f"{key}: {value}")
else:
    print("No books found for the query.")


