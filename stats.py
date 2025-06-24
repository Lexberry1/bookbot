def num_of_words(file_contents):
        words_list =  file_contents.split()
        num_words  = len(words_list) 
        return num_words

def num_of_appearances(file_contents):
	number_count = {}
	lower_string = file_contents.lower()
	for char in lower_string:
		if char not in number_count:
			number_count[char] = 1
		else:
			number_count[char] +=1
	return number_count

def sorting(item):
	return item["num"]

def sort_on(number_count):
	char_num = {}
	char_num_list = []
	for char in number_count:
		char_num = {"char" : char, "num" : number_count[char]}	
		char_num_list.append(char_num)

	def sorting(item):
		return item["num"]
	char_num_list.sort(reverse=True, key=sorting)
	return char_num_list

