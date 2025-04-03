import pandas as pd

data = [
    [1, 'Linus Torvalds', 'Finland', 'Linux Kernel', 1991],
    [2, 'Tim Berners-Lee', 'England', 'World Wide Web', 1990],
    [3, 'Guido van Rossum', 'Netherlands', 'Python', 1991]
]

columns = ['SN', 'Name', 'Country', 'Contribution', 'Year']

df = pd.DataFrame(data, columns=columns)
df.set_index('SN', inplace=True)

print(df)
