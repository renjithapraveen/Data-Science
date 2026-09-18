"""Write a program to calculate the total trip expenditure: Calculate the hotel cost per day 
Calculate the plane cost Price of the vehicle rented during the trip"""

# Function to find hotel cost
def hotel_cost(nights):
    return 140 * nights  # $140 per night

# Function to find plane ticket cost
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0  # if the city is not listed

# Function to find rental car cost
def rental_car_cost(days):
    cost = 40 * days  # $40 per day
    if days >= 7:
        cost -= 50  # discount for 7 or more days
    elif days >= 3:
        cost -= 20  # discount for 3–6 days
    return cost

# Function to calculate total trip cost
def trip_cost(city, days, spending_money):
    total = (hotel_cost(days) +
             plane_ride_cost(city) +
             rental_car_cost(days) +
             spending_money)
    return total

# ---- Example Outputs ----
print("Cost of car rental:", rental_car_cost(5))
print("Cost of plane ride:", plane_ride_cost("Los Angeles"))
print("Cost of hotel room:", hotel_cost(7))
print("Total trip cost:", trip_cost("Los Angeles", 7, 500))
print(trip_cost("Tampa", 6, 500))
