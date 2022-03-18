<h1>reinforcement learning </h1>
<li>what's refeinorcemment learning:
<br>Reinforcement learning is a machine learning training method based on rewarding desired behaviors and/or punishing undesired ones. In general, a reinforcement learning agent is able to perceive and interpret its environment, take actions and learn through trial and error.
 <li>How does it works?
 <br>-it dectect the negative behavoir and find solution. 
  <br> -it assign positive  to the desired actions.
  <br> create q_table:
  <br> Q represent the quality
  <br>Q_learning is an algo that find the best action to maximize the rewards
  <br> how to update a q_table:
  * state: s1
  * action: a1
  * rewards: r1
  <br> so how we update a q_table:
  * first of all the agent start in s1 and take a1 and recieve r1.
  * second the agent  select from  q_table the maximum value or randomly using random(epsilon, e).
  <br>so how we update q_value in q_learning?
  *example:
  *Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action]).
  <br> let's explaing more:
  *lr: mean learning rate: it refer alpha or α ,it defin how much you accept new values vs the old ones & make difference between them and multiply them.
  *Gamma: represent  the immediate balance and the future reward and her value range between 0.8 to 0.99
  *Reawrd: when agent complete some action succesfully in a given state , the agent revcieve some values for that named rewards.
  

This directory contain:
0x00Q-learning:

