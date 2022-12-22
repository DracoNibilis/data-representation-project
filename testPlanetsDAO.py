from planetsDAO import planetDAO

# test get all
addPlanet = planetDAO.create(("Mercury", 0.03, 0, "40-60 mln km"))
print("test get all")

allPlanets = planetDAO.getAll()
for planet in allPlanets:
    print(planet)
