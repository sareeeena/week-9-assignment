import requests

API_BASE = "https://kitsu.io/api/edge/anime"

def search_anime(query):
    headers = {
        "Accept": "application/vnd.api+json",
        "Content-Type": "application/vnd.api+json"
    }
    try:
        # Search by text
        response = requests.get(f"{API_BASE}?filter[text]={query}", headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data:", e)
        return None

def display_info(data):
    if not data or not data.get("data"):
        print("⚠️ No results found.")
        return

    anime = data["data"][0]["attributes"]
    title = anime.get("canonicalTitle") or anime.get("titles", {}).get("en")
    episodes = anime.get("episodeCount")
    synopsis = anime.get("synopsis")
    print("\n🎌 Anime Info:\n")
    print(f"Title      : {title}")
    print(f"Episodes   : {episodes}")
    print(f"Synopsis   : {synopsis}\n")

def main():
    name = input("Enter anime name to search: ").strip()
    if not name:
        print("❌ Please enter a valid name.")
        return

    result = search_anime(name)
    display_info(result)

if __name__ == "__main__":
    main()


