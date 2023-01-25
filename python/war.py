import random

# Create a deck of cards
deck = [i for i in range(2, 15)] * 4

# Shuffle the deck
random.shuffle(deck)

# Deal the cards to the players
player1_deck = deck[:26]
player2_deck = deck[26:]

# Initialize the piles for each player
player1_pile = []
player2_pile = []

# Initialize the round number and a variable to check if the game is over
round_number = 1
no_more_cards = False

# Prints game information
print("A random deck of cards was created, shuffled, and then dealt to two players.")
print("Both decks have 26 cards. The cards will not be shown.")

# Let the game begin!
while player1_deck and player2_deck:
    # Each player reveals the top card of their deck
    player1_card = player1_deck.pop()
    player2_card = player2_deck.pop()

    # Print the round number and a line of dashes to separate the rounds
    print("\nRound", round_number)
    print ("-" * 50)

    round_number += 1

    print("Player 1 plays", player1_card)
    print("Player 2 plays", player2_card)

    # Compare the cards
    if player1_card > player2_card:
        # Player 1 wins the round and takes both cards
        player1_pile += [player1_card, player2_card]
        if len(player2_deck) > 0:
            player2_deck.pop()
        print("Player 1 wins the round and takes", player2_card, "while keeping", player1_card)
        print("\nPlayer 1 now has", len(player1_deck), "cards. Player 2 goes down to", len(player2_deck), "cards.")
    elif player2_card > player1_card:
        # Player 2 wins the round and takes both cards
        player2_pile += [player1_card, player2_card]
        if len(player1_deck) > 0:
            player1_deck.pop()
        print("Player 2 wins the round and takes", player1_card, "while keeping", player2_card)
        print("\nPlayer 2 now has", len(player2_deck), "cards. Player 1 goes down to", len(player1_deck), "cards.")
    else:
        # There is a war
        war_pile = [player1_card, player2_card]
        print("Both players play", player1_card, "and there is a war!")
        print("\nA separate pile of cards is created for the war. Its cards will not be shown.")
        while player1_card == player2_card:
            # Check if either player has enough cards for a war
            if min(len(player1_deck), len(player2_deck)) < 2:
                print("\nThere was a war, but one of the players does not have enough cards (2) to continue.")
                print("As a result, the game is over. In this case, the player with the most cards wins.")
                if len(player1_deck) > len(player2_deck):
                    print("\nPlayer 1 wins the game with", len(player1_deck), "cards!")
                elif len(player2_deck) > len(player1_deck):
                    print("\nPlayer 2 wins the game with", len(player2_deck), "cards!")
                else:
                    print("\nThe game tied. This message should never appear.")                    
                no_more_cards = True
                break
            else:
                # Each player places the next card from their deck face down
                war_pile += [player1_deck.pop(), player2_deck.pop()]

                # Each player reveals a third card
                player1_card = player1_deck.pop()
                player2_card = player2_deck.pop()

                # Print the round number and a line of dashes to separate the rounds
                print("\nRound", round_number, "(War Round)")
                print ("-" * 50)
                
                round_number += 1
                print("Player 1 plays", player1_card)
                print("Player 2 plays", player2_card)

                # Compare the third cards
                if player1_card > player2_card:
                    # Player 1 wins the war and takes all the cards
                    player1_pile += war_pile
                    print("Player 1 wins the war and takes the war pile, with", len(war_pile), "cards.")
                    break
                elif player2_card > player1_card:
                    # Player 2 wins the war and takes all the cards
                    print("Player 2 wins the war and takes the war pile, with", len(war_pile), "cards.")
                    player2_pile += war_pile
                    break
                else:
                    # If the third cards are also equal, the war continues
                    war_pile += [player1_card, player2_card]
                    print("Both players play", player1_card, "and there is another war!")

# Check who won the game
if no_more_cards == False:
    if len(player1_deck) > len(player2_deck):
        print("\nWith", len(player1_deck), "card(s) left, Player 1 wins the game!")
    elif len(player2_deck) > len(player1_deck):
        print("\nWith", len(player2_deck), "card(s) left, Player 2 wins the game!")
    else:
        print("\nThe game tied. This message should never appear.")

# In this example, we simulate a simple card game called "War".
# In this game, a deck of 52 cards is shuffled and dealt to two
# players. Each player then reveals the top card of their deck, and
# the player with the higher card value wins the round and takes both
# cards.
# 
# If the cards have the same value, then there is a "war", in
# which both players place the next card from their deck face down,
# and then reveal a third card. The player with the higher third card 
# wins the war and takes all the cards from the war pile.
# 
# The game continues until one player runs out of cards, at which
# point the other player is declared the winner.