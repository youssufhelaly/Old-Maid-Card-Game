# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)
#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer=[]
    other=[]
    for i in range(len(deck)):
        if i%2==0:
            dealer.append(deck[i])
        else:
            other.append(deck[i])
    return (dealer, other)


def remove_pairs(cards):
    '''
     (list of str)->list of str

     Returns a copy of list cards where all the pairs from cards are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    no_pairs=[]
    cards.sort()
    if len(cards)==1:
        return cards
    for card_index in range(len(cards)-1):
        if cards[card_index][0]==cards[card_index-1][0] and cards[card_index][0]==cards[card_index+1][0] and len(cards)!=2:
            no_pairs.append(cards[card_index])
        elif cards[card_index][0]!=cards[card_index-1][0] and cards[card_index][0]!=cards[card_index+1][0]:
            no_pairs.append(cards[card_index])
    if cards[-1][0]!=cards[-2][0]:
        no_pairs.append(cards[-1])
    char=0
    for i in range(len(no_pairs)-1):
        if char==len(no_pairs) or char==len(no_pairs)-1:
            return no_pairs
        elif no_pairs[char][0]==no_pairs[char+1][0] :
            no_pairs.pop(char)
            no_pairs.pop(char)
            char-=1
        char+=1
    random.shuffle(no_pairs)
    return no_pairs



def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    end=''
    for i in deck:
        end+=i+" "
    print( "\n"+end+"\n")
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     ans=int(input("Give me an integer between 1 and "+ str(n)+ ": "))
     while ans<1 or ans>n:
        ans=int(input("Invalid number. Please enter integer between 1 and "+str(n)+":"))
     return ans

def play_game():
    '''()->None
    This function plays the game'''
    
    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)
    dealer=tmp[0]
    human=tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")
    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
     
    while len(human)>0 and len(dealer)>0: 
        dealer=remove_pairs(dealer)
        human=remove_pairs(human)
        print("**********************************************************************")
        if len(dealer)==0:
            print("Ups. You do not have any more cards\nYou lost! I, Robot, win")
            break
        elif len(human)==0:
            print("Ups.You do not have any more cards\nCongratulations!You, Human, win")
            break
        else:
            print("Your turn.")
            print("\nYour current deck of cards is: ")
            print_deck(human)
            print("I have "+str(len(dealer))+ " cards. If 1 stands for my first card and "+ str(len(dealer))+ " for my last card, which of my cards would you like? ")
            ans=get_valid_input(len(dealer))
            if ans==1:
                print("You asked for my "+str(ans)+"st card.")
            elif ans==2:
                print("You asked for my "+str(ans)+"nd card.")
            elif ans==3:
                print("You asked for my "+str(ans)+"rd card.")
            else:
                print("You asked for my "+str(ans)+"th card.")
            print("Here it is. It is "+str(dealer[ans-1]))
            print("With "+str(dealer[ans-1])+" added, your current deck of cards is:")
            human.append(dealer[ans-1])
            dealer.pop(ans-1)
            print_deck(human)
            print("And after discarding pairs and shufing, your deck is:")
            human=remove_pairs(human)
            print_deck(human)
            wait_for_player()
        

        print("**********************************************************************")
        if len(dealer)==0:
            print("Ups. You do not have any more cards\nYou lost! I, Robot, win")
            break
        elif len(human)==0:
            print("Ups.You do not have any more cards\nCongratulations!You, Human, win")
            break
        else:
            print("My turn\n")
            card=random.randint(1,(len(human)))
            if card==1:
                print("I took your "+str(card)+"st card.")
            elif card==2:
                print("I took your "+str(card)+"nd card.")
            elif card==3:
                print("I took your "+str(card)+"rd card.")  
            else:
                print("I took your "+str(card)+"th card.")
            dealer.append(human[card-1])
            human.pop(card-1)
            wait_for_player()

    
#
# main
play_game()