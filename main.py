import sys
from stats import get_word_count, get_sorted_character_list

def get_book_text(filename):
    try:
        with open(filename) as f:
            file_contents = f.read()
            return file_contents
    except:
        print(f"File does not exist! ({filename})")
        sys.exit(1)

def main():
    try:
        filename = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(filename)
    word_count = get_word_count(text)
    character_count = get_sorted_character_list(text)

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filename}")
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")
    for character in character_count:
        char = character["char"]
        num = character["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

main()
