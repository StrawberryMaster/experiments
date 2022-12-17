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

while player1_deck and player2_deck:
    # Each player reveals the top card of their deck
    player1_card = player1_deck.pop(0)
    player2_card = player2_deck.pop(0)

    # Compare the cards
    if player1_card > player2_card:
        # Player 1 wins the round and takes both cards
        player1_pile.extend([player1_card, player2_card])
    elif player2_card > player1_card:
        # Player 2 wins the round and takes both cards
        player2_pile.extend([player1_card, player2_card])
    else:
        # There is a war
        war_pile = [player1_card, player2_card]
        while player1_card == player2_card:
            # Check if either player has enough cards for a war
            if len(player1_deck) < 2 or len(player2_deck) < 2:
                print("There was a war, but one of the players ran out of cards.")
                break
            else:
                # Each player places the next card from their deck face down
                war_pile.extend([player1_deck.pop(0), player2_deck.pop(0)])

                # Each player reveals a third card
                player1_card = player1_deck.pop(0)
                player2_card = player2_deck.pop(0)

                # Compare the third cards
                if player1_card > player2_card:
                    # Player 1 wins the war and takes all the cards
                    player1_pile.extend(war_pile)
                    break
                elif player2_card > player1_card:
                    # Player 2 wins the war and takes all the cards
                    player2_pile.extend(war_pile)
                    break
                else:
                    # If the third cards are also equal, the war continues
                    war_pile.extend([player1_card, player2_card])

# Check who won the game
if player1_deck:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")

# In this example, we simulate a simple card game called "War".
# In this game, a deck of 52 cards is shuffled and dealt to two
# players. Each player then reveals the top card of their deck, and
# the player with the higher card value wins the round and takes both
# cards.
# 
# If the cards have the same value, then there is a "war", in
# which both players place the next card from their deck face down,
# and then reveal a third card. The player with the higher third card 
# wins the war and takes all the cards.
# 
# The game continues until one player runs out of cards, at which
# point the other player is declared the winner.
# NOTE: BROKEN