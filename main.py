import requests

def fetch_jobs(query, location, api_key):
    print("Fetching jobs...")
    url = "https://serpapi.com/search.json"
    params = {"engine" : "google_jobs",
              "q": f"{query} {location}",
              "hl": "en",
              "api_key": api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Connection error! check your API or Internet connection")
        return None

def display_jobs(data):
    if "jobs_results" not in data:
        print("No job results found")
        print("API Response:", data.get("error", "Check your query or API key status."))
        return
    for index, job in enumerate(data["jobs_results"], start=1):
        title = job.get("title", "Unknown Title")
        company = job.get("company_name", "Unknown Company")
        location = job.get("location", "Unknown Location")
        apply_links = job.get("apply_options", [])
        link = apply_links[0].get("link") if apply_links else "No link provided"
        print(f"{index}. {title}")
        print(f"   Company:  {company}")
        print(f"   Location: {location}")
        print(f"   Link:     {link}")
        print("-" * 50)


API_KEY = "REPLACE WITH YOUR API KEY"
quit = False
while not quit:
    print("=== Search ===")
    user_query = input("What job do you need?: ")
    user_location = input("Where?: ")
    results = fetch_jobs(user_query, user_location, API_KEY)
    if results:
        display_jobs(results)
    end = input("Would you like to see more results? (y/n): \n")
    if end.lower() == "n":
        quit = True
