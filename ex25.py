# str.split([sep[, maxsplit]]) return a list of words in the stirng, using sep as the delimiter string
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # split every time you see a space
    return words
    
# a string must be splitted into a list of words before the words can be sorted  
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
# list.pop([i]) remove the item at the given position in the list, and return it.  If no index is
# specified, a.pop() removes and returns the last item in the list. (The square brackets around the
# i in the medthod signature denote that the parameter is optional, not that you should type square
# brackets in that position)   
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
    
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
# The sort_sentence function could also be rewritten like this 
# if you do not want to use the break_words and sort_words functions.  
def sort_sentence_2(sentence):
    sorted_words = sorted(sentence.split())
    return sorted_words
    
    
def print_first_and_last(sentence):
    """Prints the first and las words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
sentence = "I have a cat and its name is fish"
words = break_words(sentence)
print words
sorted_words = sort_words(words)
print sorted_words
print_first_word(sorted_words)
print_first_word(words)
print_last_word(words)
print_last_word(sorted_words)
print sort_sentence(sentence)
print sorted("I have a cat and his name is fish".split())
a = "I have a cat and I love it".split()
print a