import json

with open("words.txt", 'r') as file:
    content = file.read()
    # To get the num of words, you need to first split the content
    word_list = content.split()
    # Then get the number words using len of the variable used to split content
    word_count = len(word_list)
    file.close()
    pass

print("In words.txt there are",(word_count),"words")