import math


# TRAVEL DATABASE

travel_db = {

    "Hyderabad": {

        "spots": {

            "history": [
                "Charminar",
                "Golconda Fort",
                "Salar Jung Museum"
            ],

            "food": [
                "Famous Biryani Spots",
                "Irani Cafe",
                "Street Food Market"
            ],

            "nature": [
                "Hussain Sagar Lake",
                "NTR Garden"
            ],

            "shopping": [
                "Laad Bazaar",
                "Inorbit Mall"
            ]
        },

        "foods": {

            "veg": [
                "Veg Biryani",
                "South Indian Meals",
                "Paneer Curry"
            ],

            "non-veg": [
                "Hyderabadi Chicken Biryani",
                "Mutton Biryani",
                "Kebab"
            ]
        },

        "hotel_prices": {
            "low": 1000,
            "medium": 2500,
            "high": 5000
        },

        "travel_cost": 500
    },

    "Visakhapatnam": {

        "spots": {

            "nature": [
                "RK Beach",
                "Kailasagiri",
                "Yarada Beach"
            ],

            "history": [
                "Submarine Museum",
                "Victory at Sea Memorial"
            ],

            "food": [
                "Seafood Restaurants",
                "Beach Snacks"
            ],

            "shopping": [
                "CMR Central Mall"
            ]
        },

        "foods": {

            "veg": [
                "Vegetable Meals",
                "Dosa"
            ],

            "non-veg": [
                "Fish Curry",
                "Prawns Fry"
            ]
        },

        "hotel_prices": {
            "low": 1200,
            "medium": 3000,
            "high": 5500
        },

        "travel_cost": 600
    },

    "Bengaluru": {

        "spots": {

            "nature": [
                "Cubbon Park",
                "Lalbagh Botanical Garden"
            ],

            "history": [
                "Bangalore Palace"
            ],

            "food": [
                "Food Street",
                "South Indian Restaurants"
            ],

            "shopping": [
                "Commercial Street",
                "UB City Mall"
            ]
        },

        "foods": {

            "veg": [
                "Idli",
                "Masala Dosa"
            ],

            "non-veg": [
                "Chicken Meals",
                "Biryani"
            ]
        },

        "hotel_prices": {
            "low": 1500,
            "medium": 3500,
            "high": 6000
        },

        "travel_cost": 700
    }
}


# MAIN PLANNER FUNCTION

def create_trip(city, budget, total_days,
                preference, food_choice):

    if city not in travel_db:
        print("Sorry! City not available.")
        return

    data = travel_db[city]

    print("\nAI TRAVEL PLAN")
    print("Destination:", city)
    print("Budget: ₹", budget)
    print("Days:", total_days)
    print("Interest:", preference)
    print("Food Preference:", food_choice)

    # HOTEL SELECTION

    if budget < 5000:
        room_type = "low"

    elif budget < 10000:
        room_type = "medium"

    else:
        room_type = "high"

    stay_cost = (
        data["hotel_prices"][room_type]
        * total_days
    )

    local_transport = (
        data["travel_cost"]
        * total_days
    )

    meal_per_day = 400
    total_meal_cost = meal_per_day * total_days

    selected_places = []

    # ADD PLACES BASED ON INTEREST

    if preference in data["spots"]:

        for place in data["spots"][preference]:
            selected_places.append(place)

    # ADD EXTRA PLACES

    if len(selected_places) < total_days:

        for section, values in data["spots"].items():

            for location in values:

                if location not in selected_places:
                    selected_places.append(location)

    # FOOD SUGGESTIONS

    suggested_food = data["foods"].get(
        food_choice.lower(),
        []
    )

    # TOTAL EXPENSE

    final_cost = (
        stay_cost +
        local_transport +
        total_meal_cost
    )

    print("\nRecommended Places:")

    for item in selected_places:
        print("-", item)

    print("\nRecommended Food:")

    for food in suggested_food:
        print("-", food)

    print("\nHotel Category Selected:", room_type)

    print("\nEstimated Cost:")
    print("Hotel Cost     : ₹", stay_cost)
    print("Transport Cost : ₹", local_transport)
    print("Food Cost      : ₹", total_meal_cost)
    print("Total Cost     : ₹", final_cost)

    if final_cost > budget:
        print("\nWarning: Budget may not be sufficient.")

    else:
        print("\nTrip fits within budget.")

    print("\nPERSONALIZED TOUR PLAN")

    trip_index = 0

    daily_places = math.ceil(
        len(selected_places) / total_days
    )

    for current_day in range(1, total_days + 1):

        print("\nDay", current_day)

        counter = 0

        while counter < daily_places:

            if trip_index < len(selected_places):

                print(
                    "- Visit",
                    selected_places[trip_index]
                )

                trip_index += 1

            counter += 1

        if suggested_food:
            print("- Try:", suggested_food[0])


# USER INPUT SECTION

print("AI TRAVEL PLANNER")

city_name = input(
    "Enter destination city "
    "(Hyderabad/Visakhapatnam/Bengaluru): "
)

trip_budget = int(
    input("Enter budget: ₹")
)

number_of_days = int(
    input("Enter number of days: ")
)

user_interest = input(
    "Enter interest "
    "(history/food/nature/shopping): "
).lower()

food_type = input(
    "Food preference (veg/non-veg): "
).lower()

create_trip(
    city_name,
    trip_budget,
    number_of_days,
    user_interest,
    food_type
)
