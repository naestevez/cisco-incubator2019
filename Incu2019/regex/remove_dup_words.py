
###################################################
# Duplicate words
# The students will have to find the duplicate words in the given text,
# and return the string without duplicates.
#
###################################################
import re

text="This is is a test test test sentence, and I am very happy happy"

def remove_duplicates(text):
    """remove duplicate words in a given text"""
    text_list_str = re.findall(r"\w+\S", text)

    for word in text_list_str:
        # loop checks every word in text_list_str after the first word for a duplicate
        for otherword in text_list_str[text_list_str.index(word) + 1:]:
            # if duplicate found, delete word
            if otherword == word:
                del text_list_str[text_list_str.index(word)]

    # joins all words with ", " and converts list into string
    text_with_no_dup = " ".join(text_list_str)
    print(text_with_no_dup)
    return text_with_no_dup

remove_duplicates(text)
