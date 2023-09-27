"""Word Finder: finds random words from a dictionary."""
from random import randint
class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, path_to_file):
        "Creates a list  of words written from a file"
        self.list_of_words = self.get_words(path_to_file)
        print (f'{len(self.list_of_words)} words read')

    def get_words(self, path_to_file):
        file = open (path_to_file,'r')
        list_of_words =[]
        for line in file:
            list_of_words.append(line.replace("\n",""))  
        file.close()
        return list_of_words
    
    def random (self):
        random = randint(0, len(self.list_of_words))
        return self.list_of_words[random]

class SpecialWordFinder(WordFinder):
    
    def get_words(self, path_to_file):

        file = open (path_to_file,'r')
        list_of_words =[]
        for line in file:
            if line.strip() != "":
                list_of_words.append(line.replace("\n","").replace("#","").strip())  
        file.close()
        return list_of_words
