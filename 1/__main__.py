#!/bin/env python

import sys, os

class FrequencyCalculator:
	def __init__(self, filename):
		self.changes = []
		for line in open(filename):
			self.changes.append(int(line))

	def calculateTotalFrequency(self):
		self.totalFrequency = 0
		for change in self.changes:
			self.totalFrequency += change

	def getTotalFrequency(self):
		self.calculateTotalFrequency()
		return self.totalFrequency


	def calculateFirstDoubleFrequency(self):
		self.doubleFrequency = None
		frequency =            0
		counter =              0
		frequencies =          []

		while self.doubleFrequency is None:
			if frequency in frequencies:
				self.doubleFrequency = frequency
			else:
				pos = counter % len(self.changes)
				change = self.changes[pos]
				frequencies.append(frequency)
				frequency += change

			counter += 1

	def getFirstDoubleFrequency(self):
		self.calculateFirstDoubleFrequency()
		return self.doubleFrequency

try:
	fc = FrequencyCalculator(sys.argv[1])
except IndexError:
	fc = FrequencyCalculator(os.path.join('1', 'input.txt'))
print(f'The total frequency is [{fc.getTotalFrequency()}]')
print(f'The first double frequency is [{fc.getFirstDoubleFrequency()}]')
