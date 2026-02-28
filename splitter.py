class HinglishSplitter:
    def split_words(self, text):
        words=[]
        current=""

        for ch in text:
            if ch.isalpha() and ord(ch)<128:
                current+=ch
            elif '\u0900'<=ch<='\u097F':
                current+=ch
            elif ch.isdigit():
                current+=ch
            else:
                if current:
                    words.append(current)
                    current=""

                if ch.strip():
                    words.append(ch)            

        if current:
            words.append(current)   

        return words            
