def count_words(text: str) -> int:
    count = 0
    txt = text.split()  # This has to be done, so that words are split from the string. Otherwise I would have counted every char

    for word in txt:
        count += 1
    return count


def count_each_char(text: str) -> dict:
    counted_chars = {}

    for char in text:
        char_l = char.lower()
        if char_l not in counted_chars:
            counted_chars[char_l] = 0
            counted_chars[char_l] += 1
        else:
            counted_chars[char_l] += 1

    return counted_chars
