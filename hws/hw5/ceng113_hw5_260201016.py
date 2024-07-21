# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:04:35 2021

@author: fatih
"""
import random

class Gamebot:

    def __init__(self, play_hand, stack):
        self.play_hand = play_hand                  # a reference to the player's hand
        self.stack = stack                          # a reference to the stack
        self.count_deck = [['b',1],['b',1],['b',1],['b',2], # a list to count the remaining
                           ['b',2],['b',3],['b',3],['b',4], # cards in the deck
                           ['w',1],['w',1],['w',1],['w',2],
                           ['w',2],['w',3],['w',3],['w',4]]
        for card in play_hand:                      # bot has already seen the player's hand,so it knows
            self.update_count_deck(card)            # that those cards are not in the deck anymore.
        self.hand = [['!',-1],['!',-1],['!',-1]]    # bot's hand. '!' indicates unknown color,
                                                    # -1 indicates unknown value

    def get_tip(self, tip):
        self.tip = tip
        self.tip = self.tip.split(",") # converts string to list
        if self.tip[-1] == "w": # it checks the last element of the list
            for i in self.tip[0:-1]:
                self.hand[int(i)-1][0] = 'w' #and changes its location in x
        elif self.tip[-1] == "b":
            for i in self.tip[0:-1]:
                self.hand[int(i)-1][0] = 'b'
        elif self.tip[-1] == "1":
            for i in self.tip[0:-1]:
                self.hand[int(i)-1][1] = 1
        elif self.tip[-1] == "2":
            for i in self.tip[0:-1]:
                self.hand[int(i)-1][1] = 2
        elif self.tip[-1] == "3":
            for i in self.tip[0:-1]:
                self.hand[int(i)-1][1] = 3
        elif self.tip[-1] == "4":
            for i in self.tip[0:-1]:
                self.hand[int(i)-1][1] = 4
        pass

    def update_count_deck(self,card):
        self.card = card
        # input: card to be removed
        # output: none
        # card is removed from the count_deck of the bot.
        pass

    def update_hand(self,num):
        self.num = num
        self.num -= 1
        self.hand.pop(self.num) # it pops the card
        self.hand.insert(self.num,['!',-1]) # and adds blank card in place of removed card
        
        # input: num: location of the card to be removed from the bot's hand
        # output: none
        # A card is removed from the bot's hand according to the given input and a new one is appended.
        pass

    def give_tip(self):
        isheknow = False
        b = 0
        w = 0
        one = 0
        two = 0
        three = 0
        four = 0
        for i in self.play_hand:
            if i[0] == 'b':
                b += 1
            elif i[0] == 'w':
                w += 1
        for i in self.play_hand:
            if i[1] == 1:
                one += 1
            if i[1] == 2:
                two += 1
            if i[1] == 3:
                three += 1
            if i[1] == 4:
                four += 1
        # first it counts the number of blacks,whites and card number 
        if (b == 3 or w == 3) and isheknow == False: # according to the amount of these numbers it gives a tip
            isheknow = True
            if b == 3:
                tip = "1,2,3,b" 
                print("Computer gives a tip :\n" + tip) # and it prints the tip
            else:
                tip = "1,2,3,w"
                print("Computer gives a tip :\n" + tip)                        
        elif one == 3 or two == 3 or three == 3 or four == 3:
            if one == 3:
                tip = "1,2,3,1"
                print("Computer gives a tip :\n" + tip)
            elif two == 3:
                tip = "1,2,3,2"
                print("Computer gives a tip :\n" + tip)
            elif three == 3:
                tip = "1,2,3,3"
                print("Computer gives a tip :\n" + tip)
            elif four == 3 :
                tip = "1,2,3,4"
                print("Computer gives a tip :\n" + tip)
        elif one == 2 or two == 2 or three == 2 or four == 2:
            one_ = ""
            two_ = ""
            three_ = ""
            four_ = ""
            a = 1
            if one == 2:                    
                for i in self.play_hand:
                    if 1 in i:
                        w = str(a) + ","
                        one_ = one_ + w
                    a +=1
                one_ = one_ + "1"
                tip = one_
                print("Computer gives a tip :\n" + tip)
            if two == 2:
                for i in self.play_hand:
                    if 2 in i:
                        w = str(a) + ","
                        two_ = two_ + w
                    a += 1
                two_ = two_ + "2"
                tip = two_
                print("Computer gives a tip :\n" + tip)
            if three == 2:
                for i in self.play_hand:
                    if 3 in i:
                        w = str(a) + ","
                        three_ = three_ + w
                    a += 1
                three_ = three_ + "3"
                tip = three_                          
                print("Computer gives a tip :\n" + tip)
            if four  == 2 :
                for i in self.play_hand:
                    if 4 in i:
                        w = str(a) + ","
                        four_ = four_ + w
                    a += 1
                four_ = four_ + "4"
                tip = four_
                print("Computer gives a tip :\n" + tip)
        elif (b == 2 or w == 2) and isheknow == False:
            isheknow = True
            b_ = ""
            w_ = ""
            c = 1
            if b == 2:
                for i in self.play_hand:
                    if "b" in i:
                        w = str(c) + ","
                        b_ = b_ + w
                        c += 1
                b_ = b_ + "b"
                tip = b_
                print("Computer gives a tip :\n" + tip)
            elif w == 2:
                for i in self.play_hand:
                    if "w" in i:
                        w = str(c) + ","
                        w_ = w_ + w
                    c += 1
                w_ = w_ + "w"
                tip = w_
                print("Computer gives a tip :\n" + tip)
            else:
                p = random.choice(self.play_hand)
                l = 1
                for i in self.play_hand:
                    if i == p:
                        tip = str(l) + "," + str(i[1])
                        print("Computer gives a tip :\n" + tip)
                    l += 1
        pass

    def pick_stack(self):
        for card in self.hand:
            if card[0] == 'b':
                if self.stack[0] == []:
                    if card[1] == 1:
                        self.stack[0].append(card)
                        return card
                elif self.stack[0] == [['b',1]]:
                    if card[1] == 2:
                        self.stack[0].append(card)
                        return card
                elif self.stack[0] == [['b',1],['b',2]]:
                    if card[1] == 3:
                        self.stack[0].append(card)
                        return card
                elif self.stack[0] == [['b',1],['b',2],['b',3]]:
                    if  card[1] == 4:
                        self.stack[0].append(card)
                        return card
                else:
                    continue
            elif card[0] == 'w':
                if self.stack[1] == []:
                    if card[1] == 1:
                        self.stack[1].append(card)
                        return card
                elif self.stack[1] == [['w',1]]:
                    if card[1] == 2:
                        self.stack[1].append(card)
                        return card
                elif self.stack[1] == [['w',1],['w',2]]:
                    if card[1] == 3:
                        self.stack[1].append(card)
                        return card
                elif self.stack[1] == [['w',1],['w',2],['w',3]]:
                    if  card[1] == 4:
                        self.stack[1].append(card)
                        return card
                else:
                    continue
            else:
                continue
            
        # input: none
        # output: If possible, the location of the card to be placed in the stack, otherwise -1. Minimal
        # the requirement for this function is to find the card to be stacked with 100% certainty.
        # BONUS: Smarter decision-making algorithms can be implemented.
        pass

    def pick_discard(self):
        
        # input: none
        # output: The location of the card to be discarded. Minimal requirement for this function is that,
        # if possible, the bot picks the card that is already in the stack. If this is not the case,
        # the bot picks the card of which it has minimum information.
        # BONUS: Smarter decision-making algorithms can be implemented.
        pass

def shuffle(deck):
    random.shuffle(deck)
    # shuffles the deck by using 'shuffle'
    pass


def print_menu():
    print("Hit 'v' to view the status of the game.")
    print("Hit 't' to spend a tip.")
    print("Hit 's' to try and stack your card.")
    print("Hit 'd' to discard your card and earn a tip.")
    print("Hit 'h' to view this menu.")
    print("Hit 'q' to quit.")

def update_hand(hand,deck,num):
    hand.pop(int(num)-1) # it pops the card according to the given number
    if len(deck) > 0: # it checks the number of cards in the deck
        hand.append(deck[0]) # if its greater than 0, draws the top card in the deck
        del deck[0] # and removes from the deck
    else:
        print("There is no card in the deck !!!")
    
    # input: hand to be updated,current deck and the location of the card to be removed
    # output: removed card
    # This function is called when a card is played (either stacked or discarded). It removes
    # the played card from the hand. If there are any cards left in the deck, the top card
    # in the deck is drawn and appended to the hand.
    pass

def try_stack(card,stack,trash,lives):
    if card[0] == 'b': # it looks at the colors first
        if stack[0] == []: # then it checks state of stacks
            if card[1] == 1: # finally, if the card number matches, appends it to stack
                stack[0].append(card)
            else:
                trash.append(card) #if it does not match, appends it to trash
                lives -= 1
                print("trash",trash)
            return lives , stack , trash
        elif stack[0] == [['b',1]]:
            if card[1] == 2:
                stack[0].append(card)
            else:
                trash.append(card)
                lives -= 1
                print("trash",trash)
            return lives , stack , trash
        elif stack[0] == [['b',1],['b',2]]:
            if card[1] == 3:
                stack[0].append(card)
            else:
                trash.append(card)
                lives -= 1
                print("trash",trash)
            return lives , stack , trash
        elif stack[0] == [['b',1],['b',2],['b',3]]:
            if  card[1] == 4:
                stack[0].append(card)
            else:
                trash.append(card)
                lives -= 1
                print("trash",trash)
            return lives , stack , trash
    elif card[0] == 'w':
        if stack[1] == []:
            if card[1] == 1:
                stack[1].append(card)
            else:
                trash.append(card)
                lives -= 1
                print("trash",trash)
            return lives , stack , trash
        elif stack[1] == [['w',1]]:
            if card[1] == 2:
                stack[1].append(card)
            else:
                trash.append(card)
                lives -= 1
                print("trash",trash)
            return lives , stack , trash
        elif stack[1] == [['w',1],['w',2]]:
            if card[1] == 3:
                stack[1].append(card)
            else:
                trash.append(card)
                lives -= 1
                print("trash",trash)
            return lives , stack , trash
        elif stack[1] == [['w',1],['w',2],['w',3]]:
            if  card[1] == 4:
                stack[1].append(card)
            else:
                trash.append(card)
                lives -= 1
                print("Trash",trash) # and it prints the trash
            return lives , stack , trash
    pass

def discard(card,trash,tips):
    trash.append(play_hand[int(card)-1]) #it  appends the card to trash
    tips += 1 # increases the tip number by one
    return tips # return tips to use it in the menu
    print("Updated trash: \n" , trash)
    print("Number of tips \n" + str(tips))
    # then prints trash and tips
    pass

print("Welcome! Let's play!")
print_menu()
deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
        ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]
stack = [[],[]] #0 means black, 1 means white
trash = []
lives = 2
tips = 3
shuffle(deck)
# First hands are dealt.
comp_hand = deck[0:3]# TODO: it gives top 3 three card to computers hand
play_hand = deck[3:6]# TODO: it gives 3rd, 4th, 5th cards to players hand
del deck[0:6]
bot = Gamebot(play_hand,stack)  # Gamebot object is created.
turn = 0 
isheknow = False                       # 0 means player, 1 means computer. So for each game, the player starts.
while True:
    if turn == 0:
        inp = input("Your turn:")
        if inp == 'v':
            print("Computer's hand:", comp_hand)
            print("Number of tips left:", tips)
            print("Number of lives left:", lives)
            print("Current stack:")
            print("Black:", stack[0])
            print("White:", stack[1])
            print("Current trash:", trash)
        elif inp == "t":
            if tips > 0:
                turn = 1
                #same algorithm as in give_tip
                b = 0
                w = 0
                one = 0
                two = 0
                three = 0
                four = 0
                for i in comp_hand:
                    if i[0] == 'b':
                        b += 1
                    elif i[0] == 'w':
                        w += 1
                for i in comp_hand:
                    if i[1] == 1:
                        one += 1
                    if i[1] == 2:
                        two += 1
                    if i[1] == 3:
                        three += 1
                    if i[1] == 4:
                        four += 1
                # first it counts the number of blacks,whites and card numbers
                if (b == 3 or w == 3) and isheknow == False:
                    isheknow = True
                    if b == 3:
                        tip = "1,2,3,b"
                        print("Player gives a tip:\n" + tip)
                                                        
                    else:
                        tip = "1,2,3,w"
                        print("Player gives a tip:\n" + tip)                        
                    
                elif one == 3 or two == 3 or three == 3 or four == 3:
                    if one == 3:
                        tip = "1,2,3,1"
                        print("Player gives a tip:\n" + tip)
                    elif two == 3:
                        tip = "1,2,3,2"
                        print("Player gives a tip:\n" + tip)
                    elif three == 3:
                        tip = "1,2,3,3"
                        print("Player gives a tip:\n" + tip)
                    elif four == 3 :
                        tip = "1,2,3,4"
                        print("Player gives a tip:\n" + tip)

                elif one == 2 or two == 2 or three == 2 or four == 2:
                    one_ = ""
                    two_ = ""
                    three_ = ""
                    four_ = ""
                    a = 1
                    if one == 2:                    
                        for i in comp_hand:
                            if 1 in i:
                                one_ = one_ + str(a) + ","
                            a +=1
                        one_ =one_ + "1"
                        tip = one_
                        print("Player gives a tip:\n" + tip)
                    if two == 2:
                        for i in comp_hand:
                            if 2 in i:
                                two_ = two_ + str(a) + ","
                            a += 1
                        two_ = two_ + "2"
                        tip = two_
                        print("Player gives a tip:\n" + tip)
                    if three == 2:
                        for i in comp_hand:
                            if 3 in i:
                                three_ = three_ + str(a) + ","
                            a += 1
                        three_ = three_ + "3"
                        tip = three_                          
                        print("Player gives a tip:\n" + tip)
                    if four  == 2 :
                         for i in comp_hand:
                            if 4 in i:
                                four_ = four_ + str(a) + ","
                            a += 1
                         four_ = four_ + "4"
                         tip = four_
                         print("Player gives a tip:\n" + tip)
                elif (b == 2 or w == 2) and isheknow == False:
                    isheknow = True
                    b_ = ""
                    w_ = ""
                    c = 1
                    if b == 2:
                        for i in comp_hand:
                            if "b" in i:
                                b_ = b_ + str(c) + ","
                            c += 1
                        b_ = b_ + "b"
                        tip = b_
                        print("Player gives a tip:\n" + tip)
                    if w == 2:
                        for i in comp_hand:
                            if "w" in i:
                                w_ = w_ + str(c) + ","
                            c += 1
                        w_ = w_ + "w"
                        tip = w_
                        print("Player gives a tip:\n" + tip)
                else:
                    p = random.choice(comp_hand)
                    l = 1
                    for i in comp_hand:
                        if i == p:
                            tip = str(l) + "," + str(i[1])
                            print("Player gives a tip:\n" + tip)
                        l += 1
                tips -= 1
                bot.get_tip(tip)
                pass
            else:
                print("Not possible! No tips left!")
        elif inp == "s":
            turn = 1        # Switch turns.
            while True:
                card = input("Player stacks a card: \n")
                # takes the location of the card to be stacked
                if card == "1" or card == "2" or card == "3":                   
                    lives,stack,trash = try_stack(play_hand[int(card)-1],stack,trash,lives)
                    update_hand(play_hand,deck,card)
                    # if location is valid, it calls the function
                    break
                else:
                    print("Invalid choice")
                    # if not it shows an error 
                    continue
            pass
        elif inp == "d":
            turn = 1  # Switch turns.
            while True:
                num = input("Player discards a card: \n")
                # takes the location of the card to be discarded
                if num == "1" or num == "2" or num == "3":
                    tips = discard(num,trash,tips)
                    update_hand(play_hand,deck,num)
                    # if location is valid, it calls the function       
                    break
                else:
                    print("Invalid choice")
                    # if location is valid, it calls the function
                    continue
            pass
        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print("Please enter a valid choice (v,t,s,d,h,q)!")
    else:
        # A minimal strategy of the bot is given.
        # BONUS: Smarter rule sets can be implemented.
        if tips > 1  and len(play_hand)>0:
            bot.give_tip()
            # calls the function
            tips -= 1
            #reduces tips by one
            pass
        else:
            bot_hand = bot.hand                
            b_num = bot.pick_stack()
            # Check if bot can pick a card to stack.
            # If yes, update comp_hand, bot's hand and bot's count_deck and try to stack the selected card.
            # If no, make bot pick a card to discard. Update comp_hand, bot's hand and bot's count_deck
            # and discard the selected card.
            pass
        turn = 0        # Switch turns.
    score = sum([len(d) for d in stack])
    if lives==0:
        print("No lives left! Game over!")
        print("Your score is", score)
        break
    if len(comp_hand+play_hand)==0:
        print("No cards left! Game over!")
        print("Your score is", score)
        break
    if score == 8:
        print("Congratulations! You have reached the maximum score!")
        break
