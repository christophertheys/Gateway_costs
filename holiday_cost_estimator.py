# Holiday Away
# This program will output the cost of the selected category from the user. There are four separate functions
print("\t \t \t This is the getaway cost estimator \n".upper())
print(" \t Input the number to make the selection \n"
      "Option 1 = hotel cost \n"
      "Option 2 = plane cost \n"
      "Option 3 = car rental \n"
      "Option 4 =  total hotel cost \n")
user_input_selection = int(input("Select the option of your choice : \n"))


def hotel(price, nights):
    total_cost = price * nights
    return hotel_stay_description + "$" + str(total_cost)


def plane(price, distance):
    total_cost = price * distance
    return plane_cost_description + "$" + str(total_cost)


def car(price, days):
    total_cost = price * days
    return car_rental_description + "$" + str(total_cost)


def holiday(hotel, plane, car):
    total_holiday_cost = hotel + plane + car
    return holiday_cost_description + "$" + str(total_holiday_cost)


if user_input_selection == 1:
    hotel_stay_description = "The total cost of the hotel cost is equal to : "
    rate = 1500
    period = 3
    hotel_cost = hotel(rate, period)
    print(hotel_cost)

if user_input_selection == 2:
    plane_cost_description = "The cost of the flight is equal to : "
    print("Destinations : \n"
          "London = LND \n"
          "New York = NYC \n"
          "Dubai = DXB \n"
          "Tokyo = TKO \n"
          "Doha = DHA \n")
    destination_input = input("Select which city to fly to by entering the characters of the destination : ".upper())
    if destination_input == "LND":
        distance = 1200
        price = 1.5
        plane_cost = plane(distance, price)
        print(plane_cost)
    if destination_input == "NYC":
        distance = 2000
        price = 1.15
        plane_cost = plane(distance, price)
        print(plane_cost)
    if destination_input == "DXB":
        distance = 900
        price = 1.8
        plane_cost = plane(distance, price)
        print(plane_cost)
    if destination_input == "TKO":
        distance = 2360
        price = 1.25
        plane_cost = plane(distance, price)
        print(plane_cost)
    if destination_input == "DHA":
        distance = 1050
        price = 1.7
        plane_cost = plane(distance, price)
        print(plane_cost)
    if destination_input == " ":
        print("Invalid input".upper())

if user_input_selection == 3:
    car_rental_description = "The cost of the car rental for the time period stated is equal to : "
    number_of_days = int(input("Enter the number of days that the car will be rented out : "))
    price = 500
    car_rental_cost = car(price, number_of_days)
    print(car_rental_cost)

if user_input_selection == 4:
    holiday_cost_description = "Total cost of the holiday is equal to : "
    nights_stay = int(input("Enter the number of nights for the holiday trip : "))
    destination_of_holiday = 1250 * 1.5
    days_of_car_rental = int(input("Enter the number of days for the car rental : "))
    total_cost = holiday(nights_stay*1500, days_of_car_rental*500, destination_of_holiday)
    print(total_cost)
