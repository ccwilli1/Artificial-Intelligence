import random
from math import exp

MAX_TRIALS = 100
MAX_SIDEWAYS = 100

Objects = {'A': (10, 2), 'B': (6, 3), 'C': (4, 8),
           'D': (8, 5), 'E': (9, 5), 'F': (7, 6)}
C = 15
Items = list(Objects.keys())
nObjects = len(Objects)

def Value(state):
    # write your code here
    # Hint: you will need to use Items list to access the
    #       Objects weights and values

def get_neighbor(state):
    # write your code here
    
def hill_climbing(state):
    # write your code here
    
bestValue = -1
bestState = []
for k in range(40):
    state = [random.randrange(2) for k in range(nObjects)]
    random.shuffle(state)
    state = hill_climbing(state)
    v = Value(state)
    
    if bestValue < v:
        bestValue = v
        bestState = state
print('best state found: ', bestState, bestValue)
    
