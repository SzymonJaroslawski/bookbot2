def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_num_chars(text)
    chars_sorted_list = chars_to_list(chars)
    print(f"--- Being raport of {book_path} ---")
    print(f"{num_words} words found in the document \n")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End raport ---")

# split text into words and counts them
def get_num_words(text):
    words = text.split()
    return len(words)

# return "num" value of sorting dictionary
def sort_on(d):
    return d["num"]

# convert dictionary into list of it for each letter
def chars_to_list(disc):
    sorted_list = []

    for ch in disc:
        sorted_list.append({"char": ch, "num": disc[ch]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# count chars in text, convert into small caps and count each chars into dictionary
def get_num_chars(text):
    chars = {}
    lowered_words = "".join(text).lower()

    for letter in lowered_words:
        if letter in chars:
            chars[letter] += 1
        else: 
            chars[letter] = 1
        
    return chars

# open and read file
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
