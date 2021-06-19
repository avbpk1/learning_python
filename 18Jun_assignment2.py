# 2) Assume a list of values where you have the product name and price separated by comma. Display these strings in the descending order of price.
prod_catalog = ["Idli,50","Puri,100","Vada,80","Pesarattu,200","Chai,30","Meals,500"]
print("Product list in reverse order of prices")
for prod in sorted(prod_catalog, key= lambda prod: int(prod.split(',')[1]),reverse=True):
    print(prod)
# Improved version with Pretty Table
from prettytable import PrettyTable
table = PrettyTable()
table.title = 'Product Prices'
table.field_names = ['Product','Price']
for prod in sorted(prod_catalog, key= lambda prod: int(prod.split(',')[1]),reverse=True):
    #table.add_row([prod.split(',')[0],prod.split(',')[1]])
    table.add_row(prod.split(','))

print(table)
