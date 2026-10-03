# use a named constant
# by using 2.0 as its value, it is automatically stored as a float
# because we defined it at the top level, it is available to any function
# in our program
COST_PER_HOUR = 2.0

def calculate_estimate_parking_hours(parked_minutes):
    return parked_minutes / 60

# parked_hours = ?; I need to figure out how to convert parked minutes into hours so that those
# without the ability/technology to convert the numbers themselves can still calculate their fee.

# goal of this definition is to calculate estimate parking costs and then 
# returning back a value to its system to utilize later for its main def. 
def calculate_estimate_parking_cost(parked_hours, COST_PER_HOUR):
    return round(parked_hours * COST_PER_HOUR, 2)
#you can nestle inside returns.

# define main logic of my program
# create a variable in which I will store user-entered parked hours
# a variable is a named space in memory
#def main(parked_hours):
def main():
    #parked_hours = float(input("How many hours will you have parked your car / park your car? "))
    parked_minutes = int(input("How many minutes will you have parked your car / park your car? "))
    parked_hours = calculate_estimate_parking_hours(parked_minutes)
    cost = calculate_estimate_parking_cost(parked_hours, COST_PER_HOUR)
    print(f"Your estimated parking cost is: ${cost:.2f}.")
    print(f"Your estimated parking hours are: {parked_hours:.2f} hour(s).")

 # call our function (processing)
#cost = calculate_estimate_parking_cost(parked_hours) ? I need to change due
# to the fact that my code isn't working as intended. Bugs.


#call/evoke my main function and execute the logic of the program
main()
#python campus_parking.py