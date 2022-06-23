def is_vowel(char):
   vowels = ['a', 'e', 'i', 'o', 'u']
   return char in vowels

print(is_vowel('c'))
print(is_vowel('e'))     

i = 0
x = 0
while i < 4:
    x+=i
    i+=1
print(x)