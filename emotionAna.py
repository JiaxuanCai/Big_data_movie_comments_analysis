import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt

f = open('comments.txt', 'r', encoding='UTF-8')
list = f.readlines()
sentimentslist = []
for i in list:
    s = SnowNLP(i)
    # print s.sentiments
    sentimentslist.append(s.sentiments)
plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
plt.xlabel('Sentiments Probability')
plt.ylabel('Quantity')
plt.title('Analysis of Sentiments')
plt.show()