"""A simple program to translate a phrase into pig latin
Coded by: Rowan Jansens"""


def main():
    phrase = input('Enter a phrase: ')
    pig_latin(phrase)

def pig_latin(phrase):
    new_phrase = []
    words = phrase.split()     #break the phrase up into a list of single  words
    for i in range(len(words)):     #iterate through all the words in the list
        vowel = first_vow(words[i])     # get the position of first vowel
        
        #make new word by cutting off everything before the fist vowel and adding a suffix
        new_word = str(words[i][vowel:] + suffix(words[i], vowel))
        new_phrase.append(new_word)   #add new word to the "new_phrase" list
    print(' '.join(w for w in new_phrase))   #print the words in the list like a sentence
        
def suffix(words, vowel):
    #make suffix by adding "ay" to the letters before the fist vowel
    s = str('-' + words[0:vowel] + 'ay')
    return s   
    
def first_vow(words):
    vow = ['a', 'e', 'i', 'o', 'u', 'y']
    
    #iterate through the letters of the given word
    for j in range(len(words)):
        #try to match a vowel in the word
        for k in range (len(vow)):
            #if matched, return current position
            if (words[j] == vow[k]):
                return j
main()
