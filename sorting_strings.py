def sort(word):
    new_word=word.split() # to split the sentence in to words 
    return sorted(new_word)   # to sort the the words according to ascii value
     
   
word=input(" ")
print(sort(word))

