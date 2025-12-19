def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        content = f.read()
    return content


def count_words(text: str) -> int:
    count = 0
    txt = text.split()  # This has to be done, so that words are split from the string. Otherwise I would have counted every char

    for word in txt:
        count += 1
    return count


def main():
    text = get_book_text("books/frankenstein.txt")
    count = count_words(text)
    print(f"Found {count} total words")


if __name__ == "__main__":
    main()
