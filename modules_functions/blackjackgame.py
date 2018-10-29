import tkinter
import random
from pathlib import Path

# Get card folder for Windows
card_folder = Path("C:/Users/Tim/IdeaProjects/Modules_Functions/cards")


# Import card images
def import_cards(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    # Retrieve cards for each suit
    for suit in suits:
        # Cards 1-10
        for card in range(1, 11):
            name = card_folder / "{}_{}.png".format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        # Face cards
        for card in face_cards:
            name = card_folder / "{}_{}.png".format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def score_hand(hand):
    # Calculate score of cards in list
    # Only one ace has value 11, reduces to 1 if hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score == 21:
        result_text.set("21! Player Wins!")
    if player_score > 21:
        result_text.set("Dealer Wins!")
    # Old way of dealing hand below, new implementation above
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if bust, check if there is ace and subtract 10
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer Wins")


def new_game():
    # Function to create new game
    # Gets global variables
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    global deck
    # Destroys frames
    player_card_frame.destroy()
    dealer_card_frame.destroy()
    # Zeros hands
    dealer_hand = []
    player_hand = []
    # Resets result
    result_text.set("")
    # Remake frame
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="ew")
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, rowspan=2, sticky="ew")
    # Reset deck
    deck = list(cards)
    random.shuffle(deck)
    # Re-deal beginning cards
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


mainWindow = tkinter.Tk()

# Set up screen and frames for dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")

# Result of game
result_text = tkinter.StringVar()
status_label = tkinter.Label(mainWindow, textvariable=result_text)
status_label.grid(row=0, column=0, columnspan=3, sticky="nesw")

# Frame for cards
card_frame = tkinter.Frame(mainWindow, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)
card_frame["padx"] = 20

# Frame and score for dealer
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="ew")

# Frame and score for player
player_score_label = tkinter.IntVar()
# Taken care of in function above but left as notes
# player_score = 0
# player_ace = False
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, rowspan=2, sticky="ew")

# Buttons to deal cards
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0, sticky="e")
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1, sticky="w")
new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2, sticky="ew")

# Load cards
cards = []
import_cards(cards)
print(cards)

new_game()

# Code below made redundant by new_game function
# # Create deck and shuffle
# deck = list(cards)
# random.shuffle(deck)
#
# # Create hands
# dealer_hand = []
# player_hand = []
#
# deal_player()
# dealer_hand.append(deal_card(dealer_card_frame))
# dealer_score_label.set(score_hand(dealer_hand))
# deal_player()

mainWindow.mainloop()
