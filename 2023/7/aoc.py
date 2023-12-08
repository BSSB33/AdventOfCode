def parse_data(path):
    f = open(path, "r")
    data = f.read().split("\n")
    for i in range(len(data)):
        s = data[i].split(" ")
        data[i] = [[c for c in s[0]], int(s[1])]
    return data

def get_hand_score(hand):
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
    elif any(hand.count(card) == 3 for card in set(hand)) and len(set(hand)) == 3:
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


def rank_hands(hands):
    # symbols in descending order of value
    symbols = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
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


def task1(hands):
    for hand in hands:
        hand.append(get_hand_score(hand[0]))
    hands = rank_hands(hands)

    total_winnings = 0
    for i in range(len(hands)):
        total_winnings += hands[i][1] * (i+1)
    return total_winnings


if __name__ == "__main__":
    data = parse_data("input.txt")
    #print(data)
    print(task1(data))
    #print(task2(data))