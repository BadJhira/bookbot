def main():
    # Establish path to text file
    book_path = "books/frankenstein.txt"

    text = book_contents(book_path)
    wCount = wordCount(text)
    cCount = charCount_cooked(charCount(text))

    print(f"--- Begin report on {book_path} ---")
    print(f"{wCount} words found in the document")
    print()
    for item in cCount:
        # VS says .isalpha isn't defined, but it still works when ran *shrug*
        if not item["char"].isalpha():
            continue
        char = item["char"]
        count = item["num"]
        print(f"The {char} character was found {count} times")
    print("--- End report ---")

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

# Necessary weird function to pass into .sort
def sort_on(dict):
    return dict["num"]

# Cooked converting the char dict into a list that can be ordered (why bother)
def charCount_cooked(dict):
    charList = []
    # Making a list of dicts makes sense, but not in this application tbh
    # I feel like writing our own sorting function for the dict would have been a better challenge
    for c in dict:
        charList.append({"char": c, "num": dict[c]})
    # The accursed .sort (reverse=True just means bigger number go first)
    charList.sort(reverse=True, key=sort_on)
    return charList

# ***** MAIN *****
main()