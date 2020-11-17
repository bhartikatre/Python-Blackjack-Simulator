##########################################################################################################################    
# This Simulator is a cutdown version of BLACKJACK .
# Only one player and the dealer.Player always takes his turn first.
# Player auto hits once when sum is less than 17 and than can hit multiple times(based on choice)
# once sum of his hands is more than 17 he is made to stand or either he opts stand option
# Once user stands, the dealer can hit multiple times till the sum of their hand is less than 17
##########################################################################################################################    
import random
import os
##########################################################################################################################    
# Function play():This function implements all rules for this cutdown blackjack 
# Takes 4 deck of cards to start shuffle & distributing cards one each to player(first) than dealer
# Function hand_calc finds aum of hand 
# decides win,loose or draw based on sum .21 is blackjack.
##########################################################################################################################    
def play():    
    deck_cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
         ] * 4 
    random.shuffle(deck_cards)
    player_cards = []
    dealer_cards = []
    player_cards.append(deck_cards.pop())
    dealer_cards.append(deck_cards.pop())
    player_cards.append(deck_cards.pop())
    dealer_cards.append(deck_cards.pop())
#############################################################################################################################
# Function hand_calc : Implements logic to add sum of hand and decide value 
# of an ace in the hand .An ace can be worth 1 or 11 depending on sum
#################################################################################################################################
    def hand_calc(hand):
        
        sum=0 
        ace=[card for card in hand if card == 'A']
        not_ace=[card for card in hand if card != 'A']     
        for card in not_ace:
            if card in 'JQK':
                sum += 10
            else:    
                sum += int(card)           
        for card in ace:
            if sum <= 10:
                sum += 11
            else:
                sum += 1    
        return sum
    user_standing = 'false'
    
    while True :        
        score_player = hand_calc(player_cards)
        score_dealer = hand_calc(dealer_cards)       
        os.system('cls' if os.name == 'nt' else 'clear')        
        print('----------------------------------------------------------')
        print('Blackjack Simulator !!!  ')
        print('----------------------------------------------------------')
        print('Dealer cards               :  [{}][?]  '.format(dealer_cards[0]))
        print('Your cards   &   (sum)     :  [{}]   ({})'.format(']['.join(player_cards),score_player))
        print('----------------------------------------------------------')    
        if score_player == 21 :
            print ('Blackjack you win !!!')
            return 1             
        if score_dealer == 21 :
                print ('Dealer hits Blackjack, you loose...')
                print('Dealer cards  (total)     : [{}] ({})'.format(']['.join(dealer_cards),score_dealer))
                return -1         
        if score_player < 17:
                print('You will auto hit once if sum is less than 17')
                player_cards.append(deck_cards.pop())
                score_player = hand_calc(player_cards)
                print('Your cards after auto hit (sum) : [{}]  ({})'.format(']['.join(player_cards),score_player))       
        if score_player > 21:
            print('You busted! and you loose...')
            return -1
        
        def recall_choice():
            print('')    
            print('What would you like to do now? sum is       : ',score_player)
            print('[1] for HIT   : ')
            print('[2] for STAND : ')
            print('Invalid option will make you stand')
        
        if score_player <= 17:
            while score_player <= 17 :
                recall_choice()
                option = input('You choose : ' ) 
                if option == '1':
                    player_cards.append(deck_cards.pop())
                    score_player = hand_calc(player_cards)
                    print ('Your cards now (Total) : [{}]  ({})'.format(']['.join(player_cards),score_player))             
                else: 
                    break
        if score_player > 21:
            print(' ')
            print('You busted! and you loose..')
            return -1
        if score_player > 17 :
            print ('Please stand as sum is more than or equal 17') 
                                            
# once user stands gives chance to the dealer and result                      
        user_standing = 'true'               
        if user_standing :
            if score_dealer < 17 :
                while hand_calc(dealer_cards) <= 17:
                    dealer_cards.append(deck_cards.pop())  
                    score_dealer = hand_calc(dealer_cards)     
            print ('')                    
            print('Dealer cards  (total)     : [{}] ({})'.format(']['.join(dealer_cards),score_dealer))
            if score_dealer > 21:
                print(' ')
                print('Dealer bursted and you win!!!')
                return 1              
            elif score_player == score_dealer:
                print(' ')
                print('Its a draw or push!')
                return 0                
            elif score_player > score_dealer:
                print(' ')
                print('You win !! Dealer looses : Dealer score',score_dealer)
                return 1            
            else:
                print(' ')
                print('You loose as dealer score is more than your score..')
                return -1