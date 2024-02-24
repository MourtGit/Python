'''This program will ask for a word and reverses the word.
Displays on the screen: Your word is: word, and the reverse is: drow.
Leverage methods: split, join, reverse'''

word = input("Enter the word to be reversed: ")
print(f"Your word is: {word}, and the reverse is {''.join(reversed(word))}")






'''
reverse=reversed(word) # reverses the word and holds items into memory (yield iterable items)
reverse_list=list(reverse) # converts the reversed items (characters) to a list
reversed_word = ''.join(reverse_list) # joins the elements of the list, separating them 
# with empty string (no separator)
print(reverse_list) # for test, to see the list in reversed order
print(f"Your word is: {word}, and the reverse is: {reversed_word}.")
'''

'''
# Alternate method
word=input("Enter a word: ")
print("The reverse is: ", word[::-1])
'''