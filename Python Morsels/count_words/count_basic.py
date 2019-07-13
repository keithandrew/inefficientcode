"""Python Morsels Problem 01/07/2019"""

def count_words(string):

	"""
	This function takes in a string, and indexes it based on frequency of usage
	"""

	# define storage dictionary and word list, forcing words to lower case
	index_dict = {}

	# interate through the list and update dictionary values
	for word in string.split():
		if word in index_dict:
			index_dict[word] += 1
		else:
			index_dict.update({word: 1})

	return index_dict
