import random


def roll():
    min_value=1
    max_value=6
    roll= random.randint(min_value, max_value)

    return roll

while True:
    players= input("ENTER THE NO OF PLAYERS IN BETWEEN (2-4):   ")
    if players.isdigit():
        players= int(players)
        if 2<= players <=4:
            break
        else:
            print("PLAYERS MUST BE IN BETWEEN 2-4")
    else:
        print("INVALID , PLEASE TRY AGAIN!!")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:

    for player_idx in range(players):
        print("\nplayer", player_idx + 1, "TURN HAS JUST STARTED!")
        print("YOUR TOTAL SCORE IS: ",players_scores[player_idx], "\n")

        current_score = 0
        while True:

            should_roll = input("WOULD YOU LIKE TO ROLL THE DICE\n\nTHEN PRESS (Y)")
            if should_roll.lower() !="y":
                break

            value = roll()
            if value == 1:
                print("YOU ROLLED A ONE! NEXT PLAYERS TURN!")
                current_score =0
                break
            else:
                current_score += value
                print(f"YOU ROLLED A : ", value)
            
            print(f"YOUR CURRENT SCORE IS :", current_score)


    players_scores[player_idx] += current_score
    print("YOUR TOTAL SCORE IS ",players_scores[player_idx])


max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("PLAYER NUMBER ", winning_idx +1,"IS THE WINNER WITH A SCORE OF:", max_score)
    





