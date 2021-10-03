#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def get_num_letters(text):
	number_ofLetter = 0
	text = str(text)
	
	for letter in text :
		if letter.isalnum() : 
			number_ofLetter +=1
		else : continue

	return number_ofLetter

def get_word_length_histogram(text):
	text = str(text)
	words_byLength = [0]
	letter_inWord = 0

	for letter in text :
		if letter.isalnum() :
			letter_inWord += 1
		elif ord(letter) == 45 :
			continue
		elif letter_inWord == 0 :
			continue
		else :
			list_length = len(words_byLength)
			if  list_length > letter_inWord :
				number_ofWord = int(words_byLength[letter_inWord]) + 1
				words_byLength.insert(letter_inWord, number_ofWord)
				words_byLength.pop(letter_inWord + 1)
			elif list_length == letter_inWord : 
				words_byLength.append(1)
			else: 
				while list_length < letter_inWord :
					words_byLength.append(0)
					list_length += 1
				words_byLength.append(1)
			letter_inWord = 0

	return words_byLength

def format_histogram(histogram):
	ROW_CHAR = "*" 
	result = ""
	alignment = len(str(len(histogram) - 1))
	for i, number_ofWord in enumerate(histogram) :
		if i == 0:
			continue
		else:
			result += f"{i : >{alignment}} {ROW_CHAR*number_ofWord}" + "\n"
	
	return result

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	SPACE_CHAR = " "
	result = ""
	search_byNumber = max(histogram)

	while search_byNumber != 0 :
		for i, number_ofWord in enumerate(histogram) :
			if i == 0:
				continue
			elif number_ofWord >= search_byNumber :
				result += BLOCK_CHAR
				if i == len(histogram) - 1 :
					result += "\n"
					search_byNumber -= 1
					break
				else : continue
			elif i < len(histogram) - 1 :
				result += SPACE_CHAR
			else :
				result += " \n"
				search_byNumber -= 1
				break
	result += LINE_CHAR * len(histogram)

	return result


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
