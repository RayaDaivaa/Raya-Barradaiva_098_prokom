def make_album(artist, title):
    return {"artist": artist,"title": title}


while True:
    print("\nEnter album information.")
    print("Enter 'q' to quit.")

    artist = input("Artist name: ")
    if artist.lower() == "q":
        break

    title = input("Album title: ")
    if title.lower() == "q":
        break

    album = make_album(artist, title)
    print(album)