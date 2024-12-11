def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(f"{chars}")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}
    lowered_words = "".join(text).lower()

    for letter in lowered_words:
        if letter in chars:
            chars[letter] += 1
        else: 
            chars[letter] = 1

    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
