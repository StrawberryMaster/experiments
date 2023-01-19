import random

# Set up the deck of cards
suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = [rank + " of " + suit for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Deal the cards
player1_hand = deck[:7]
player2_hand = deck[7:14]
draw_pile = deck[14:]

# Set up the game loop
game_over = False
winner = ""
while not game_over:
    # Player 1's turn
    print("Player 1's hand:", player1_hand)
    print("Player 2's hand:", ["?"] * len(player2_hand))
    print("Draw pile:", len(draw_pile))
    ask_rank = input("Player 1, what rank do you want to ask for? ")
    if ask_rank in player2_hand:
        # Player 2 has the rank that was asked for
        print("Player 2 has the " + ask_rank + "!")
        player1_hand.append(ask_rank)
        player2_hand = [card for card in player2_hand if card != ask_rank]
    else:
        # Player 2 does not have the rank that was asked for
        print("Go fish!")
        if len(draw_pile) > 0:
            player1_hand.append(draw_pile.pop())
        else:
            game_over = True
            winner = "nobody"
    
    # Check if player 1 has won
    if len(player1_hand) == 0:
        game_over = True
        winner = "Player 1"
    
    # Player 2's turn
    if not game_over:
        print("Player 1's hand:", ["?"] * len(player1_hand))
        print("Player 2's hand:", player2_hand)
        print("Draw pile:", len(draw_pile))
        ask_rank = input("Player 2, what rank do you want to ask for? ")
        if ask_rank in player1_hand:
            # Player 1 has the rank that was asked for
            print("Player 1 has the " + ask_rank + "!")
            player2_hand.append(ask_rank)
            player1_hand = [card for card in player1_hand if card != ask_rank]
        else:
            # Player 1 does not have the rank that was asked for
            print("\nGo fish!")
            if len(draw_pile) > 0:
                player2_hand.append(draw_pile.pop())
            else:
                game_over = True
                winner = "nobody"
        
        # Check if player 2 has won
        if len(player2_hand) == 0:
            game_over = True
            winner = "Player 2"

# Print the winner
print("The winner is " + winner + "!")