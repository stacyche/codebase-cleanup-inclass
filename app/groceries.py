
# READ INVENTORY OF PRODUCTS

#products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
#products_df = read_csv(products_filepath)
#products = products_df.to_dict("records")

import os


def to_usd(my_price):
    '''
    This is a docstring. It tells us what this function is about. 
    What its responsibilities are. 
    What the parama are about 
    What datatypes the params are. 
    What this function will return. 
    Example of invoking the function 

    Invoke like this: to_usd(9.999)
    '''
    return '${:,.2f}'.format(my_price)





# checks to see if a products.csv file exists. If not, it uses the default
if os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")) == True:
    print("USING CUSTOM PRODUCTS CSV FILE...")
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
else:
    print("USING DEFAULT PRODUCTS CSV FILE...")
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "default_products.csv")



from pandas import read_csv

#reads the csv file into products variable
products = read_csv(csv_filepath)
#pandas transforms the data into a list of dictionaries
products = products.to_dict('records')



# PRINTED INVENTORY REPORT

print("---------")
print("THERE ARE", len(products), "PRODUCTS:")
print("---------")

for p in products:
    print("..." + p["name"] + "   " + to_usd(p["price"]))


all_prices = []
for p in products:
    all_prices.append(float(p["price"]))

import statistics
avg_price = statistics.median(all_prices)

print("---------")
print("AVERAGE PRICE:", to_usd(avg_price))





# EMAIL INVENTORY REPORT
