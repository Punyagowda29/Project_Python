import random
def guess(x):
    random_num=random.randint(1,x)
    guess=0
    while guess!=random_num:
        guess = int(input(f"guess a number between 1 and {x}"))
        if guess<random_num:
            print("too low")
        elif guess>random_num:
            print("too high")
    print(f"guess right the number was {random_num}")

guess(15)