def search(f):
    print("Searching...")

    sections = ""
    books = "Books:\n"

    with open(f) as file:
        for line in file:
            if line.startswith("Section"):
                sections = sections + line
            else:
                books = books + line

    print("Done!")

    return f"{sections}\n\n{books}"


def save(f, data):
    print("Saving...")
    with open(f, "w") as file:
        file.write(data)
    print("Done!")


def run():
    info = search("books.txt")
    save("exported_books.txt", info)


if __name__ == "__main__":
    run()