def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)


if __name__ == "__main__":
    main()
