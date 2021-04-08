# Homework 3: Python
# Python Challenge #4: PyParagraph
#
# I created a Python script to assess an input paragraph for several factors.
# The script counts the words and sentences in a paragraph, as  well as the average 
# length of words (in letters) and sentences (in words).
# Make sure to run the script from the right directory for the relative path to work.

# Import modules
import os
import re
import numpy

# Open and read txt file, store in variable
importp1 = open("Resources/paragraph_1.txt","r")
paragraph = importp1.read()

# Split into words
words = re.split(" ", paragraph)

# Split into sentences
sentences = re.split("(?<=[.!?]) +", paragraph)

# Get the average letters per word 
lettercts = []
for i in range(len(words)):
    lettercts.append(int(len(words[i])))
avgcalc1 = numpy.average(lettercts)
avgletter = numpy.around(avgcalc1,1)

# Get the average words per sentence
wordcts = []
for i in range(len(sentences)):
    sent = sentences[i]
    splits = sent.split(" ")
    wordcts.append(len(splits))
avgcalc2 = numpy.average(wordcts)
avgword = numpy.around(avgcalc2,1)

# Create txt file with results
# Create path output
output_path = os.path.join("Analysis","paragraph1_analysis.txt")
with open(output_path, 'w', newline='') as txtfile:

    print(f"Paragraph Analysis",file=txtfile)
    print(f"___________________________",file=txtfile)
    print(f"Approximate Word Count: {len(words)}",file=txtfile)
    print(f"Approximate Sentence Count: {len(sentences)}",file=txtfile)
    print(f"Average Letter Count: {avgletter}",file=txtfile)
    print(f"Average Sentence Length: {avgword}",file=txtfile)

