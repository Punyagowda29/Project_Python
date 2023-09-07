import random
def rps():
    user=input("whats your choice,'r' for rock,'s' for scissor,'p' for paper")
    comp=random.choice(['r','s','p'])
    if user==comp:
        return "tie"
    if win(user,comp):
        return "you won"
    return "you lost"

def win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(rps())