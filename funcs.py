import sqlite3
from random import random, randint, choice

def create_db():
	sqlite3_file = '/Users/adriankonstantinov/Documents/Projects/groupme_bot/db/wb.db'

	conn = sqlite3.connect(sqlite3_file)
	c = conn.cursor()

	c.execute("""CREATE TABLE words (
				word text 
				)""")
	c.execute("INSERT INTO words VALUES ('fug')")
	conn.commit()
	conn.close()

def add_word(w):
	sqlite3_file = '/Users/adriankonstantinov/Documents/Projects/groupme_bot/db/wb.db'

	conn = sqlite3.connect(sqlite3_file)
	c = conn.cursor()
	word = w

	c.execute("INSERT INTO words VALUES (?)", (word,))

	conn.commit()
	conn.close()
	print('ADDED')

def get_word():
	sqlite3_file = '/Users/adriankonstantinov/Documents/Projects/groupme_bot/db/wb.db'

	conn = sqlite3.connect(sqlite3_file)
	c = conn.cursor()

	wordlist = [x[0] for x in c.execute("SELECT * FROM words")]

	phrase = ''
	listloop = [0] * (randint(4,9))
	
	for a in listloop:
		nextword = choice(wordlist)
		phrase = phrase + nextword + ' '
		wordlist.remove(nextword)

	listloop = [0] * (randint(4,9))

	conn.commit()
	conn.close()

	return phrase

def leninc(lenlist):
	with open("len.txt", "r+") as f:
		val = int(f.read() or 0) + lenlist
		f.seek(0)
		f.truncate()
		f.write(str(val))
		return val
	
def indexinc():
	with open("inc.txt", "r+") as f:
		val = int(f.read() or 0) + 1
		f.seek(0)
		f.truncate()
		f.write(str(val))
		return val






