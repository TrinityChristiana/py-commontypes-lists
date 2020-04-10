planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

rocky_planets = planet_list[0:4]
# print("planet_list:", planet_list)
# print("rocky_planets:", rocky_planets)
del planet_list[-1:]
# print("planet_list:", planet_list)

spacecraft = [
    ("Cassini", "Saturn"),
    ("Pioneer", "Saturn"),
    ("Voyager", "Saturn"),
    ("Voyager", "Neptune"),
    ("Voyager", "Uranus"),
    ("Viking", "Mars"),
    ("InSight", "Mars"),
    ("Juno", "Jupiter"),
    ("Pioneer", "Jupiter"),
    ("Mariner", "Mercury"),
    ("Messenger", "Mercury"),
    ("Venera", "Venus"),
]

for planet in planet_list:
    travels = []
    for journey in spacecraft:
        if journey[1] == planet:
            travels.append(journey[0])

    print(f"Spacecrafts that went to {planet}:", "none" if len(travels) == 0 else travels)
