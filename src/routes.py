# import dependences
from flask import Blueprint
from flask import jsonify
from flask import request
import json
import math

# import class models
from models import db
from models import Cities

api = Blueprint('api' , __name__)

@api.route('/load_json')
def cargar_json():
    try:
        with open('cities.json') as cities_json:
            cities = json.load(cities_json)
        for city in cities:
            query =db.insert(Cities,city)
            db.session.execute(query)
        db.session.commit()
        return jsonify({"message":"ok","cities":cities}),200
    except Exception as e:
        print('error: ', e)
        return jsonify({"message":"error"}),500

@api.route('/search')
def search():
    name = request.args.get('q')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    
    
    return [name, latitude, longitude]

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia