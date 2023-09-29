import random
words=['hello','engineering','science','computer']
word=random.choice(words)
print("guess a character")
turns=12
guesses=''
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("you win")
        print("correct word",word)
        break
    print()
    guess=input("enter character")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("wrong")
        print("you have",+turns,'left')
        if turns==0:
            print("you loss")
