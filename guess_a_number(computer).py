import random
def comp_guess(x):
    low=1
    high=x
    fb=''
    while fb!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        fb=input(f"is {guess}, too high(H), too low(L) or correct (C)".lower())
        if fb=='h':
            high=guess-1
        elif fb=='l':
            low=guess+1
    print(f"you guess it right, the number was{guess}")

comp_guess(200)