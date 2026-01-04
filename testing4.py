import requests

API_URL = "https://catfact.ninja/facts"

def get_cat_facts():
    """Fetch cat facts from API"""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
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

def process_facts(data, num):
    """Select the number of facts requested"""
    facts = [item['fact'] for item in data['data']]
    return facts[:num]

def display_facts(facts):
    """Print the facts nicely"""
    if not facts:
        print("⚠️ No facts available.")
        return
    print("\n😺 Cat Facts:\n")
    for i, fact in enumerate(facts, 1):
        print(f"{i}. {fact}")
    print("\n💾 Facts saved to cat_facts.txt")

def save_to_file(facts):
    """Save facts to a text file"""
    with open("cat_facts.txt", "w", encoding="utf-8") as f:
        for fact in facts:
            f.write(f"{fact}\n")

def main():
    print("🐱 Welcome to the Cat Fact Explorer")
    try:
        num = int(input("How many cat facts do you want? "))
        if num <= 0:
            raise ValueError
    except ValueError:
        print("❌ Please enter a positive number.")
        return

    data = get_cat_facts()
    if data is None:
        return

    facts = process_facts(data, num)
    display_facts(facts)
    save_to_file(facts)

if __name__ == "__main__":
    main()
