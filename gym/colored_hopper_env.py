import gym
import pybullet as p
import pybullet_data

class ColoredHopperEnv(gym.Env):
    def __init__(self):
        self.env = gym.make('Hopper-v3')
        self.client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.hopper_id = p.loadURDF("hopper.urdf", [0, 0, 1])
        self.colors = {
            'torso': [1, 0, 0, 1],  # Red
            'thigh': [0, 1, 0, 1],  # Green
            'leg': [0, 0, 1, 1],    # Blue
            'foot': [1, 1, 0, 1]    # Yellow
        }
        self.setup_colors()

    def setup_colors(self):
        for link_idx in range(p.getNumJoints(self.hopper_id)):
            link_name = p.getJointInfo(self.hopper_id, link_idx)[12].decode('utf-8')
            if link_name in self.colors:
                p.changeVisualShape(self.hopper_id, link_idx, rgbaColor=self.colors[link_name])
            else:
                p.changeVisualShape(self.hopper_id, link_idx, rgbaColor=[1, 1, 1, 1])  # Default to white

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        self.render()
        return obs, reward, done, info

    def reset(self):
        obs = self.env.reset()
        self.render()
        return obs

    def render(self, mode='human'):
        # Custom render using pybullet
        for link_idx in range(p.getNumJoints(self.hopper_id)):
            link_state = p.getLinkState(self.hopper_id, link_idx)
            p.resetBasePositionAndOrientation(self.hopper_id, link_state[0], link_state[1])

if __name__ == "__main__":
    env = ColoredHopperEnv()
    obs = env.reset()
    done = False
    while not done:
        action = env.env.action_space.sample()  # Random action
        obs, reward, done, info = env.step(action)
        time.sleep(0.01)
