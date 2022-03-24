#!/usr/bin/env python3
"""Task 3"""


import numpy as np
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1,
          gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):

    """function that train Q_learning:
    env is the FrozenLakeEnv
    Q is a numpy.ndarray
    episodes is the total number of ep
    alpha is the learning rate
    gamma is the discount rate
    epsilon is the initial threshold
    """

    # agent start from 0.
    total_rewards = []
    for i in range(episodes):
        env.reset()
        before = 0
        reward = 0
        current_state = 0

        # epsilon_greedy is imported from the prev task
        for i in range(max_steps):
            next_move = epsilon_greedy(Q, current_state, epsilon)
            current_state, reward, succes, _ = env.step(next_move)
            # In case of losing:
            # the agent falls in hole & he lose -1 from the reaward
            if succes is True and reward == 0:
                reward = -1

            # Update the Q_table
            # Calculating the total rewards before i return it.
            Q[before, next_move] += (alpha * (reward + gamma
                                              * np.max(Q[current_state])
                                              - Q[before, next_move]))
            before = current_state
            if succes is True:
                break
        epsilon = max(epsilon * (1 - epsilon_decay), min_epsilon)
        total_rewards.append(reward)

    # Print a simple message
    print("\U0001f600", "Hi")

    # Return the total rewards claimed from the agent
    # Retrun the updated Q-table
    return Q, total_rewards,
