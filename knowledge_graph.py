# KNOWLEDGE GRAPH DATA

travel_graph = {

    "Hyderabad": {

        "tourist_spots": [
            "Charminar",
            "Golconda Fort",
            "Hussain Sagar"
        ],

        "famous_foods": [
            "Hyderabadi Biryani",
            "Irani Chai"
        ],

        "transport_modes": [
            "Metro",
            "Bus",
            "Cab"
        ]
    },

    "Bengaluru": {

        "tourist_spots": [
            "Cubbon Park",
            "Lalbagh",
            "Bangalore Palace"
        ],

        "famous_foods": [
            "Masala Dosa",
            "Filter Coffee"
        ],

        "transport_modes": [
            "Metro",
            "Bus",
            "Cab"
        ]
    },

    "Visakhapatnam": {

        "tourist_spots": [
            "RK Beach",
            "Kailasagiri",
            "Yarada Beach"
        ],

        "famous_foods": [
            "Seafood",
            "Fish Curry"
        ],

        "transport_modes": [
            "Bus",
            "Cab",
            "Train"
        ]
    }
}


# DISPLAY FUNCTION

def display_graph(city_name):

    if city_name not in travel_graph:
        print("City not found in Knowledge Graph")
        return

    city_info = travel_graph[city_name]

    print("\nKNOWLEDGE GRAPH FOR", city_name)

    print("\nTourist Places:")

    for location in city_info["tourist_spots"]:
        print("-", location)

    print("\nFood Recommendations:")

    for item in city_info["famous_foods"]:
        print("-", item)

    print("\nTransport Options:")

    for vehicle in city_info["transport_modes"]:
        print("-", vehicle)


# SAMPLE EXECUTION

selected_city = "Hyderabad"

display_graph(selected_city)


print("\nSOFTWARE / TOOLS USED FOR KNOWLEDGE GRAPHS")

tools_list = [
    "Neo4j",
    "RDFLib (Python)",
    "Protégé",
    "GraphDB",
    "NetworkX"
]

for number, tool in enumerate(tools_list, start=1):
    print(f"{number}. {tool}")
