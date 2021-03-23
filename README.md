
  # Simulated Annealing with KNN
## What is SA?
Simulated Annealing (SA) is an effective and general form of optimization. It is useful in finding global 
optima in the presence of large numbers of local optima. “Annealing” refers to an analogy with 
thermodynamics, specifically with the way that metals cool and anneal. Simulated annealing uses the 
objective function of an optimization problem instead of the energy of a material.
Implementation of SA is surprisingly simple. The algorithm is basically hill-climbing except instead of 
picking the best move, it picks a random move. If the selected move improves the solution, then it is 
always accepted. Otherwise, the algorithm makes the move anyway with some probability less than 1. 

The probability decreases exponentially with the “badness” of the move, which is the amount deltaE 
by which the solution is worsened (i.e., energy is increased.)
Prob(accepting uphill move) ~ 1 - exp(deltaE / kT))
A parameter T is also used to determine this probability. It is analogous to temperature in an annealing 
system. At higher values of T, uphill moves are more likely to occur. As T tends to zero, they become 
more and more unlikely, until the algorithm behaves more or less like hill-climbing. In a typical SA 
optimization, T starts high and is gradually decreased according to an “annealing schedule”. The 
parameter k is some constant that relates temperature to energy (in nature it is Boltzmann’s constant.)
Simulated annealing is typically used in discrete, but very large, configuration spaces, such as the set of 
possible orders of cities in the Traveling Salesman problem and in VLSI routing. It has a broad range of 
application that is still being explored.

## About Dataset
The data set used, the pair of dealing with divorce problems in Turkey has created the survey data.
Attribute Information:
1. If one of us apologizes when our discussion deteriorates, the discussion ends.
2. I know we can ignore our differences, even if things get hard sometimes.
3. When we need it, we can take our discussions with my spouse from the beginning and correct it.
4. When I discuss with my spouse, to contact him will eventually work.
5. The time I spent with my wife is special for us.
6. We don't have time at home as partners.
7. We are like two strangers who share the same environment at home rather than family.
8. I enjoy our holidays with my wife.
9. I enjoy traveling with my wife.
10. Most of our goals are common to my spouse.
11. I think that one day in the future, when I look back, I see that my spouse and I have been in harmony 
with each other.
12. My spouse and I have similar values in terms of personal freedom.
13. My spouse and I have similar sense of entertainment.
14. Most of our goals for people (children, friends, etc.) are the same.
15. Our dreams with my spouse are similar and harmonious.6
16. We're compatible with my spouse about what love should be.
17. We share the same views about being happy in our life with my spouse
18. My spouse and I have similar ideas about how marriage should be
19. My spouse and I have similar ideas about how roles should be in marriage
20. My spouse and I have similar values in trust.
21. I know exactly what my wife likes.
22. I know how my spouse wants to be taken care of when she/he is sick.
23. I know my spouse's favorite food.
24. I can tell you what kind of stress my spouse is facing in her/his life.
25. I have knowledge of my spouse's inner world.
26. I know my spouse's basic anxieties.
27. I know what my spouse's current sources of stress are.
28. I know my spouse's hopes and wishes.
29. I know my spouse very well.
30. I know my spouse's friends and their social relationships.
31. I feel aggressive when I argue with my spouse.
32. When discussing with my spouse, I usually use expressions such as ‘you always’ or ‘you never’ .
33. I can use negative statements about my spouse's personality during our discussions.
34. I can use offensive expressions during our discussions.
35. I can insult my spouse during our discussions.
36. I can be humiliating when we discussions.
37. My discussion with my spouse is not calm.
38. I hate my spouse's way of open a subject.
39. Our discussions often occur suddenly.
40. We're just starting a discussion before I know what's going on.
41. When I talk to my spouse about something, my calm suddenly breaks.
42. When I argue with my spouse, ı only go out and I don't say a word.
43. I mostly stay silent to calm the environment a little bit.
44. Sometimes I think it's good for me to leave home for a while.
45. I'd rather stay silent than discuss with my spouse.
46. Even if I'm right in the discussion, I stay silent to hurt my spouse.7
47. When I discuss with my spouse, I stay silent because I am afraid of not being able to control my 
anger.
48. I feel right in our discussions.
49. I have nothing to do with what I've been accused of.
50. I'm not actually the one who's guilty about what I'm accused of.
51. I'm not the one who's wrong about problems at home.
52. I wouldn't hesitate to tell my spouse about her/his inadequacy.
53. When I discuss, I remind my spouse of her/his inadequacy.
54. I'm not afraid to tell my spouse about her/his incompetence.
