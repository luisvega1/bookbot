import sys
from stats import words_counter, char_counter, sort_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        content = get_book_text(file_path)
        words_count = words_counter(content)
        char_counts = char_counter(content)
        sorted_list = sort_dict(char_counts)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            if item['char'].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
main()
