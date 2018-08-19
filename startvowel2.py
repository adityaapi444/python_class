s1=input("enter a string")

for each in s1:
    s2=each.lower()
    if(s2=='a'or s2=='e' or each=='i'or s2=='o' or s2=='u'):
        print("Entered string is starts with Vowel")
        break
    else:
        print("Entered string is not starts with Vowel")
        break
