from random import randint, choice

def read_text(filename):
	with open(filename, "r") as file:
		contents = file.read().replace('\n\n',' ')
	return contents

def mchain(text, chain):
	words = text.split(' ')
	i = 1
	j = 0
	
	for w in words[i:]:
		key = words[i - 1]

		if key in chain:
			chain[key].append(w)
		else:
			chain[key] = [w]

		i = i + 1
		j = j + 1
	
	key = words[j]
	chain[key] = ['']

	return chain

def message(chain, count):
    word1 = choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    
    return message