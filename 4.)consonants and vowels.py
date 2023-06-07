s=input("Enter a string: ").lower()
list=["a","e","i","o","u"]
n=len(s)
v=0
for i in range(0,n):
    if(s[i] in list):
        v+=1
print("Count of vowels: ",v)
print("Count of consonants: ",n-v)