from tokenizer import HindiEnglishTokenizer

tokenizer=HindiEnglishTokenizer()

data=""" kal meri class nahi hai 
        tum assignment submit karo
        मुझे"""

tokenizer.fit(data)

while True:
    text=input("Enter Sentence:")
    encoded=tokenizer.encode(text)
    print("Encoded:",encoded)

    decoded=tokenizer.decode(encoded)
    print("Decoded:",decoded)
