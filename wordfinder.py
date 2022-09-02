"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    def __init__(self, file):
        """Reads file and reports the number of words read"""

        open_file = open(file)
        self.words = self.read_file(open_file)
        print(f"{len(self.words)} words read")

    def read_file(self, open_file):
        """Turns read file into list of words"""
        return [w.strip() for w in open_file]
    
    
    def random(self):
        """Returns random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, open_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in open_file
                if w.strip() and not w.startswith("#")]
            
