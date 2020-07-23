from gym.envs.registration import register

register(
    id='karmedbandits-v0',
    entry_point='gym_bandits.envs:KArmedBandits',
)