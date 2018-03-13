import gym
from gym import error, spaces, utils
from gym.utils import seeding

class HearthstoneEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    print("Hearthstone Game Environment Start")
    self.action_space = None
    self.reset()

  def step(self, action):
    pass

  def reset(self):
    pass

  def render(self, mode='human', close=False):
    pass
