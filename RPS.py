# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess
def BeatQuincy(prev_play, opponent_history = [],counter = [0]):
    options = ["P","P","S","S","R"]
    counter[0]+=1
    guess = options[counter[0]%len(options)]


    return guess