#Created by: Alireza Teimoori

#Created on: 6 Oct 2017
#Created for: ICS3UR-1

#Lesson: Asssignment 3b

# This program calculates pizza price 
# user is allowed to choose from 2 size
# of pizzas and 1 to 4 toppings
# app calculates sub total, HST, Final Total


import ui

### Variables and Constants

pizza_size = None
#print(pizza_size)

topping_number = 0
#print(topping_number)

HST = 1.13

sub_total = 0
added_hst = 0
final_total = 0

pizza_cost = 0
topping_cost = 0

if pizza_size == 'Large':
    pizza_cost = 6
elif pizza_size == 'Extra Large':
    pizza_cost = 10


def large_button_touch_up_inside(sender):
    #changes pizza_size variable to Large
    
    global pizza_size
    global pizza_cost
    pizza_size = 'Large'
    pizza_cost = 6
    #print(pizza_size)
    
    view['checking_label'].text = "Your pizza is "+ pizza_size 
    
def extra_large_button_touch_up_inside(sender):
    #changes pizza_size variable to Extra Large
    
    global pizza_size
    global pizza_cost
    pizza_size = 'Extra Large'
    pizza_cost = 10
    #print(pizza_size)
    
    view['checking_label'].text = "Your pizza is "+ pizza_size 
    
def confirm_touch_up_inside(sender):
    # changes topping_number value to what ever user has entred
    
    global topping_number
    topping_number = int(view['topping_textfield'].text)
    #print(topping_number)
    if 0 <= topping_number <= 4:
        view['checking_label'].text = "Your pizza is "+ pizza_size +" with "+str(topping_number)+" topping(s)"
    else:view['checking_label'].text = "You can only choose a number between 0 and 4"
    
def calculate_button_touch_up_inside(sender):
    global sub_total
    global added_hst
    global final_total
    
    if 0 < topping_number <= 4 :
        global topping_cost
        topping_cost = 1+((topping_number-1)*0.75)
        
    elif topping_number == 0:
        topping_cost = 0
        
    sub_total = pizza_cost+topping_cost
    added_hst = (HST*(sub_total))-sub_total
    final_total = HST*(sub_total)
    
    view['sub_total_answer_label'].text = "${:,.2f}".format(sub_total)
    view['hst_answer_label'].text = "${:,.2f}".format(added_hst)
    view['final_total_answer_label'].text = "${:,.2f}".format(final_total)



view = ui.load_view()
view.present('sheet')
