txt=str(input('Enter the word: '))
vowels="aeiouAEIOU"

count=0
for char in txt:
    if char in vowels:
        count+=1
print("The vowel count is: ",count)