import random

dice = [1,2,3,4,5,6]
dice_score = [1,5,15,-15,-5,-1]


def play():
    score_A = 0
    score_B = 0
    round = 1
    while score_A < 100 and score_B < 100:
        print('Round:',round)
        if round % 2 == 1:
            roll = random.choice(dice)
            print("A's roll:",roll)
            print("A's score:",score_A)
            score_A += dice_score[roll-1]
            print("A's new score:",score_A)
        else:
            roll = random.choice(dice)
            print("B's roll:",roll)
            print("B's score:",score_B)
            score_B += dice_score[roll-1]
            print("B's new score:",score_B)
        print()
        round += 1
    if score_A > score_B:
        print(f'A won with {score_A} points in {round-1} rounds')
    elif score_A < score_B:
        print(f'B won with {score_B} points in {round-1} rounds')          


play()
