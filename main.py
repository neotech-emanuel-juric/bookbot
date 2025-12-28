from stats import count_each_char, count_words, sort_count_charts


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    count = count_words(text)
    count_chars = count_each_char(text)

    ## Printing

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for value in sort_count_charts(count_chars):
        print(f"{value['char']}: {value['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
