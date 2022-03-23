Task1:
<br>I used Gym library(gym is toolkit that provides wide variety of simulated environnement).
<br>i used gym.make to load the premade env(frozenlake) and i returned it. "    return gym.make("FrozenLake-v0", desc=desc, map_name=map_name)"
<br>variables:
<br>desc--> custom description of the map to load for the environment
<br>map_name --> string containing the pre-made map to load
<br>is_slippery -->is a boolean to determine if the ice is slippery
<br>if desc & map_name are none = randomly generated 8x8 map.

Task2:
<br> in this task i used (env.observation_space.n)--> to define the observations of environnement to inform the agent before he start running.
<br> i also used (env.action_space.n) --> to define characteristics of the action space and to define the minimum and maximum value too.
<br>Variables:
<br>s1=env.action_space.n
<br>a1=env.observation_space.n
<br>Please for more informations about OpenAI check this:https://leechangyo.github.io/reinforcement%20learning/2019/10/03/OpenAI-Gym-Tutorial/
<br>in the end i returned the Q_tables filled with zeros using numpy(np.zeros).

Task3:
in this task i create function that uses epsilon to determine the next action for agent
<br> so as first step i needed to know if i will explore or exploite by using numpy (np.uniform.random)
<br> Then i used again numpy(numpy.random.randint) to explore it.
<br> in the end i returned the maximum element of the next move using (np.argmax)
