STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

    # Step 1 - Open to read text
def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as my_file:
        my_file = my_file.read()
        my_file = clean_text(my_file)
    print(my_file)

    # Step 2 - Remove all punctuation.
    # Step 3 - Normalize all letters to lowercase. 
    # Step 4 - Remove all "stop words" as listed above.
def clean_text(text):
    """Remove all punctuations from file"""
    text = text.replace(",", "").replace("!", "").replace(".", "").replace("--", " ")
    text = text.lower()
    for word in text:
        if word in STOP_WORDS:
            text = text.replace(word, "")

    # Step 5 - Go through file word by word, and list how often each word is used. Use a dictionary to store info. {}

        #    if word is in {} add 1
        #    if word is not in dictionary, create add 1.

        # Not sure how to work out the def below to count each word. Returns "None"
# def count_words(str):
#     counts = dictionary()
#     words = str.split()

#     for words in text:
#         if word in count:
#             counts[word] += 1
#         else:
#             counts[word] = 1

    # for each word counted, store in dictionary?
    
    # Step 6 - Print report showing how often each word is used. ****

        # "*" * (number of times each word is listed)

    return count.items




if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
