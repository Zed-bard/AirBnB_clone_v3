#!/usr/bin/python3
"""places_amenities.py"""
from flask import abort, jsonify, make_response, request
from models import storage
from models.amenity import Amenity
from models.place import Place
from api.v1.views import app_views


@app_views.route('/places/<string:place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def get_place_amenities(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)

    if storage.__class__.__name__ == 'DBStorage':
        amenities = [amenity.to_dict() for amenity in place.amenities]
    else:
        amenities = [storage.get("Amenity", amenity_id).to_dict()
                     for amenity_id in place.amenity_ids]

    return jsonify(amenities)


@app_views.route('/places/<string:place_id>/amenities/<string:amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    """Deletes an Amenity object from a Place"""
    place = storage.get("Place", place_id)
    amenity = storage.get("Amenity", amenity_id)
    if place is None or amenity is None:
        abort(404)

    if amenity not in place.amenities:
        abort(404)

    place.amenities.remove(amenity)
    place.save()
    return jsonify({}), 200


@app_views.route('/places/<string:place_id>/amenities/<string:amenity_id>',
                 methods=['POST'], strict_slashes=False)
def post_place_amenity(place_id, amenity_id):
    """Links an Amenity object to a Place"""
    place = storage.get("Place", place_id)
    amenity = storage.get("Amenity", amenity_id)
    if place is None or amenity is None:
        abort(404)

    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200

    place.amenities.append(amenity)
    place.save()
    return jsonify(amenity.to_dict()), 201
