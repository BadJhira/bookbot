def main():
    # Establish path to text file
    book_path = "books/frankenstein.txt"

    text = book_contents(book_path)
    wCount = wordCount(text)
    cCount = charCount(text)
    print(cCount)

# Reads in a file and returns a string of text
def book_contents(book_path):
    # Not exactly certain how 'with open(x) as y' works...
    # open(x) at least defaults to reading the given file (as text?)
    with open(book_path) as f:
        return f.read()
    
# Returns an int count of number of words in a string   
def wordCount(text):
    # Takes in a string, then splits it at a delimiter (whitespace here) to construct an array of strings
    words = text.split()
    return len(words)

# Constructs and returns a dict of characters from a string
def charCount(text):
    # Lowering the text first (could do this individually inside the loop)
    text = text.lower()
    # Constructing dictionary to store char/int pairs
    charDict = {}
    # For loop that checks each char against the dict, incrementing the int as it does
    for char in text:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    return charDict

# ***** MAIN *****
main()