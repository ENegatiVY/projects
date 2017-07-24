class WordFrequency:
    word = ''
    frequency = 0

    def __init__(self, str):
        self.word = str
        self.frequency = 1

    def __eq__(self, other):
        return self.word == other.word
