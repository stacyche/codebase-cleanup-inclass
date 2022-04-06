

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

if __name__ == "__main__": 
    # nesting code in the main condition will 
    # allow other scripts to cleanly import functions from this file 
    # without running this code 

    #this code still gets run when we invoke the script from the command line 
    price = input("Please choose a price like 4.9999")

    print(to_usd(float(price)))

to_usd