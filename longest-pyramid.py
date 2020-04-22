"""
A word pyramid starts with a word, and then removes one letter at a time, with each step producing another word
"""

def get_dictionary():
	with open('txt-files/words.txt') as f:
		lines = f.readlines()
		longest_word = max(len(line.strip('\n')) for line in lines)
		words = [set() for _ in range(longest_word)]
		for line in lines:
			if 'i' in line or 'a' in line:
				line = line.strip('\n')
				words[len(line)-1].add(line.strip('\n'))
	return words

def get_sub_words(word):
	"""Return all words that can be made by removing a single letter from word"""
	for i in range(len(word)):
		yield word[:i] + word[i+1:]

def get_mapping(words):
	mapping = {'a': {''}, 'i': {''}}
	for word_length in range(1, len(words)):
		for word in words[word_length]:
			subs_from_word = set()
			for sub in get_sub_words(word):
				# if the sub word is a valid word, and has a path to single letters
				if sub in mapping:
					subs_from_word.add(sub)

			# if any subs have been found, add the new word to mapping
			if subs_from_word:
				mapping[word] = subs_from_word

	return mapping

def get_paths(mappings, word, path=None):
	if not word:
		return [path]
	if not path:
		path = []

	paths = []
	for sub in mappings[word]:
		for sub_path in get_paths(mappings, sub, path + [word]):
			paths.append(sub_path)
	return paths

if __name__ == '__main__':
	words = get_dictionary()
	mappings = get_mapping(words)
	for longest_pyramid in filter(lambda x: len(x) == 11, mappings.keys()):
		print('\n'.join(map(str, get_paths(mappings, longest_pyramid))), '\n\n')

