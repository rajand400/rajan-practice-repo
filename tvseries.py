import requests

url = "https://api.tvmaze.com/search/shows?q=breaking"

response = requests.get(url)
print(f"Status Code: {response.status_code}")\

if response.status_code == 200:
    shows = response.json()
    print(shows)
    if shows:
        for show in shows:
            show_info = show.get('show', {})
            print(f"Title: {show_info.get('name')}")
            print(f"Premiered: {show_info.get('premiered')}")
            print(f"Summary: {show_info.get('summary')}")
            print(f"Rating: {show_info.get('rating', {}).get('average')}")
            print("-" * 40) 
    else:
        print("No shows found for the query.")
else:
    print(f"Error fetching data: {response.status_code}")