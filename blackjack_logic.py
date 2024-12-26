import random

# Constants for the game
WINNING_SCORE = 21
DEALER_STAND = 17

# Global variables to manage game state
deck = []
player_hand = []
dealer_hand = []
balance = 100
bet = 0
game_over = False

def initialise_deck():
    """Initialise a shuffled deck of cards."""
    number_cards = list(range(2, 11)) * 4
    face_cards = ['J', 'Q', 'K'] * 4
    ace_card = ['A'] * 4
    deck = number_cards + face_cards + ace_card
    random.shuffle(deck)
    return deck


def deal_card(deck, hand):
    """Deal a single card to a hand."""
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)


def determine_total(hand):
    """Calculate the total value of a hand."""
    total = 0
    ace_11s = 0
    for card in hand:
        if isinstance(card, int):
            total += card
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > WINNING_SCORE:
        total -= 10
        ace_11s -= 1
    return total


def check_winner():
    """Determine the winner of the current game."""
    player_total = determine_total(player_hand)
    dealer_total = determine_total(dealer_hand)

    if player_total > WINNING_SCORE:
        return "Bust! House wins."
    elif dealer_total > WINNING_SCORE:
        return "Dealer busts! You win!"
    elif player_total > dealer_total:
        return "You win!"
    elif dealer_total > player_total:
        return "House wins!"
    else:
        return "It's a tie!"


def start_new_game(player_bet):
    """Reset the game state for a new game."""
    global deck, player_hand, dealer_hand, balance, bet, game_over

    if player_bet > balance or player_bet <= 0:
        return (
            "Invalid bet amount. Please place a valid bet.",
            str(player_hand),
            str(dealer_hand),
            "Total: --",
            "Total: --",
            f"Balance: ${balance}",
        )

    deck = initialise_deck()
    player_hand = []
    dealer_hand = []
    bet = player_bet
    game_over = False

    # Deal initial cards
    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

    dealer_display = [dealer_hand[0], "Hidden"]

    return (
        str(player_hand),
        str(dealer_display),  # Show only the first dealer card
        f"Total: {determine_total(player_hand)}",
        "Total: Hidden",
        "Game ongoing!",
        f"Balance: ${balance - bet}",  # Deduct bet temporarily
    )


def player_hit():
    """Handle the player's hit action."""
    global deck, player_hand, game_over

    if game_over:
        return (
            str(player_hand),
            str(dealer_hand),
            f"Total: {determine_total(player_hand)}",
            "Total: Hidden",
            "Game is over. Start a new game!",
            f"Balance: ${balance}",
        )

    deal_card(deck, player_hand)
    player_total = determine_total(player_hand)

    if player_total > WINNING_SCORE:
        return player_stay()  # Automatically end the game if player busts

    dealer_display = [dealer_hand[0], "Hidden"]

    return (
        str(player_hand),
        str(dealer_display),  # Keep dealer's second card hidden
        f"Total: {player_total}",
        "Total: Hidden",
        "Game ongoing!",
        f"Balance: ${balance - bet}",
    )


def player_stay():
    """Handle the player's stay action and dealer's turn."""
    global deck, dealer_hand, balance, bet, game_over

    game_over = True

    while determine_total(dealer_hand) < DEALER_STAND:
        deal_card(deck, dealer_hand)

    result = check_winner()

    if "You win" in result:
        balance += bet * 2
    elif "House wins" in result:
        balance -= bet

    return (
        str(player_hand),
        str(dealer_hand),  # Reveal full dealer hand
        f"Total: {determine_total(player_hand)}",
        f"Total: {determine_total(dealer_hand)}",
        result,
        f"Balance: ${balance}",
    )
