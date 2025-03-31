from stats import get_num_words
from stats import get_character_count
import sys


def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents


def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = arguments[1]
    content = get_book_text(path)
    word_count = get_num_words(content)
    character_count = get_character_count(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in character_count:
        print(f"{char}: {character_count[char]}")


main()
