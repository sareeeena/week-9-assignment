import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            # The API returns a list of matches, we take the first one [0]
            data = response.json()[0]
            
            # Navigating nested JSON
            common_name = data['name']['common']
            capital = data['capital'][0]
            population = data['population']
            
            print(f"Country: {common_name}")
            print(f"Capital: {capital}")
            print(f"Population: {population:,}") # Format with commas
        elif response.status_code == 404:
            print("Error: Country not found.")
        else:
            print(f"Server Error: {response.status_code}")
            
    except requests.exceptions.RequestException:
        # Catches DNS failures, no internet, etc.
        print("Error: Could not connect to the internet.")

get_country_info("uzbekistan")