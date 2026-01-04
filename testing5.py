import requests

API_URL = "https://ghibliapi.herokuapp.com/films"

def get_films():
    """Fetch films from Ghibli API"""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()  # Raise error if API fails
        return response.json()
    except requests.exceptions.ConnectionError:
        print("❌ No internet connection.")
        return None
    except requests.exceptions.HTTPError:
        print("❌ API returned an error.")
        return None
    except requests.exceptions.Timeout:
        print("❌ Request timed out.")
        return None

def filter_films(films, min_year, min_score):
    """Return films matching criteria"""
    filtered = []
    for film in films:
        try:
            if int(film["release_date"]) >= min_year and int(film["rt_score"]) >= min_score:
                filtered.append(film)
        except:
            continue
    # Sort by Rotten Tomatoes score descending
    filtered.sort(key=lambda f: int(f["rt_score"]), reverse=True)
    return filtered

def display_films(films):
    if not films:
        print("⚠️ No films match your criteria.")
        return
    print("\n🎬 Matching Studio Ghibli Films:\n")
    for film in films:
        print(f"Title: {film['title']}")
        print(f"Director: {film['director']}")
        print(f"Year: {film['release_date']}")
        print(f"Rotten Tomatoes Score: {film['rt_score']}")
        print("-"*30)
    # Save to file
    with open("ghibli_films.txt", "w", encoding="utf-8") as f:
        for film in films:
            f.write(f"{film['title']} ({film['release_date']}) - Score: {film['rt_score']}\n")
    print("\n💾 Results saved to ghibli_films.txt")

def main():
    print("🌟 Welcome to the Studio Ghibli Explorer!")
    try:
        min_year = int(input("Enter minimum release year (e.g., 2000): "))
        min_score = int(input("Enter minimum Rotten Tomatoes score (0-100): "))
    except ValueError:
        print("❌ Please enter valid numbers.")
        return

    films = get_films()
    if films is None:
        return

    filtered = filter_films(films, min_year, min_score)
    display_films(filtered)

if __name__ == "__main__":
    main()
