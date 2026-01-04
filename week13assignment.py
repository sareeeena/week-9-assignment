import requests

def get_anime_info(anime_name):
    url = f"https://kitsu.io/api/edge/anime?filter[text]={anime_name}"
    
    try:
        response = requests.get(url) 
        
        if response.status_code == 200:
            data = response.json()
            # print(data)
            
            if data['data']==[]:
                print(f"No anime found with this name {anime_name}")
                return
            
            anime = data['data'][0]['attributes']
            title = anime['canonicalTitle']
            episodes = anime['episodeCount']
            synopsis = anime['synopsis']
            
            print("-"*50)
            print(f"\n Anime Information")
            print(f"Title    : {title}")
            print(f"Episodes : {episodes}")
            print(f"Synopsis : {synopsis}")
        
            with open("anime_info.txt", "w") as f:
                f.write(f"Title    : {title}\n")
                f.write(f"Episodes : {episodes}\n")
                f.write(f"Synopsis : {synopsis}\n")
                f.close()
        
        elif response.status_code == 404:
            print("Error: Anime not found")
        else:
            print(f"Server Error: {response.status_code}")
    
    except requests.exceptions.RequestException:
        print("Error: Could not connect to the internet")

print("  Welcome to the Anime World!  ")
user_input = input("Enter the name of the anime: ")

get_anime_info(user_input)


