from collections import Counter

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago.
#  It is not a very good player so you will need to change the code to pass the challenge.





def beat_quincy(prev_play, opponent_history = [],counter = [-1]):
    # quincy cycles RPPSR so you need to go PSSRP (start with index 0)
    counter[0]+=1
    if prev_play != "":
        opponent_history.append(prev_play)
    
    best_move = {"RP":"S","PP":"R","PS":"P","SR":"P","RR":"S"}
    if len(opponent_history)>=2:
        last_two = "".join(opponent_history[-2:])
    elif len(opponent_history)==1:
        last_two="RR"
    else:
        last_two="SR"
    
    
    guess = best_move[last_two]

    return guess


def BeatKris(prev_play, my_prev_play = [""] , opponent_history = [],counter = [-1]):
    # kris tries to beat your last move, so you need to beat whatever beats your last move, so you can beat whatever beats your last move
    
    if not my_prev_play[0]:
        my_prev_play[0] = "R"
    best_move = {'S':'P', 'P':'R','R':'S'}
    guess = best_move[my_prev_play[0]]
    my_prev_play[0] = guess
    return guess

def BeatMrugesh(prev_play, opponent_history = [],counter = [-1], my_history = [""]):
    # mrugesh tries to beat your most frequent move out of your last 10,
    # if there is a tie in your last 10  mrugesh will pick randomly between the options
    # if there are 2 options you can choose the best one to win/tie, but when there are 3 options its totally random so i picked "P"
    move = "P"
    counter[0]+=1
    if counter[0]==0 or counter[0]==1:
        move = "P"
        my_history.append(move)
        return move
    best_moves_1 = {"P":"R","R":"S","S":"P"}
    best_moves_2 = {
                    "PR":"S",
                    "RP":"S", 
                    "PS":"R",
                    "SP":"R",
                    "RS":"P",
                    "SR":"P"
                    }
    my_last_ten = my_history[-10:]
    most = "".join(most_frequent(my_last_ten))
    if len(most)==1:
        move = best_moves_1[most]
    elif len(most) ==2:
        move = best_moves_2[most]
    elif len(most)==3:
        move = "P"
    
    my_history.append(move)
    
    return move




def most_frequent(strings):
    
    counts = Counter(strings)
    # Get the most common string(s)
    most_common = counts.most_common()
    
    if not most_common:
        return "No valid strings"
    max = most_common[0][1]
    ties = [item[0] for item in most_common if item[1]==max]
    
    return ties
    

def beat_abbey(prev_play,my_prev_play =[""],
          my_history=[],
          play_order={"RR": 0,"RP": 0,"RS": 0,"PR": 0,"PP": 0,"PS": 0,"SR": 0,"SP": 0,"SS": 0, }):

    if not my_prev_play[0]:
        my_prev_play[0]='R'
    my_history.append(my_prev_play[0])

    last_two = "".join(my_history[-2:])
    if len(last_two) == 2:
        play_order[last_two] += 1

    potential_plays = [
        my_prev_play[0] + "R",
        my_prev_play[0] + "P",
        my_prev_play[0] + "S",
    ]

    sub_order = {
        k: play_order[k]
        for k in potential_plays if k in play_order
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
    move = ideal_response[prediction]
    my_prev_play[0] = move
    return move
