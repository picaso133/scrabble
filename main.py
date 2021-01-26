import numpy as np

def dict2array(path):
    f = open(path, "r") # get file
    return f.read().splitlines() # split string by new line


def str2hash(str):
    str2array = list(str) #  convert the str into a list
    unique, counts = np.unique(np.array(str2array), return_counts=True) # ounting values
    return dict(zip(unique, counts)) # create a dictionary of values and their counter


def hashScore(hash1, hash2):
    score = 0; # initialize accumulator
    hash1_keys = set(hash1.keys()) # get keys from hash1
    hash2_keys = set(hash2.keys()) # get keys from hash2
    interserction = hash1_keys.intersection(hash2_keys) # get keys intersection
    diff = hash2_keys - hash1_keys # get keys differentiation
    if len(diff): # if any key doesn't exist in hash means that hash doesn't match
        return 0 # set accumulator 0
    else: # all the keys exist in the hash
        for key in interserction: # parse key intersection
            if (hash1[key] >= hash2[key]): # if count keys from the hash2 are less when hash1
                score += int(hash2[key]) # increment the accumulator
            else: # too many keys
                return 0 # set accumulator 0
    return score # return accumulator

def scrabble(str):
    arr = [] # initialize an array that will contain all keys for potentials words
    max = 0 # initialize maxim value
    result = "" # initialize variable result
    words = np.array(dict2array("words2.txt")) # get the words from the dictionary
    hash = str2hash(str) # get hash for the input string

    # for minimize words parsing
    for x in hash:
        arr.append([i for i, item in enumerate(words) if x[0] in item]) # check each letter from the input string if is exist in words and append it to an array with potentials words


    potentialWords = list(set([item for sublist in arr for item in sublist])) # get the unique keys
    for h in potentialWords: # parsing every word from the dictionary
        score = hashScore(str2hash(str), str2hash(words[h])) # check score
        if max < score: # if the detected score is greater than current
            max = score # max score is set with current
            result = words[h] # set the result with the current word
            # print(f">>>F {words[h]} : {score} [{str2hash(words[h])}] ? [{str2hash(str)}]") # for debugging
    return result


if __name__ == '__main__':
    print(scrabble("rancary")) # call scrabble function
