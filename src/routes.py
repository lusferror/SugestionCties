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
def cargar_json():#this function store the cities
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
def search():#this funtion search suggestion

    # variables
    cities_array=[]
    max_dist=0;
    min_dist=0;

    # function
    try:
        name = request.args.get('q')
        latitude = float(request.args.get('latitude'))
        longitude = float(request.args.get('longitude'))
        query = db.select(Cities).where(Cities.name.like("%"+name+"%"))
        cities = db.engine.connect().execute(query)

        for citie in cities:
            citie_score=dict()
            citie_score["name"]=f'{citie.name}, {citie.admin1}, {citie.country}'
            citie_score["latitude"] = citie.lat
            citie_score["longitude"] =citie.long
            citie_score["score"] =  haversine(latitude,longitude,float(citie.lat),float(citie.long))
            if max_dist < citie_score["score"]:
                max_dist=citie_score["score"]
            if min_dist==0:
                min_dist=max_lat=citie_score["score"]
            elif min_dist > citie_score["score"]:
                min_dist = citie_score["score"]
            cities_array.append(citie_score)

        for citie in cities_array:
            citie["socore"] = round(1-(citie["score"]/max_dist),2)

        def sort_score(citie):
            return citie['score']
        
        cities_array.sort(key=sort_score)
        return jsonify({'search':cities_array}),200
    
    except Exception as e:
        print(e)
        return ('Invalid type on given arguments'),400

def haversine(lat1, lon1, lat2, lon2): #this function calculate distace between two point
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia