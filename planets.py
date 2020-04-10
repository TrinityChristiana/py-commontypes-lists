# **************************** Challenge: Planet List ****************************
print("************Planet List *************************")
"""
Author: Trinity Terry
pyrun: python planets.py
"""
planet_list = ["Mercury", "Mars"]

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(["Uranus", "Neptune"])

# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_planets = planet_list[0:4]
print("planet_list:", planet_list)
print("rocky_planets:", rocky_planets)

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[-1:]
print("planet_list:", planet_list)

print("")
# **************************** Challenge: Iterating over planets ****************************
print("************Iterating over planets *************************")

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

# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
for planet in planet_list:
    travels = []
    for journey in spacecraft:
        if journey[1] == planet:
            travels.append(journey[0])

    print(f"Spacecrafts that went to {planet}:",
          "none" if len(travels) == 0 else travels)