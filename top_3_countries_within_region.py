import requests
from prettytable import PrettyTable
import pandas as pd
url = input("Please enter get api URL:")
resp = requests.get(url)
if resp.status_code != 200:
    f"Sorry Error requesting data from URL - {url}"
    exit(1)
countries = resp.json()
# table = PrettyTable(['Name','Area'])
# for c in sorted(countries, key=lambda c: (c['area'] if c['area'] else 0), reverse=True)[:5]:
#     table.add_row((c['name'],c['area']))
# print(table)

for cnts in countries:
    dff = pd.DataFrame.from_dict(cnts, orient="index")
    dff[['region', 'name']].sort_values(['population'], ascending=False).head(3)
    #dff = df.loc[df['Newspaper'] != 'Total']
    # reg_countries = df.groupby(['region','country'])
    # print(reg_countries.sum('population'))
    print(dff)
