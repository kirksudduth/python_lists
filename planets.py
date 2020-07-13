planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

two_planet_list = ["Uranus", "Neptune"]

planet_list.extend(two_planet_list)
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

rocky_planets = planet_list[:4]
del planet_list[-1]
