#1/usr/env python

import sys

class day:
	def __init__(self, filename):
		self.file = []
		for line in open(filename):
			self.file.append(line.strip())

	def findWords(self, num):
		total = 0
		for line in self.file:
			if len([char for char in line if line.count(char) == num]) != 0:
				total += 1
		return total

	def findBiWords(self):
		self.biWordsCount = self.findWords(2)

	def findTriWords(self):
		self.triWordsCount = self.findWords(3)

	def getChecksum(self):
		self.findBiWords()
		self.findTriWords()
		return self.biWordsCount * self.triWordsCount

	def findCommonWords(self):
		for word1 in self.file:
			for word2 in self.file:
				if word1 == word2:
					continue
				# print(f'[{word1}] and [{word2}] share [{self.commonKeys(word1, word2)}] with {self.countDiff(word1, word2)} errors.')
				if self.countDiff(word1, word2) == 1:
					return self.commonKeys(word1, word2)
		raise ValueError('Could not find two words with only one error')

	def countDiff(self, word1, word2):
		# Counting the number of keys to see key errors
		return len(word1) - len(self.commonKeys(word1, word2))

	def commonKeys(self, word1, word2):
		# Checking to make sure both words are the same size
		if len(word1) != len(word2):
			raise IndexError(f'Both words must be the same size:\n\t{word1}\n\t{word2}')

		# Checking for each position to see if they share a key
		keys = []
		for num in range(len(word1)):
			if word1[num] == word2[num]:
				keys.append(word1[num])
		return keys


# Creating a day object to calculate puzzle output
try:
	pig = day(sys.argv[1])
except IndexError:
	pig = day(os.path.join('1', 'testInput.txt'))

# Executing commands to calculate the answer to the puzzle
pig.findBiWords()
pig.findTriWords()

# Printing out the information requested
print(f'Checksum is [{pig.getChecksum()}]')
keys = ''.join(pig.findCommonWords())
print(f'Similar keys between boxes are {keys}')