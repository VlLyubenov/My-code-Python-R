# -*- coding: utf-8 -*-

# -- Continuous --

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
import seaborn as sb

data = np.arange(1,10,0.1)

pdf = norm.pdf(data, loc = 5 , scale = 1 )

sb.set_style('whitegrid')
sb.lineplot(data, pdf , color = 'black')
plt.xlabel('X')
plt.ylabel('Вероятност')

cdf = norm.cdf(data, loc = 5 , scale = 1 )
sb.set_style('whitegrid')
sb.lineplot(data, cdf , color = 'black')
plt.xlabel('X')
plt.ylabel('Кумулативна вероятност')

# -- Discrete --

import seaborn as sns
import pandas as pd
import numpy as np
import seaborn as sb
sns.set_style('whitegrid')

avg = 5
std_dev = .1
num_reps = 500
num_simulations = 1000

pct_to_target = np.random.normal(avg, std_dev, num_reps).round(2)

np.random.normal(avg, std_dev, num_reps).round(2)

sb.set_style('whitegrid')
sb.histplot(pct_to_target, stat = "probability", color = 'black')
plt.xlabel('X')
plt.ylabel('Вероятност')

# -- Law of large numbers --

import matplotlib.pyplot as plt
import random 

n=1
prob=[]
flip=[]

while n<1000:
    head=0
    tail=0

    for i in range(n):
        if random.randint(0,1)==0:
            head+=1
        else:
            tail+=1
    k=head/(head+tail)
    prob.append(k)
    flip.append(n)
    n+=1


plt.subplot(2,1,1)
plt.hist(prob,100,label='Probality of Heads')
plt.legend()


plt.subplot(2,1,2)
plt.plot(flip,prob)
plt.xlabel('Number of Flips')
plt.ylabel('Probability of Heads')
plt.grid(True)

plt.show()

sb.set_style('whitegrid')
sb.histplot(prob , stat = "probability",color = 'black')
plt.xlabel('X')
plt.ylabel('Вероятност')

sb.set_style('whitegrid')
sb.lineplot(flip,prob, color = 'black')
plt.xlabel('Брой хвърляния на монетата')
plt.ylabel('Средна аритметична на извадката')

# -- Sheet 5 --

import random
randomlist = random.sample(range(1, 10000), 9999)

import statistics

import pandas as pd
randomlist = pd.DataFrame(randomlist)

randomlist.mean

import numpy as np
np.random.random_integers(1000,size=(5,))

sample = randomlist.sample(n=10)

sample.mean()

n = 1
k = list()

while n <1000:
    sample = randomlist.sample(n=10)
    k.append(sample.mean())
    n+=1

means = pd.DataFrame(k)

means

import seaborn as sb
import matplotlib.pyplot as plt


sb.set_style('whitegrid')
sb.displot(means, kind="kde", color = 'black')
plt.xlabel('Средна аритметична на n=10')
plt.ylabel('Вероятност')

sb.set_style('whitegrid')
sb.displot(randomlist, kind="kde", color = 'black')
plt.xlabel('X')
plt.ylabel('Вероятност')

n = 1
k = list()

while n <750:
    sample = randomlist.sample(n=15)
    k.append(sample.mean())
    n+=1

means1 = pd.DataFrame(k)

n = 1
k = list()

while n <300:
    sample = randomlist.sample(n=33)
    k.append(sample.mean())
    n+=1

means2 = pd.DataFrame(k)


sb.set_style('whitegrid')
sb.displot(means1, kind="kde", color = 'black')
plt.xlabel('Средна аритметична на n=15')
plt.ylabel('Вероятност')


sb.set_style('whitegrid')
sb.displot(means2, kind="kde", color = 'black')
plt.xlabel('Средна аритметична на n=30')
plt.ylabel('Вероятност')


sb.set_style('whitegrid')
sb.displot(means, kind="kde", color = 'black')
plt.xlabel('Средна аритметична на n=10')
plt.ylabel('Вероятност')

sb.set_style('whitegrid')
sb.displot(means1, kind="kde", color = 'black')
plt.xlabel('Средна аритметична на n=15')
plt.ylabel('Вероятност')


sb.set_style('whitegrid')
sb.displot(means2, kind="kde", color = 'black')
plt.xlabel('Средна аритметична на n=30')
plt.ylabel('Вероятност')

