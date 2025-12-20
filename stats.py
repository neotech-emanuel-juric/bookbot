def count_words(text: str) -> int:
    count = 0
    txt = text.split()  # This has to be done, so that words are split from the string. Otherwise I would have counted every char

    for word in txt:
        count += 1
    return count
