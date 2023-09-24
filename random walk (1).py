# -*- coding: utf-8 -*-

# -- Sheet --

import pandas_datareader as web
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

from matplotlib import style

style.use("ggplot")

start = dt.datetime(2020,1,1)
end = dt.datetime(2030,1,1)

numsimulations = 100
numdays = 252

simulation_df = pd.DataFrame()

prices = [100,100]

lastprice = prices[-1]

simulation_df = pd.DataFrame
price_series = []





simulation_df.to_csv("data/data.csv")

import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

l = 100
steps = np.random.choice([-1, 1], size=l) + 0.05 * np.random.randn(l) # l steps
position = np.cumsum(steps) # integrate the position by summing steps values
y = 0.05 * np.random.randn(l)

fig = go.Figure(data=go.Scatter(
    x=position,
    y=y,
    mode='markers',
    name='Random Walk in 1D',
    marker=dict(
        color=np.arange(l),
        size=7,
        colorscale='Reds',
        showscale=True,
    )
))

fig.update_layout(yaxis_range=[-1, 1])
fig.show()

simulation_df.plot(figsize=(15,7),grid=True)
plt.show()



# -- Sheet 2 --

import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style



last_price = 100

#Number of Simulations
num_simulations = 100
num_days = 260

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = 0.02
    
    price_series = []
    
    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol)) + 0.05
        price_series.append(price)
        count += 1
    
    simulation_df[x] = price_series
    
fig = plt.figure()

plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Седмица')
plt.ylabel('Цена')
plt.show()

