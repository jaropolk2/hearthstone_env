from gym.envs.registration import register

register(
    id='hearthstone-v0',
    entry_point='gym_hearthstone.envs:HearthstoneEnv',
)
