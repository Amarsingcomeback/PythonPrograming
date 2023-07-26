# Python if-else statements using membership operators (in, not in)
word = str(input("enter word : "))
latter = str(input("enter one latter : "))

if latter in word:
    print("sure your latter i find it")
elif latter not in word:
    print("ohh your latter i can't find")
else:
    print("sorry")