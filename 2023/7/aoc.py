def parse_data(path):
    f = open(path, "r")
    data = f.read().split("\n")
    for i in range(len(data)):
        s = data[i].split(" ")
        data[i] = [[c for c in s[0]], int(s[1])]
    return data

def get_hand_score(hand, joker=False):
    if joker and 'J' in hand:
        # Joker acts like whatever card would make the hand the strongest type possible.
        # e.g.: 2JJ4J -> 24444 -> 4 of a kind
        #       2JJ4J -> 22244 -> 5 Full house
        #       2JJ4J -> 22242 -> 4 of a kind
        #       2JJ4J -> 2AA4A -> 3 of a kind
        #       2JJ4J -> 2AA44 -> 2 pairs
        #       2JJ4J -> 2AA42 -> 1 pair
        
        # finding the card that would make the hand the strongest
        highest_score = 0
        strongest_card = 'J'
        for card in set(hand):
            if card != 'J':
                score = get_hand_score(hand + [card])
                if score > highest_score:
                    highest_score = score
                    strongest_card = card
        # replacing Js with the strongest card
        hand = [card if card != 'J' else strongest_card for card in hand]

    # 5 of a kind
    if len(set(hand)) == 1:
        return 7
    # 4 of a kind
    elif any(hand.count(card) == 4 for card in set(hand)):
        return 6
    # Full house
    elif any(hand.count(card) == 3 for card in set(hand)) and any(hand.count(card) == 2 for card in set(hand)):
        return 5
    # 3 of a kind
    elif any(hand.count(card) == 3 for card in set(hand)) and not any(hand.count(card) == 2 for card in set(hand)):
        return 4
    # 2 pairs
    elif len([card for card in set(hand) if hand.count(card) == 2]) == 2:
        return 3
    # 1 pair
    elif any(hand.count(card) == 2 for card in set(hand)):
        return 2
    # High card
    else:
        return 1


def rank_hands(hands, joker=False):
    # symbols in descending order of value
    symbols = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    symbols = symbols[:3] + symbols[4:] + [symbols[3]] if joker else symbols
    hands = sorted(hands, key=lambda x: x[2], reverse=True)
    for i in range(len(hands)):
        for j in range(i+1, len(hands)):
            if hands[i][2] == hands[j][2]:
                for k in range(len(hands[i][0])):
                    if hands[i][0][k] != hands[j][0][k]:
                        if symbols.index(hands[i][0][k]) > symbols.index(hands[j][0][k]):
                            hands[i], hands[j] = hands[j], hands[i]
                            break
                        else:
                            break
    return hands[::-1]


def task(hands, joker=False):
    for hand in hands:
        hand.append(get_hand_score(hand[0], joker))
    hands = rank_hands(hands, joker)

    total_winnings = 0
    for i in range(len(hands)):
        total_winnings += hands[i][1] * (i+1)
    return total_winnings



if __name__ == "__main__":
    print(task(parse_data("input.txt")))
    print(task(parse_data("input.txt"), joker=True))