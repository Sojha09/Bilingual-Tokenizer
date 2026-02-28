from normalizer import normalize
from splitter import HinglishSplitter
from vocabulary import Vocabulary

class HindiEnglishTokenizer:

    def __init__(self):
        self.splitter=HinglishSplitter()
        self.vocab=Vocabulary()

    def fit(self,text):
        text=normalize(text)
        words=self.splitter.split_words(text)
        self.vocab.build(words)

    def encode(self,text):
        text=normalize(text)
        words=self.splitter.split_words(text)
        return self.vocab.encode(words)
    def decode(self, ids):
        return " ".join(self.vocab.decode(ids))        
