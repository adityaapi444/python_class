sen=input("enter a sentence")
l=sen.split()
count=0
stop_word=['a', 'as', 'the', 'is', 'of', 'it', 'in', 'into', 'to', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was']
for each in l:
    if each in stop_word:
        count+=1
print("stop words are ",count)
