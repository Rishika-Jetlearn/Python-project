alpha={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
pangram=input("Enter your text:").lower()
empty=[]
for a in pangram:
    if a.isalpha():
        empty.append(a)
if alpha == set(empty):
    print("It is a pangram")
    
else:
    print("This is not a pangram")
