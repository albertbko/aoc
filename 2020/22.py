import os
import queue # this is more for thread safe communications. no copy so does not work for part2/recursion
import time

def calculate_score(winner):
    score = 0
    while (winner.qsize() > 0):
        score += winner.qsize() * winner.get()
    return score

def calculate_score2(winner):
    score = 0
    mult = len(winner)
    for card in winner:
        score += card * mult
        mult -= 1
    return score

def part1(player1_deck, player2_deck):
    player1 = queue.Queue(maxsize = len(player1_deck)*2)
    player2 = queue.Queue(maxsize = len(player2_deck)*2)

    # assuming starting out with same number of cards
    for i in range(len(player1_deck)):
        player1.put(player1_deck[i])
        player2.put(player2_deck[i])

    while (player1.qsize() > 0 and player2.qsize() > 0):
        # play game and compare cards
        p1 = player1.get()
        p2 = player2.get()

        if (p1 > p2):
            player1.put(p1)
            player1.put(p2)
        elif (p2 > p1):
            player2.put(p2)
            player2.put(p1)

    
    if (player1.qsize() > player2.qsize()):
        winner = player1
    else:
        winner = player2

    # calculate score
    return calculate_score(winner)

def play_game(player1, player2):
    gamelog = []

    while (len(player1) > 0 and len(player2) > 0):
        p1 = player1[0]
        p2 = player2[0]

        # check for infinite game
        p3 = player1 + [99999] + player2
        if (p3 in gamelog):
            return 'player1', player1
        gamelog.append(p3)

        if p1 < len(player1) and p2 < len(player2):
            sub_winner, _ = play_game(player1[1:p1+1], player2[1:p2+1])
            if (sub_winner == 'player1'):
                player1.extend((p1,p2))
            elif (sub_winner == 'player2'):
                player2.extend((p2,p1))
        else:
            if (p1 > p2):
                player1.extend((p1,p2))
            elif (p2 > p1):
                player2.extend((p2,p1))
        del player1[0]
        del player2[0]

    if (len(player1) > len(player2)):
        winner = 'player1'
        deck = player1
    else:
        winner = 'player2'
        deck = player2
    
    return winner, deck

def part2(player1_deck, player2_deck):
    _, deck = play_game(player1_deck, player2_deck)
    return calculate_score2(deck)

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    inputfile = open(path + '\\22input.txt', 'r')
    input = inputfile.read().split('\n\n')
    player1 = input[0].split(':')
    player2 = input[1].split(':')

    player1_deck = [int(x) for x in player1[1].strip().splitlines()]
    player2_deck = [int(x) for x in player2[1].strip().splitlines()]
    
    start = time.time()
    print(f'Part1: {part1(player1_deck, player2_deck)}')
    print(f'=== Runtime %s ===' % (time.time() - start))

    start = time.time()
    print(f'Part2: {part2(player1_deck, player2_deck)}')
    print(f'=== Runtime %s ===' % (time.time() - start))

if __name__ == '__main__':
    main()