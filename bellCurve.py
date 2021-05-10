import random 
import plotly.express as px
import plotly.figure_factory as ff 

diceSum = []
count = []
for i in range(0,100):
      dice1 = random.randint(1,6)
      dice2 = random.randint(1,6)
      diceSum.append(dice1 + dice2)
      count.append(i)
# fig = px.bar(x = diceSum,y = count)
fig = ff.create_distplot([diceSum],['Result'],show_hist = False)
fig.show()


