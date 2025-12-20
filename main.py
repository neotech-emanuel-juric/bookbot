from stats import count_words


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    text = get_book_text("books/frankenstein.txt")
    count = count_words(text)
    print(f"Found {count} total words")


if __name__ == "__main__":
    main()
