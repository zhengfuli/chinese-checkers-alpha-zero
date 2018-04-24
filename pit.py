import Arena
from MCTS import MCTS
from metasquares.MetaSquaresGame import MetaSquaresGame, display
from metasquares.MetaSquaresPlayers import *
from metasquares.pytorch.NNet import NNetWrapper as NNet

import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

g = MetaSquaresGame(8)

# all players
rp = RandomPlayer(g).play
gp = GreedyMetaSquaresPlayer(g).play
hp = HumanMetaSquaresPlayer(g).play

# nnet players
n1 = NNet(g)
# n1.load_checkpoint('/home/dell/temp/','checkpoint_4.pth.tar')
n1.load_checkpoint('./temp/','best.pth.tar')
args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))


# n2 = NNet(g)
# n2.load_checkpoint('./','best.pth.tar')
# args2 = dotdict({'numMCTSSims': 25, 'cpuct':1.0})
# mcts2 = MCTS(g, n2, args2)
# n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

# arena = Arena.Arena(n1p, gp, g)
# print(arena.playGames(100, verbose=False))

arena = Arena.Arena(n1p, hp, g, display=display)
print(arena.playGames(10, verbose=True))
