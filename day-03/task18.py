library = {
    101: {
        "title": "C Programming",
        "author": "Jonny",
        "copies": 5
    },

    102: {
        "title": "Javascript Programming",
        "author": "Jassica",
        "copies": 3
    },

    103: {
        "title": "Game Development",
        "author": "Danial",
        "copies": 4
    }
}

book_id = 102

if book_id in library:

    if library[book_id]["copies"] > 0:

        library[book_id]["copies"] -= 1

        print("Book Issued Successfully!")

    else:
        print("Book Not Available!")

else:
    print("Book Not Found!")

print("Updated Library:")
print(library)