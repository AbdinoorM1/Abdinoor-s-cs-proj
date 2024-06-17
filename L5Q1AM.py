def draw_top(rank):
    print(" " + 7*"_")
    print("|" + rank + 6*" " + "|")  
# Draw the top boarder of the card as well as the rank in the top left corner
def draw_symbols(n,symbol):
    if n == 0:
        print("|" + 7*" " +"|")
    elif n == 1:
        print("|" + 3*" " + symbol + 3*" " + "|")

    elif n == 2:
        print("|" + " " + symbol + 3*" " + symbol +" " +"|")

    elif n == 3:
        print("|" + " " + symbol + " " + symbol + " " + symbol + " " + "|")
    
def draw_mid(num_outer, num_mid, symbol):
    draw_symbols(num_outer, symbol)
    draw_symbols(num_mid, symbol)
    draw_symbols(num_outer, symbol)
    

def draw_bot(rank):
    print("|" + 6*"_" + rank + "|")

def rank_input():
    rnk = input("Enter card rank (A-9): ").upper()
    if rnk == "1":
        rnk = "A"
    return rnk

def suit_input():
    suit = input("Enter suit (C,D,H,S) ").upper()
    if suit == "C":
        suit = "\u2663"
    elif suit == "D":
        suit = "\u2666"
    elif suit == "H":
        suit = "\u2665"
    elif suit == "S":
        suit = "\u2660"
    return suit
def main():
    rank = rank_input()
    symbol = suit_input()    
    if rank == "A":
        num_outer = 0
        num_mid = 1
        num_outer = 0 
    elif rank == "2":
        num_outer = 1
        num_mid = 0
        num_outer = 1
    elif rank == "3":
        num_outer = 1
        num_mid = 1
        num_outer = 1
    elif rank == "4":
        num_outer = 2
        num_mid = 0
        num_outer = 2
    elif rank == "5":
        num_outer = 2
        num_mid = 1
        num_outer = 2
    elif rank == "6":
        num_outer = 2
        num_mid = 2
        num_outer = 2
    elif rank == "7":
        num_outer = 2
        num_mid = 3
        num_outer = 2
    elif rank == "8":
        num_outer = 3
        num_mid = 2
        num_outer = 3
    elif rank == "9":
        num_outer = 3
        num_mid = 3
        num_outer = 3        
    draw_top(rank)
    draw_mid(num_outer, num_mid, symbol)
    draw_bot(rank)
main()