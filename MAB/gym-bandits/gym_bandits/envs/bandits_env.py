import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class KArmedBandits(gym.Env):
    """
    Bandit environment base to allow agents to interact with the class k-armed bandits as defined in Sutton and Barto's Reinforcement Learning: An Introduction - Chapter 2

    r_dist:
        The payoffs (rewards) of each lever. It's defined as a list of means and standard deviations of a normal distribution for each lever. (called q*(a))
    """

    def __init__(self, r_dist):
        for reward in r_dist:
            if not isinstance(reward, list):
                raise ValueError("r_dist must be in the format [[mean, stdev], [mean, stdev], ...]")
            elif reward[1] <= 0:
                raise ValueError("Every stdev in the rewards has to be greater than 0")

        self.r_dist = r_dist
        self.k_bandits = len(r_dist)
        self.action_space = spaces.Discrete(self.k_bandits)
        self.observation_space = spaces.Discrete(1) # Nonassociative Bandits

        self._seed()
        
    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return[seed]

    def step(self, action):
        assert self.action_space.contains(action)

        reward = 0
        done = True

        reward = np.random.normal(self.r_dist[action][0], self.r_dist[action][1])

        return 0, reward, done, {}
    
    def reset(self):
        return 0
    
    def render(self, mode='human', close='False'):
        pass