'''This code reverses your first name and prints it in a list without using slicing.'''

first_name = "smith"
reversed_name = []

'''This starts at last index, goes backward or decrement by 1,
that's what -1 means, and stops before -1 which is 0'''
for char_index in range(len(first_name) - 1, -1, -1): 
    reversed_name.append(first_name[char_index])
reversed_straight=''.join(reversed_name)
print(reversed_name)
print(reversed_straight)
