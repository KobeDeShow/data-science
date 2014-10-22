import sys
import string

def word_count():
    # We are going to count the occurences of all the words that appear in the book
    # Alice in Wonderland.
    # 
    # Thus, for this exercise, you need to write a program that will tally
    # the occurences of all the words that appears in Alice in Wonderland serially.
    #
    # The text in Alice in Wonderland will be fed into this program line by line.
    # And you need to write a program that will take each line and do the following:
    # 1) Tokenize a line of text into string tokens, by white space
    #    Example: "Hello, World!" will be converted into "Hello," and "World!"
    #
    # 2) Remove all punctuations
    #    Example: "Hello," and "World!" will be converted to "Hello" and "World"
    #
    # 3) Convert all words into lowercases
    #    Example: "Hello" and "World" will be converted to "hello" and "world"
    #
    # Store the the number of times that a word appears in Alice in Wonderland
    # in the word_counts dictionary
    
    word_counts = {}

    for line in sys.stdin:
        data = line.strip().split(" ")
        #data = line.strip().split() # this doesn't include empty strings
        
        for word in data:
            #key = word.strip(string.punctuation).lower()
            key = word.translate(string.maketrans("", ""), string.punctuation).lower()
            if word_counts.has_key(key):
                word_counts[key] += 1
            else:
                word_counts[key] = 1
    
    print word_counts


if __name__ == "__main__":
    word_count()
