Task1:
I used Gym library(gym is toolkit that provides wide variety of simulated environnement).
i used gym.make to load the premade env(frozenlake) and i returned it. "    return gym.make("FrozenLake-v0", desc=desc, map_name=map_name)"
variables:
desc--> custom description of the map to load for the environment
map_name --> string containing the pre-made map to load
is_slippery -->is a boolean to determine if the ice is slippery
if desc & map_name are none = randomly generated 8x8 map.
