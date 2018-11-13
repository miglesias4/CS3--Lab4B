# -*- coding: utf-8 -*-
"""
Created and modified by: Matthew Iglesias
80591632
Diego Aguirre 
T.A. Anitha Nath
"""

from HashTable import ChainingHashTable

##Reads the file words.txt and inserts into HashTable by chaining
def file_to_table():
    ##keys = []
    english_words = ChainingHashTable()
    with open("words.txt") as f:
        for words in f:
            english_words.insert(words.rstrip('\n'))
    return english_words

def print_anagrams(word,english_words,prefix =""):
    if len(word) <= 1:
        str = prefix + word
        #print(str, english_words.search(str))
        if english_words.search(str):
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] ##letters before cur
            after = word[i + 1:] ##letters after cur
            if cur not in before:
                print_anagrams(before + after,english_words,prefix + cur)
                
def count_anagrams(word,english_words,prefix =""):
    count = 0
    if len(word) <= 1:
        str = prefix + word
        if english_words.search(str):
            count += 1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] ##letters before cur
            after = word[i + 1:] ##letters after cur
            if cur not in before:
                count += count_anagrams(before + after,english_words,prefix + cur)
    return count


##write a method to determine the average number of comparisons
##required to perform a successful retrieve operation
def avg_comparisons(self):
    count = 0
    for i in self.table:
        count += len(self.table) // 2
    return count

def main():  
    print('-----Hash Table-----')    
    chaining = file_to_table()
    #print(chaining)
    print("Your choice word is: ",chaining.search("lobby"))
    load_fact = ChainingHashTable.get_load_factor(chaining)
    print('Load Factor: ',load_fact)
    print_anagrams("lobby", chaining) ##Prints the anagrams associated with the word
    print("Number of anagrams asscciated: ",count_anagrams("lobby",chaining)) ##Prints the number of anagrams from word
    print('Average Comparisons: ' , avg_comparisons)
main()