def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    print(book_contents)

def main():
    return get_book_text("books/frankenstein.txt")

main()