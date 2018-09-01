sen=input("enter a sentence")
word=(input("enter the word which u want to count")).lower()
l=(sen.lower()).split()
print(word,":",l.count(word)/len(l))
