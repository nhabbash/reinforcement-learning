## K-Armed Bandit Environment

# Overview
K-Armed Bandit Environemnt for OpenAI Gym as defined in Sutton and Barto's Reinforcement Learning: An Introduction - Chapter 2.

The environment takes as input the rewards distribution for each lever as a list of lists of means and stdevs of a normal distribution, with k being the length of this list.
The defined environment is `karmedbandits-v0`.

# Installation
```sh
cd gym-bandits
pip install -e . 
```

# Usage

```python
import gym
env = gym.make('gym_bandits:karmedbandits-v0')
```

# Notes
Inspiration taken from https://github.com/JKCooper2/gym-bandits. 