authors = {
    "Author #1": [
        "#1 Book #1",
        "#1 Book #2",
        "#1 Book #3"
    ],
    "Author #2": [
        "#2 Book #1",
        "#2 Book #2",
        "#2 Book #3"
    ],
    "Author #3": [
        "#3 Book #1",
        "#3 Book #2",
        "#3 Book #3"
    ]
}

author_user_input = input("Enter author name: ")
if author_user_input not in authors.keys():
    print(f"Author({author_user_input}) not found in dictionary!")
else:
    print("List of Author's books: ")
    for book in authors[author_user_input]:
        print(f"\t{book}")
