"""A simple program to translate a phase into pig latin
Coded by: Rowan Jansens"""


def main():
    phrase = input('Enter a phrase: ')
    pig_latin(phrase)

def pig_latin(phrase):
    words = phrase.split()     #break the phrase up into single  words
    wc = len(words)
    for i in range(wc):     #iterate through the all the words
        vowel = first_vow(words[i])     # get the position of first vowel
        #make a the new words by cutting off the first bit and adding a sufix
        new_word = str(words[i][vowel:] + sufix(words[i], vowel))
        #print the new words
        print(str(new_word))
        
def sufix(words, vowel):
    #make sufix by adding "ay" to the letter before the fist vowel
    s = str('-' + words[0:vowel] + 'ay')
    return s   
    
def first_vow(words):
    length = len(words)     #legth of an individual word
    vow = ['a', 'e', 'i', 'o', 'u', 'y']
    #iterate through the letters untill a vowel is reached
    #then return its possition in the word
    for j in range(length):
        for k in range (6):
            if (words[j] == vow[k]):
                return j
main()
