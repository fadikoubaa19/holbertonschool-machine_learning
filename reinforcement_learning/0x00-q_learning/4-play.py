#!/usr/bin/env python3
"""Final task"""

import numpy as np
import gym


def play(env, Q, max_steps=100):
    """function that train the agent play"""

    # reset the envirement into the initial stat
    current_episode = env.reset()
    completed = False

    # Render action in every step
    env.render()

    # take action in every step
    for step in range(max_steps):

        # return act with maximum values
        act = np.argmax(Q[current_episode, :])

        # return the four actions
        state, reward, completed, _ = env.step(act)

        # update actions
        env.render()

        # in case of 0 return the reward
        if completed and reward == 0:
            return reward

        # if episode is completed return the total reward
        if(completed):
            break
        current_episode = state
    return reward
