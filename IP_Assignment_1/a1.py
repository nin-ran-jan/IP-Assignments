def show_menu():

    #This function prints the menu at the starting of the program, just as it is executed.
    #This enables the customer to go through the item codes and costs, to make a decision as to what to buy.
    #No calculations and no return value in this function.
        
    print("""=================================================
                   MY BAZAAR
=================================================
Hello! Welcome to my grocery store!
Following are the products available in the shop:

-------------------------------------------------
CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
-------------------------------------------------
  0  | Tshirt      | Apparels     | 500
  1  | Trousers    | Apparels     | 600
  2  | Scarf       | Apparels     | 250
  3  | Smartphone  | Electronics  | 20,000
  4  | iPad        | Electronics  | 30,000
  5  | Laptop      | Electronics  | 50,000
  6  | Eggs        | Eatables     | 5
  7  | Chocolate   | Eatables     | 10
  8  | Juice       | Eatables     | 100
  9  | Milk        | Eatables     | 45
------------------------------------------------
""")






          
def get_regular_input():

    #This function obtains the regular input as entered by the customer.
    #A list of length 10, and respective quantity values is returned.
    
    print("""

-------------------------------------------------
ENTER ITEMS YOU WISH TO BUY
-------------------------------------------------""")

    regular_items = input("Enter the item codes (space-seperated): ") #The input is obtained as a string, with space seperated entries.
    l = regular_items.split()
    
    #The <string>.split() method seperates all the items of the <string>.
    #It does this by deleting all the <space> entries of the <string> and stores rests of the substrings in the form of an ordered list.
    #The entries in the string are of the type <str>.
    
    quant = [0]*10

    #A list of length 10 and values <0> is created.
    #This is the list that will be returned by the function.
    
    for i in range(len(l)):

        #Runs the loop as many times as the length of the list <l>.
        
        if int(l[i]) not in range(10):
            print("\n",l[i], " is not a valid entry in this list. It will not be considered.", sep = "")

            #Checks for invalid inputs.
            #Only accepts input if it is an integer entry between 0 and 9 (inclusive).
            
        else:
            quant[int(l[i])] += 1

            #Increment of <quant>'s index by 1 with respect to its index as entered by the customer.
        
    return quant







def get_bulk_input():

    #This function obtains bulk input from the customer.
    #A list of length 10, and respective quantity values is returned.
    
    print("""
-------------------------------------------------
ENTER ITEM AND QUANTITIES
-------------------------------------------------""")
    
    l = ["Tshirt","Trousers","Scarf","Smartphone","iPad","Laptop","Eggs","Chocolate","Juice","Milk"]

    #A list of item descriptions sorted on the basis of code indexes.
    
    quant = [0]*10

    #A list of length 10 and values <0> is created.
    #This is the list that will be returned by the function.
    
    while True:

        #Will run the loop till the <break> command is used to exit it.
        
        inp = input("Enter code and quantity (leave blank to stop): ")

        #Inputs the code and quantity from the customer.

        if inp == "":

            #Breaks from the loop if the string entered is empty.
            
            print("Your order has been finalized.")
            
            break
        
        
        
        inp = inp.split(" ")

        #Splits the string on the basis of <spaces> and stores it in a list.
        #The indexing of the string is done sequentially as done in the original string.
        #The values of the list are of type <str>.
        

        if len(inp) != 2:
            
            print("Invalid input. Try again.\n")

            #Can only have 2 entries in the list.

        elif inp[0] == "" and inp[1] == "":
            
            print("Invalid input. Try again.\n")

            #Negates a corner case when a single space is entered as input.

        elif int(inp[0]) in range(10) and int(inp[1]) >= 0:
            
            quant[int(inp[0])] += int(inp[1])
            print("You added",int(inp[1]),l[int(inp[0])],"\n")

            #If the entered code and quantity are errorless, they are entered (with the particular index) to the list <quant>.
            #A conformational line is printed alongside.

        elif int(inp[0]) not in range(10) and int(inp[1]) < 0:

            print("Invalid code and quantity. Try again.\n")

            #Invalid code and quantity.

        elif int(inp[1]) < 0:

            print("Invalid quantity. Try again.\n")

            #Invalid quantity.

        elif int(inp[0]) not in range(10):

            print("Invalid code. Try again.\n")

            #Invalid code.
        

    return quant
            

        




def print_order_details(quantities):

    #This function prints the order details.
    #No value is returned in this function.
    
    print("""

-------------------------------------------------
ORDER DETAILS
-------------------------------------------------""")
    
    c = 0
    l = ["Tshirt","Trousers","Scarf","Smartphone","iPad","Laptop","Eggs","Chocolate","Juice","Milk"]

    #A counter for the serial number is used.
    #A list corresponding to item descriptions and item code is entered.
    #l[<item code>] = <item description>
    
    costs = [500,600,250,20000,30000,50000,5,10,100,45]

    #Costs of the items, ordered by the item codes.
    #costs[<item code>] = <item cost>
    
    for i in range(10):

        #A loop runs 10 times (the number of items).
        
        if quantities[i] != 0:

            #Checks for each entry of the list, whether it is <0> or not.
            
            c += 1

            #Increments the counter by 1.
            
            print("[",c,"] ",l[i]," x ",quantities[i]," = Rs ",costs[i]," * ",quantities[i]," = Rs ",quantities[i]*costs[i],sep = "")

            #Prints the required line for a particular order item.







def calculate_category_wise_cost(quantities):

    #This function calculates the cost of products segregated by category.
    #It returns a tuple, with costs of each category.
    #Its parameter is the list with all the order entries.
    
    print("""

-------------------------------------------------
CATEGORY-WISE COST
-------------------------------------------------""")
    
    costs = [500,600,250,20000,30000,50000,5,10,100,45]
    
    #List of costs of each item, based on index = item_code.
    
    apparels_cost = 0
    electronics_cost = 0
    eatables_cost = 0

    #Initializing variables with value <0>.
    
    for i in range(10):

        #Runs loop 10 times (The number of items).
        
        if i in [0,1,2]:
            
            apparels_cost += quantities[i]*costs[i]

            #Checks for apparels and adds cost to variable.
            
            if i == 2:
                
                print("Apparels = Rs",apparels_cost)

                #Prints apparels cost only when last entry of apparels is running in the loop.
                
        elif i in [3,4,5]:
            
            electronics_cost += quantities[i]*costs[i]

            #Checks for electronics and adds cost to variable.
            
            if i == 5:
                
                print("Electronics = Rs",electronics_cost)

                #Prints electronics cost only when last entry of electronics is running in the loop.
                
        else:
            
            eatables_cost += quantities[i]*costs[i]

            #Checks for eatables and adds cost to variable.
            
            if i == 9:
                
                print("Eatables = Rs",eatables_cost)

                #Prints eatables cost only when last entry of eatables is running in the loop.

                
    return (apparels_cost,electronics_cost,eatables_cost)
    





def get_discount(cost, discount_rate):

    #This helper function returns the discount value, based on the parameters of cost and discount rate entered.
    
    return int(cost*discount_rate)






def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):

    #This function calculates the discounted prices based on the category of the item bought.
    #The parameters entered are the respective category-wise costs calculated earlier in the program.
    #The function returns a tuple of category-wise after discount prices.
    
    print("""

-------------------------------------------------
DISCOUNTS
-------------------------------------------------""")
    
    app = 0
    ele = 0
    eat = 0

    #Category-wise discounted amounts, initialized to <0>.
    
    if apparels_cost >= 2000 and apparels_cost != 0:

        #Checks for discount conditions.
        
        print("[APPAREL] Rs ",apparels_cost," - Rs ",sep = "",end = "")
        
        app = get_discount(apparels_cost,0.1)

        #Calculates the discounted amount for this category.
        
        apparels_cost -= app

        #Reduces the category cost by the discounted amount, by calling the helper function.
        
        print(app," = Rs ",apparels_cost,sep = "")
        
        
        
    if electronics_cost >= 25000 and electronics_cost != 0:

        #Checks for discount conditions.

        print("[ELECTRONICS] Rs ",electronics_cost," - Rs ",sep = "",end = "")
        
        ele = get_discount(electronics_cost,0.1)

        #Calculates the discounted amount for this category, by calling the helper function.
        
        electronics_cost -= ele

        #Reduces the category cost by the discounted amount, by calling the helper function.

        print(ele," = Rs ",electronics_cost,sep = "")

        
        
    if eatables_cost >= 500 and eatables_cost != 0:

        #Checks for discount conditions.

        print("[EATABLES] Rs ",eatables_cost," - Rs ",sep = "",end = "")
        
        eat = get_discount(eatables_cost,0.1)

        #Calculates the discounted amount for this category, by calling the helper function.
        
        eatables_cost -= eat

        #Reduces the category cost by the discounted amount, by calling the helper function.
        
        print(eat," = Rs ",eatables_cost,sep = "")

        

    print()

    #Prints an empty line.
        
    print("TOTAL DISCOUNT = Rs ",app+ele+eat,"\nTOTAL COST = Rs ", apparels_cost+electronics_cost+eatables_cost, sep = "")
    
    return (apparels_cost, electronics_cost, eatables_cost)
    
        


                                                

def get_tax(cost, tax):

    #This helper function returns the tax value, based on the parameters of cost and tax rate entered.
    
    return int(cost*tax)





def calculate_tax(apparels_cost, electronics_cost, eatables_cost):

    #This function calculates the tax based on which catergory the item belongs to.
    #The parameters are the category-wise costs, after discounts.
    #The function returns the values of total_cost_after_tax and total_taxed_amount.
    
    print("""

-------------------------------------------------
TAX
-------------------------------------------------""")
    
    app = 0
    ele = 0
    eat = 0

    #Initializing empty variables, for the tax amounts of each category.
    
    if apparels_cost != 0:

        #Checks if category cost is not <0>.
        
        print("[APPAREL] Rs ",apparels_cost," * 0.10 = Rs ",sep = "",end = "")
        
        app = get_tax(apparels_cost,0.1)

        #Calls helper function and calculates the taxed value based on category tax rate.
        
        apparels_cost += app

        #Adds taxed amount to the cost of category.
        
        print(app)

        
        
    if electronics_cost != 0:

        #Checks if category cost is not <0>.
        
        print("[ELECTRONICS] Rs ",electronics_cost," * 0.15 = Rs ",sep = "",end = "")
        
        ele = get_tax(electronics_cost,0.15)

        #Calls helper function and calculates the taxed value based on category tax rate.
        
        electronics_cost += ele

        #Adds taxed amount to the cost of category.

        print(ele)

        
        
    if eatables_cost != 0:

        #Checks if category cost is not <0>.

        print("[EATABLES] Rs ",eatables_cost," * 0.05 = Rs ",sep = "",end = "")
        
        eat = get_tax(eatables_cost,0.05)

        #Calls helper function and calculates the taxed value based on category tax rate.
        
        eatables_cost += eat

        #Adds taxed amount to the cost of category.
        
        print(eat)

        

    print()

    #Prints an empty line.
        
    print("TOTAL TAX = Rs ",app+ele+eat,"\nTOTAL COST = Rs ", apparels_cost+electronics_cost+eatables_cost, sep = "")
    
    return (apparels_cost+electronics_cost+eatables_cost, app+ele+eat)





def apply_coupon_code(total_cost):

    #This function checks if a coupon code can be applied.
    #The parameter is the total cost after tax and discount.
    #The fucntion returns cost_after_coupon_code_applied and the price_saved because of the coupon code.
    
    print("""

-------------------------------------------------
COUPON CODE
-------------------------------------------------""")
    
    saved_price = 0

    #Initialize an empty variable.
    
    while True:

        #Runs the loop until the <break> command is used.
        
        code = input("Enter coupon code (else leave blank): ")

        #Inputs the coupon code (case sensitive).
        
        if code == "":

            #Checks if the entered string is empty.
            
            print("No coupon code applied.\n")
            
            break
        
        
        elif code == "HELLE25" and total_cost >= 25000:

            #Checks if code is entered correctly, and the conditions of the coupon code are met.
            
            print("[HELLE25] min(5000, Rs ",total_cost," * 0.25) = Rs ",min(5000,int(total_cost*0.25)),"\n", sep = "")
            
            saved_price = min(5000,int(total_cost*0.25))

            #Calculates the saved_price, that is the minimum of both the conditions.
            
            total_cost -= saved_price

            #Reduces value from the saved price.
            
            break
        
        
        elif code == "CHILL50" and total_cost >= 50000:

            #Checks if code is entered correctly, and the conditions of the coupon code are met.
            
            print("[CHILL50] min(10000, Rs ",total_cost," * 0.50) = Rs ",min(10000,int(total_cost*0.50)),"\n", sep = "")
            
            saved_price = min(10000,int(total_cost*0.50))

            #Calculates the saved_price, that is the minimum of both the conditions.
            
            total_cost -= saved_price

            #Reduces value from the saved price.
            
            break
        
        
        else:
            
            print("Invalid coupon code. Try again.\n")

            #If none of the conditions are satisfied, the input is taken again and again, from the customer.

            
    print("TOTAL COUPON DISCOUNT = Rs", saved_price, "\nTOTAL COST = Rs", total_cost)
        
    return (total_cost,saved_price)  




def main():

    #This is the main function.
    #All the functions used in the program are called from this function.
    #The order and cohesion of the program is decided from this function.

    show_menu()
    
    while True:

        #Takes input for regular/bulk order.
        #Repeats loop till correct values entered by the customer.

        yesno = input("Would you like to buy in bulk? (y or Y / n or N): ")

        if yesno == "y" or yesno == "Y":

            #For a particular input, a particular function is called.
            #Thus, the flow of the program continues.
            
            get_input = get_bulk_input()
            
            break

        
        elif yesno == "n" or yesno == "N":

            #For a particular input, a particular function is called.
            #Thus, the flow of the program continues.
            
            get_input = get_regular_input()
            
            break

        
        else:
            
            print("Invalid input. Try again.\n")

            #If a correct input is not entered, the loop will keep running.

    print_order_details(get_input)
    
    apply_coupon_code(calculate_tax(*calculate_discounted_prices(*calculate_category_wise_cost(get_input)))[0])

    #Various functions are called depending on returned values of the functions.
            

    print("\nThank you for visiting!\n")

    #The end of the program.



    

if __name__ == '__main__':
    
    main()

    #The <main()> function is called in the primary iteration of the program
