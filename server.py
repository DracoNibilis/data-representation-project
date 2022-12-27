from flask import Flask, jsonify, request, abort
from planetDAO import planetsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/planets"
@app.route('/planets')
def getAll():
    results = planetsDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/planets/<int:id>')
def findById(id):
    foundPlanet = planetsDAO.findByID(id)
    return jsonify(foundPlanet)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books
@app.route('/planets', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    planet = {
        "name": request.json['name'],
        "size": request.json['size'],
        "moons": request.json['moons'],
        "distance": request.json['distance']
    }
    values =(planet['name'],planet['size'],planet['moons'],planet['distance'])
    newId = planetsDAO.create(values)
    planet['id'] = newId
    return jsonify(planet)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/planets/<int:id>', methods=['PUT'])
def update(id):
    foundPlanet = planetsDAO.findByID(id)
    if not foundPlanet:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'moons' in reqJson and type(reqJson['moons']) is not int:
        abort(400)

    if 'name' in reqJson:
        foundPlanet['name'] = reqJson['name']
    if 'size' in reqJson:
        foundPlanet['size'] = reqJson['size']
    if 'moons' in reqJson:
        foundPlanet['moons'] = reqJson['moons']
    if 'distance' in reqJson:
        foundPlanet['distance'] = reqJson['distance']
    values = (foundPlanet['name'],foundPlanet['size'],foundPlanet['moons'],foundPlanet['distance'],foundPlanet['id'])
    planetsDAO.update(values)
    return jsonify(foundPlanet)
        

    

@app.route('/planets/<int:id>' , methods=['DELETE'])
def delete(id):
    planetsDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)