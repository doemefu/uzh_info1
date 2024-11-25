from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    
    index_dictionary = {}
    i = 0
    for part in dataset:
        for word in part.split(" "):
            word = word.lower()
            if word not in index_dictionary.keys():
                index_dictionary[word] = [i]
            else:
                index_dictionary[word] += [i]
        i += 1

    return index_dictionary
    # don't forget to return your resulting dictionary

# You can see the output of your function here
print(reverse_index(dataset))
