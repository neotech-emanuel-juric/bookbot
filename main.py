from stats import count_each_char, count_words


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    text = get_book_text("books/frankenstein.txt")
    count = count_words(text)
    print(f"Found {count} total words")
    print(count_each_char(text))


if __name__ == "__main__":
    main()
