import sys

if len(sys.argv)  < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
book = sys.argv[1]

def get_book_text(book) :
	with open(book) as f:
		file_contents = f.read()
	return file_contents

from stats import num_of_words
from stats import num_of_appearances
from stats import sort_on

def main(book):
	contents = get_book_text(book)
	num_message = f"Found {num_of_words(contents)} total words"
	number_dict = num_of_appearances(contents)
	sorted = sort_on(number_dict)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book}...")
	print("----------- Word Count ----------")
	print(num_message)
	print("--------- Character Count -------") 
	for item in sorted:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============")
 
main(book) 

