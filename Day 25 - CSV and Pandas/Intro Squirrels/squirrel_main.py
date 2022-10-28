import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_color_series = data['Primary Fur Color']

gray = 0
cinnamon = 0
black = 0

for squirrel in fur_color_series:
    if squirrel == 'Black':
        black += 1
    elif squirrel == 'Cinnamon':
        cinnamon += 1
    elif squirrel == 'Gray':
        gray += 1

d = {
    'Colors': ['Gray','Cinnamon','Black'],
    'Count': [gray, cinnamon, black]
}

df = pd.DataFrame.from_dict(d)
df.to_csv('squirrel_count.csv')
print(df)