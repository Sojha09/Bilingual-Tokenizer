class Vocabulary:

    def __init__(self):
        self.word2id={}
        self.id2word={}
        self.next_id=1

        self.unk_token="<UNK>"
        self.word2id[self.unk_token]=self.next_id
        self.id2word[self.next_id]=self.unk_token
        self.next_id +=1

    def add_words(self,word):
        if word not in self.word2id:
            self.word2id[word]=self.next_id
            self.id2word[self.next_id]=word
            self.next_id+=1    

    def build(self,words):
        for w in words:
            self.add_words(w)

    def encode_word(self, word):
        if word in self.word2id:
            return [self.word2id[word]]

        ids = []
        for ch in word:
            if ch not in self.word2id:
                self.add_words(ch)
            ids.append(self.word2id[ch])

        return ids
                

    def encode(self, words):
        encoded = []
        for w in words:
            encoded.extend(self.encode_word(w))
        return encoded
    def decode(self,ids):
        return [self.id2word.get(i,"<UNK>") for i in ids]        
