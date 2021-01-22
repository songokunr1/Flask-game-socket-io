import pandas as pd
import csv
f = open('slowa.txt', 'r', encoding='utf=-8')

slowa = []

for x in f:
    if len(x) <= 7:
        slowa.append(x[:-2])

f.close()

df = pd.DataFrame(slowa)
df.to_csv('new3.csv', index=False, sep=',', header=False, quoting=csv.QUOTE_NONNUMERIC, encoding='utf-8', line_terminator=",")