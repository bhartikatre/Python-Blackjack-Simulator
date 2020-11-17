from Blackjack_sim import *
def main():
#   '''main function for simulating blackjack'''
    win = loose = draw = simulations  = 0 
    playon = play()
    if playon == 1:
        win =+ 1
    if playon == -1:
        loose =+ 1
    if playon == 0:
        draw =+ 1
    simulations = +1
    go = input('Do you want to play again Y/N: ').upper()      
    if go =='Y':      
        while go =='Y': 
            playon = play()
            if playon == 1:
                win = win + 1            
            if playon == -1:
                loose = loose + 1
            if playon == 0:
                draw = draw + 1
            simulations =  simulations + 1
            go = input('Do you want to play again Y/N: ').upper() 
    print('----------------------------------------------------------')    
    print('Totals Summary :')
    print('No of time simulator ran   -' ,  simulations)
    print('No of times the player won - ', win)
    print('No of times the dealer won  -' , loose)
    print('No of times it was a draw  - ', draw)
    print('----------------------------------------------------------')    
main()