""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5

#Q1

def lines_from_file(path):
    stream_paragraph = open(path)
    assert readable(stream_paragraph), 'File must be readable'
    stream_list = readlines(stream_paragraph)
    for index in range(len(stream_list)):
        stream_list[index] = strip(stream_list[index], '\n')
        stream_list[index] = strip(stream_list[index])
    #print(stream_list[0])
    return stream_list

def new_sample(path, i):
    #print(lines_from_file(path)[i])
    return lines_from_file(path)[i]



#Q2

def analyze(sample_paragraph, typed_string, start_time, end_time):

    def wpm(typed_string, start_time, end_time):
        typed_chars = []
        for chars in typed_string:
            typed_chars.append(chars)
        length_chars = len(typed_chars)
        num_words = length_chars / 5
        time_diff = (end_time - start_time) / 60
        return (num_words / time_diff)

    def accur(sample_paragraph, typed_string):
        typed_words = split(typed_string)
        sample_words = split(sample_paragraph)
        min_words = min(len(typed_words), len(sample_words))
        if min_words == 0:
            return 0.0
        typed_words = typed_words[0:min_words]
        sample_words = sample_words[0:min_words]
        count = 0
        for index in range(min_words):
            #print(typed_words[index] + ' ' + sample_words[index])
            if typed_words[index] == sample_words[index]:
                count += 1
        return (count/min_words) * 100

    return [wpm(typed_string, start_time, end_time), accur(sample_paragraph, typed_string)]




#Q3



def pig_latin(given_word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    sample_word = list(given_word)

    checker = 0
    for chars in sample_word:
        if chars in vowel:
            checker += 1

    if sample_word[0] in vowel:
        word = sample_word + ['way']
    elif checker == 0:
        word = sample_word + ['ay']
    else:
        i = 0
        while sample_word[i] not in vowel:
            i += 1
        cons_clust = sample_word[0:i]
        word = sample_word[i:] + cons_clust + ['ay']
    j = 0
    pig_word = ''
    while j < len(word):
        pig_word = pig_word + word[j]
        j += 1
    return pig_word








#Q4

def autocorrect(user_input, words_list, score_function):
    d = {}
    point = 0
    for word in words_list:
        point = score_function(user_input,word)
        d[word] = point
    if user_input in words_list:
        return user_input
    else:
        return min(d, key = lambda x: score_function(user_input, x))




#Q5-
def swap_score(word1, word2):
    min_len = min(len(word1), len(word2))
    word1 = word1[:min_len]
    word2 = word2[:min_len]
    count = 0
    index = 0
    while index != min_len:
        if word1[index] != word2[index]:
            count += 1
        index += 1
    return count




# END Q1-5

# Question 6
def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    w = len(word1)
    h = len(word2)
    Matrix = [[-1 for x in range(h)] for y in range(w)]

    def computeDistance(word1, index1, word2, index2, Matrix):
        if (index1 < 0):
            return (index2 + 1)
        elif (index2 < 0):
            return (index1 + 1)

        if(Matrix[index1][index2] == -1):
            if(word1[index1] == word2[index2]):
                Matrix[index1][index2] = computeDistance(word1, index1 - 1, word2, index2 - 1, Matrix)
            else:
                substitute_char = computeDistance(word1, index1 - 1, word2, index2 - 1, Matrix)
                remove_char = computeDistance(word1, index1, word2, index2 - 1, Matrix)
                add_char = computeDistance(word1, index1 - 1, word2, index2, Matrix)
                Matrix[index1][index2] = (min(substitute_char, min(add_char, remove_char)) + 1)
        return Matrix[index1][index2]
    return computeDistance(word1, len(word1) - 1, word2, len(word2) - 1, Matrix)





KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8

def score_function_accurate(word1, word2):
     w = len(word1)
     h = len(word2)
     Matrix = [[-1 for x in range(h)] for y in range(w)]
     def computeDistance(word1, index1, word2, index2, Matrix):
         if (index1 < 0):
             return (index2 + 1)
         elif (index2 < 0):
             return (index1 + 1)

         if(Matrix[index1][index2] == -1):
             if(word1[index1] == word2[index2]):
                 Matrix[index1][index2] = computeDistance(word1, index1 - 1, word2, index2 - 1, Matrix)
             else:
                 substitute_char = computeDistance(word1, index1 - 1, word2, index2 - 1, Matrix)
                 remove_char = computeDistance(word1, index1, word2, index2 - 1, Matrix)
                 add_char = computeDistance(word1, index1 - 1, word2, index2, Matrix)
                 (min(substitute_char, min(add_char, remove_char)) + 1)
                 if substitute_char < add_char and substitute_char < remove_char:
                     Matrix[index1][index2] = KEY_DISTANCES[word1[index1], word2[index2]] + substitute_char
                 elif add_char > remove_char:
                     Matrix[index1][index2] = remove_char + 1
                 else:
                     Matrix[index1][index2] = add_char + 1
         return Matrix[index1][index2]
     return computeDistance(word1, len(word1) - 1, word2, len(word2) - 1, Matrix)

#Q8
def memoize(f):
    memory = {}
    def inner(word1, word2):
        if word1+word2 not in memory:
            memory[word1+word2] = f(word1, word2)
        return memory[word1+word2]
    return inner
@memoize
def score_function_final(word1, word2):
     return score_function_accurate(word1, word2)




# END Q7-8
