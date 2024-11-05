import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1

#This function sorts, in place, a list of Book objects by alphabetical order of their titles, using
#selection sort. The input is a list of Book objects, and then the return is nothing. It is just the
#list sorted in place
def selection_sort_books(books: list[data.Book]) -> list[data.Book]:
    for idx in range(len(books) -1):
        mindex = idx
        for x in range(idx+1, len(books)):
            if books[x].title.lower() < books[mindex].title.lower():
                mindex = x
        if mindex != idx:
            temp = books[idx]
            books[idx] = books[mindex]
            books[mindex] = temp
    return books


# Part 2

#This function takes a string and then switches the lowercase letters into uppercase, and then swaps
#uppercase letters into lowercase. The input is a string, and the output/return is a new string with
#the cases swapped
def swap_case(word: str) -> str:
    updatedWord = ""
    for character in word:
        if character.isalpha():
            if character.islower():
                updatedWord = updatedWord + character.upper()
            else:
                updatedWord = updatedWord + character.lower()
        else:
            updatedWord = updatedWord + character
    return updatedWord

# Part 3

#The function replaces all of the occurences of "old" characters with "new" characters in the input
#string. The input is a string, an old character to be replaced, and a new character to replace the
#old character with. The return is a new string just like the original, except with all of the old
#occurrences swapped with the new occurrences.
def str_translate(word: str, old: str, new: str) -> str:
    updatedWord = ""
    for character in word:
        if character.lower() == old or character.upper() == old:
            updatedWord = updatedWord + new
        else:
            updatedWord = updatedWord + character
    return updatedWord

# Part 4

#This function creates a dictionary mapping words to the amount of times that they are present in the
#string. So, it creates a dictionary mapping words to the frequency count of the input string. The
#input is a string, and the return is a dictionary with words as keys as well as their frequency counts
#as values.
def histogram(word: str) -> dict[str, int]:
    wordDict = {}
    for wrd in word.split():
        if wrd not in wordDict:
            wordDict[wrd] = 1
        else:
            wordDict[wrd] += 1
    return wordDict
