def organize_books(reading_log):
    dict={}
    for item in reading_log:
        items=item.split(",")

        genre=items[0]
        book_title=items[1]
        pagecount=int(items[2])
        if genre not in dict:
            dict[genre]=[]
        dict[genre].append((book_title,pagecount))
    return dict

def print_genre_stats(library_dict):
    for genre,info in library_dict.items():
        all_pages=0
        for book_title, pagecount in info:
            all_pages+=pagecount
        print(f"{genre}: {all_pages} pages total")

reading_log = [
    "Fantasy,The Hobbit,310",
    "SciFi,Dune,412",
    "Fantasy,Harry Potter,223",
    "Mystery,Sherlock Holmes,300",
    "SciFi,Ender's Game,324",
    "Fantasy,The Alchemist,160"]
        

asd=organize_books(reading_log)
print_genre_stats(asd)