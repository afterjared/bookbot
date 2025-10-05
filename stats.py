def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    print(f"Found {num_words} total words")
    print(f"Dictionary: {character_count}")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    for character in text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count 


main()