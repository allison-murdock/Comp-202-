#AUTHOR: ALLISON MURDOCK
#MCGILL ID: 261009978
from math import * 

PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True

def get_pizza_area(diameter):
    '''
    '''
    area = pi*(diameter / 2)**2
    print(area)

def get_fair_quantity(diameter1 , diameter2):
    '''
    '''   
    area1 = pi*(diameter1 / 2)**2
    
    area2 = pi*(diameter2 / 2)**2
    
    if area1 < area2:
    
        i = 1
        while area1 < area2:
            if (i* area1) >= area2:
                return i
            else:
                i +=1
            
    elif area2 < area1:
        
        i = 1
        while area2 < area1:
            if (i* area2) >= area1:
                return i
            else:
                i +=1
                
def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    '''
    '''
    if d_large == -1:
        return round((d_small ** 0.5)*(c_small * c_large * n_small)/c_small, 2) 
    if d_small == -1:
        return round((d_large ** 0.5)*(n_small * c_large * c_small)/n_small * c_large, 2)
    if c_large == -1:
        return round(c_small * d_large ** 2/d_small ** 2 * n_small, 2)
    if c_small == -1:
        return round(c_large * d_small ** 2 * n_small/d_large ** 2, 2)
    if n_small == -1:
        return round(c_small * d_large ** 2/d_small ** 2 * c_large, 2)
    
    
    
def get_pizza_cake_cost(base_diameter, height_per_level):
    '''
    area_pizza = pi*(base_diameter / 2)**2
    
    current_diameter = 1
    
    total_area = 0
   
    while current_diameter <= base_diameter:
        area_pizza = pi*(current_diameter / 2)**2
        
        total_area += area_pizza
        
        current_diameter += 1
        
    cake_cost = (total_area * height_per_level * PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED)   
    return round(cake_cost, 2)             
        
        '''
    
    current_diameter = base_diameter
    total_area = 0
    
    while current_diameter >= 1:
        area_pizza = pi*(current_diameter / 2)**2
        total_area += area_pizza
        current_diameter -= 1
        
    cake_cost = (total_area * height_per_level * PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED)   
    return round(cake_cost, 2)

def get_pizza_poutine_cost(diameter, height):
    '''
    '''
    volume = (pi*((diameter / 2)** 2)* height)
    
    total_cost = volume * PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    
    return round(total_cost, 2)

def display_welcome_menu():
    '''
    '''
    print("Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.","\n",
          "Please choose an option:","\n","A. Special Orders","\n","B. Formula Mode"
          "\n","C. Quantity Mode") 

def special_orders():
    '''
    '''
    prompt_cake_or_poutine = str(input("Would you like the cake or poutine? "))
    
    if prompt_cake_or_poutine == "cake":
        base_diameter = int(input("Enter diameter: "))
        height_per_level = float(input("Enter height: "))   
        
        cake_cost = get_pizza_cake_cost(base_diameter, height_per_level)  
        
        prompt_extra = str(input("Do you want the guacamole? "))
        
        if prompt_extra == "yes": 
            print("The cost is", (cake_cost + SPECIAL_INGREDIENT_COST))
        
        else:
            print("The cost is $", round(cake_cost, 2))
    else:       
        diameter = int(input("Enter diameter: "))
        height = float(input("Enter height: "))
        
        poutine_cost = get_pizza_poutine_cost(diameter, height)
        
        prompt_extra = str(input("Do you want the guacamole? "))
        
        if prompt_extra == "yes": 
            print("The cost is", (poutine_cost + SPECIAL_INGREDIENT_COST))
        
        else:
            print("The cost is $", round(poutine_cost, 2))
            
def quantity_mode():
    '''
    '''
    diameter1 = float(input("Enter diameter 1: "))
    diameter2 = float(input("Enter diameter 2: "))
    
    get_fair_quantity(diameter1 , diameter2)
    print("You should buy", get_fair_quantity(diameter1 , diameter2), "pizzas")
     

def formula_mode():
    d_large = float(input("Enter large diameter: "))
    d_small = float(input("Enter small diameter: "))
    c_large = float(input("Enter large cost: "))
    c_small = float(input("Enter small cost: "))
    n_small = float(input("Enter number of small pizzas: "))
    
    print("The missing value is:", pizza_formula(d_large, d_small, c_large, c_small, n_small))
    
def run_pizza_calculator():
    '''
    '''
    display_welcome_menu()
    prompt_order_choice = str(input("Your choice: "))
    
    if prompt_order_choice == "A":
        print(special_orders())
    
    elif prompt_order_choice == "B":
        print((formula_mode()))
    
    elif prompt_order_choice == "C":
        print(quantity_mode())
    else:
        print("invalid input, please try again.")
    
        