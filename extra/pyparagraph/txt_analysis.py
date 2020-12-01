import os
import csv
import re

#setting empty list variables
whole_text = []
split_into_sentences = []
letter_count = 0
words_in_sentence = []
split_into_words = []
total_sentence_word_count = 0

#path for csv file
file = "raw_data/paragraph_3.txt"
#opening csv file w/ reader
with open(file, 'r') as text:
    lines = text.read()

    #splitting text into words
    whole_text = lines.split(" ")

    #counting the number of words (also denominator in avg letter count)
    word_count = len(whole_text)

    #splitting into sentences using re, splitting with common sentence enders
    split_into_sentences = re.split("(?<=[.!?]) +", lines)

    #counting number of sentences (also denominator in avg sentence length)
    sentence_count = len(split_into_sentences)

    #for loop to find number of letters, save them to a variable
    for word in lines:
        char_in_word = len(word)
        letter_count = char_in_word + letter_count

    #for loop for counting words in each sentence, saving them to a variable
    for _sentence in split_into_sentences:
        split_into_words = _sentence.split(" ")
        split_into_words_count = len(split_into_words)
        total_sentence_word_count = split_into_words_count + total_sentence_word_count

#calculating avg letters and avg sentences and rounding them
average_letters = round((letter_count/word_count), 2)
average_sentences = round((total_sentence_word_count/sentence_count), 2)

#printing the variables to the terminal
print("                          ")
print(f"Approximate Word Count: {word_count} words")
print(f"Approximate Sentence Count: {sentence_count} sentences")
print(f"Average Letter Count: {average_letters} letters in a word")
print(f"Average Sentence Length: {average_sentences} words in a sentence")
print("                          ")
