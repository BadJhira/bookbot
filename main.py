def main():
    book_path = "books/frankenstein.txt"
    text = book_contents(book_path)
    count = wordCount(text)
    print(f"{count} words found in text.")

def book_contents(book_path):
    with open(book_path) as f:
        return f.read()
    
def wordCount(text):
    words = text.split()
    return len(words)

def charCount(text):
    return None

main()