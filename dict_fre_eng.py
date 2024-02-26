'''
English to French translator program.
The program takes a word from the user as an input and translates it using
a dictionary data type as a vocabulary.
If the word is not in the code vocabulary, prints ({word} is not in my memory).
**The user will select the language they would like to translate to***
'''

fre_eng={"prune":"bush plum", "bonjour":"good morning", "arachide":"peanut", "mangue":"mango",
         "oule":"african locust bean", "tamarinier noir":"velvet tamarind"}
word=input("Enter the word to translate: ").lower()
lang=input("Enter the language to translate to (E)nglish or (F)rench): ").lower()

if lang=="e" and word in fre_eng:
    translation=fre_eng.get(word)
    print(f"The word '{word}' is translated as '{translation}' in English")
elif lang=="f" and word in fre_eng.values():
    for key , value in fre_eng.items():
        if value==word:
            translation=key
    print(f"The word '{word}' is translated as '{translation}' in French")          
else:
    print(f"The word '{word}' or chosen language is not in my vocabulary")
