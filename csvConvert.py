import pandas as pd
import os

data = pd.read_csv('shorts.csv', encoding='utf-8')
with open('comments.txt', 'a+', encoding='utf-8') as f:
    for line in data.values:
        lineStr1=(str(line).replace('[\'', ''))
        f.write(lineStr1.replace('\']','') + '\n')