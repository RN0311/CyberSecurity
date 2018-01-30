## Value Iteration
### Algorithm
```python
* Start with V*(s) = 0 for all s.
* For i = 1,2 .. H
* Given V*(i), calculate for all states s which belongs to S. 
>>>> V(i+1)*(s) = max(sum(T(s,a,s')[R(s,a,s')+V(i)*(s')]))

This is called as value update or Bellman update/backup.
```
```V(i+1)*``` is the expected sum of rewards accumulated when starting from state s and acting optimally 
for a horizon of i steps.<br >
source code: [value_iteration.py](https://github.com/RN0311/CyberSecurity/blob/master/Value%20Iteration/value_iteration.py)

### Resources
* [Markov Decision Process](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa12/slides/mdps-exact-methods.pdf)
* [Deep Reinforcement Learning Demysitifed](https://medium.com/@m.alzantot/deep-reinforcement-learning-demysitifed-episode-2-policy-iteration-value-iteration-and-q-978f9e89ddaa)

