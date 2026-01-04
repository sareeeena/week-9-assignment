import requests

BASE_URL = "https://api.jikan.moe/v4/anime"

def get_anime_info(query):
    """Fetch anime info from Jikan API based on search query"""
    try:
        url = f"{BASE_URL}?q={query}&limit=1"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data['data']:
            return data['data'][0]  # Get the first search result
        else:
            print("⚠️ No anime found with that name.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        return None

def display_anime_info(anime):
    """Display anime info nicely"""
    print("\n🎌 Anime Information\n")
    print(f"Title       : {anime.get('title')}")
    print(f"Type        : {anime.get('type')}")
    print(f"Episodes    : {anime.get('episodes')}")
    print(f"Score       : {anime.get('score')}")
    print(f"Status      : {anime.get('status')}")
    print(f"Synopsis    : {anime.get('synopsis')}\n")
    print("💾 Saved to anime_info.txt")

def save_to_file(anime):
    """Save anime info to a file"""
    with open("anime_info.txt", "w", encoding="utf-8") as f:
        f.write(f"Title       : {anime.get('title')}\n")
        f.write(f"Type        : {anime.get('type')}\n")
        f.write(f"Episodes    : {anime.get('episodes')}\n")
        f.write(f"Score       : {anime.get('score')}\n")
        f.write(f"Status      : {anime.get('status')}\n")
        f.write(f"Synopsis    : {anime.get('synopsis')}\n")

def main():
    print("🎌 Welcome to the Anime Info Explorer!")
    query = input("Enter the name of the anime: ").strip()
    if not query:
        print("❌ Please enter a valid anime name.")
        return

    anime = get_anime_info(query)
    if anime is None:
        return

    display_anime_info(anime)
    save_to_file(anime)

if __name__ == "__main__":
    main()

