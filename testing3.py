import requests

API_URL = "https://ghibliapi.herokuapp.com/films"


def get_films():
    """Fetch film data from the Ghibli API."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectionError:
        print("❌ Error: No internet connection.")
        return None
    except requests.exceptions.HTTPError:
        print("❌ Error: API returned an error.")
        return None
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out.")
        return None
    except ValueError:
        print("❌ Error: Invalid JSON response.")
        return None


def process_films(films, min_year, min_score):
    """Filter and sort films based on user criteria."""
    filtered_films = []

    for film in films:
        try:
            release_year = int(film["release_date"])
            score = int(film["rt_score"])

            if release_year >= min_year and score >= min_score:
                filtered_films.append(film)

        except (ValueError, KeyError):
            continue

    filtered_films.sort(key=lambda f: int(f["rt_score"]), reverse=True)
    return filtered_films


def display_results(films):
    """Display films in a clean, readable format."""
    if not films:
        print("⚠️ No films match your criteria.")
        return

    print("\n🎥 Matching Studio Ghibli Films:\n")

    for film in films:
        print(
            f"Title: {film['title']}\n"
            f"Director: {film['director']}\n"
            f"Release Year: {film['release_date']}\n"
            f"Rotten Tomatoes Score: {film['rt_score']}\n"
            "----------------------------------"
        )


def save_to_file(films):
    """Save results to a text file."""
    with open("ghibli_films.txt", "w", encoding="utf-8") as file:
        for film in films:
            file.write(
                f"{film['title']} ({film['release_date']}) - "
                f"Score: {film['rt_score']}\n"
            )
    print("💾 Results saved to ghibli_films.txt")


def main():
    print("🌸 Welcome to the Studio Ghibli Film Explorer")

    try:
        min_year = int(input("Enter minimum release year: "))
        min_score = int(input("Enter minimum Rotten Tomatoes score: "))

        if min_year < 1900 or not (0 <= min_score <= 100):
            raise ValueError

    except ValueError:
        print("❌ Invalid input. Please enter valid numbers.")
        return

    films = get_films()
    if films is None:
        return

    results = process_films(films, min_year, min_score)
    display_results(results)
    save_to_file(results)


if __name__ == "__main__":
    main()
