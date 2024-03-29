## Problem 1: Element Frequency
def element_frequency(lst):
    """Takes a list of elements as input and 
    returns a dictionary containing the frequency 
    of each unique element in the list."""
    frequency_dict = {}
    for i in lst:
        if i in frequency_dict.keys():
            frequency_dict[i]+= 1
        else:
            frequency_dict[i] = 1
    return frequency_dict


input_lst = list(map(int, input().split()))
element_dict = element_frequency(input_lst)
print(element_dict)



## Problem 2: Running Total
def running_total(lst):
    """Takes a list of integers as input and 
    turns a new list containing the running 
    total of the elements. The running total 
    of a list is obtained by adding up the 
    elements cumulatively from the beginning."""

    new_lst = []
    j = 0
    for i in lst:
        j += i
        new_lst.append(j)
    return new_lst


in_lst = list(map(int, input().split()))
answer = running_total(in_lst)
print(answer)



## Problem 3: Remove Duplicates from String
def remove_duplicates_from_string(input_str):
    """Takes a string as input and returns a new 
    string with duplicate characters removed, 
    maintaining the original order."""

    single_char_word = ""
    for character in input_str:
        if character not in single_char_word:
            single_char_word += character

    return single_char_word


in_word = input("Enter a word: ")
new_word = remove_duplicates_from_string(in_word)
print(new_word)



## Problem 4: Check Anagrams
def are_anagrams(word1, word2):
    """Takes two strings as input and determines 
    whether they are anagrams of each other. 
    Anagrams are words or phrases formed by rearranging 
    the letters of another word or phrase."""

    if len(word1) != len(word2):
        return False
    for letters in word1.lower():
        if letters not in word2.lower():
            return False
    return True


word_1 = input("Enter 1st word: ")
word_2 = input("Enter 2nd word: ")
anagram = are_anagrams(word_1, word_2)
print(anagram)



## Problem 5: Reverse Words in a Sentence
def reverse_words(sentence):
    """Takes a string representing a sentence as input and 
    returns a new string where the order of words is reversed 
    while maintaining the order of characters within each word."""

    new_sen = ""


print(reverse_words("Hello World"))