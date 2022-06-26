import flappy_headless
import numpy as np 
from collections import defaultdict
import pickle

#Params for Q-Function
rewardFlying = 1
rewardKill = -10000
alpha = 0.2
gamma = 0.9

oldState = None
oldAction = None
gameCounter = 0
gameScores = []

#Q[0] -> no jump; Q[1] -> jump
Q = defaultdict(lambda: [0, 0])

#Get parameter as string 
def paramsToDicName(params):
    playerVelY = params['playerVelY']
    playerY = round(params['playerY'] / 10) * 10

    #check if Bot should focus on next pipe
    if int(params['upperPipes'][0]['x']) < 56:
        index = 1
    else:
        index = 0
        
    upperPipeX = round(int(params['upperPipes'][index]['x']) / 10) * 10
    upperPipeY = round(int(params['upperPipes'][index]['y']) / 10) * 10

    return str(playerVelY) + '_' + str(playerY) + '_' + \
        str(upperPipeX) + '_' + str(upperPipeY)
        


def onGameOver(gameInfo):
    global oldState
    global oldAction
    global gameCounter
    global gameScores

    gameScores.append(gameInfo['score'])

    if gameCounter % 100 == 0:
        print(str(gameCounter) + ': ' + str(np.mean(gameScores[-100:])))
    

    #Get index to be updated
    prevReward = Q[oldState]
    index = None
    if oldAction == False:
        index = 0
    else:
        index = 1

    #Update old state with Q-function for non deterministic szenario
    #estReward = 0 bc. of no further action
    #Action was not successful
    prevReward[index] = (1 - alpha) * prevReward[index] + \
        alpha * rewardKill

    Q[oldState] = prevReward

    oldState = None
    oldAction = None

    #Save Q-dictionary
    if gameCounter % 10000 == 0:
        with open("Q-Values/" + str(gameCounter) + ".pickle", "wb") as file:
            pickle.dump(dict(Q), file)

    gameCounter += 1


def shouldEmulateKeyPress(params):
    global oldState
    global oldAction

    #Get dict entry
    state = paramsToDicName(params)
    estReward = Q[state]

    #Get index to be updated
    prevReward = Q[oldState]
    index = None
    if oldAction == False:
        index = 0
    else:
        index = 1

    #Update old state with Q-function for non deterministic szenario
    #Action was successful
    prevReward[index] = (1 - alpha) * prevReward[index] + \
        alpha * (rewardFlying + gamma * max(estReward))

    Q[oldState] = prevReward

    #Check if to jump or not to jump
    oldState = state

    if estReward[0] >= estReward[1]:
        oldAction = False
        return False
    else:
        oldAction = True
        return True

flappy_headless.main(shouldEmulateKeyPress, onGameOver)