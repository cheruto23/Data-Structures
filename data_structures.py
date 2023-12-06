def is_balanced(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return not stack

def remove_duplicates(sequence):
    result = [element for index, element in enumerate(sequence) if element not in sequence[:index]]
    return result

import string
def word_frequency(sentence):
    clean_sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    
    words = clean_sentence.split()

    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict