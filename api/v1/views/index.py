#!/usr/bin/python3
"""index"""
from api.v1.views import app_views
from flask import jsonify
from module import storage
from module.user import User
from module.place import Place
from module.state import State
from module.city import City
from module.amenity import Amenity
from module.review import Review

classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status', methods=['GET'])
def status():
    ''' routes to status page '''
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def count():
    '''retrieves the number of each objects by type'''
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)

