from flask import Flask, Response, request, render_template, jsonify,redirect
from microservice1_resource import MicroService1
from flask_cors import CORS
from datetime import datetime
import json

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)

cate_cache = dict()
is_item_cache = dict()

@app.route("/api/item/<item_name>", methods=["GET"])
def get_item_by_name(item_name):

    links = []
    item_link = {"href": '/marketorders/'+item_name, "rel":"item info", "type": "GET"}
    links.append(item_link)
    rt = MicroService1.get_location_by_name(item_name)

    if rt:
        result = dict()
        result['location'] = rt
        result['links'] = links
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/item/security/<item_name>", methods=["GET"])
def get_security_name(item_name):

    links = []
    item_link = {"href": '/marketorders/'+item_name, "rel":"item security info", "type": "GET"}
    links.append(item_link)
    rt = MicroService1.get_security_by_name(item_name)

    if rt:
        result = dict()
        result['security'] = rt
        result['links'] = links
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/childstation/<location_id>", methods=["GET"])
def get_stations_by_id(location_id):

    id, name, type, station_list = MicroService1.get_stations_by_id(location_id)

    if id:
        result = dict()
        result["id"] = id
        result["name"] = name
        result["type"] = type
        result["station_list"] = station_list
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/stationparent/<station_id>", methods=["GET"])
def get_station_parent_by_id(station_id):

    item_id, item_name, security, solar_system_name, solar_system_id, constellation_name, \
    constellation_id, region_name, region_id= MicroService1.get_station_parent_by_id(station_id)

    if id:
        result = dict()
        result["id"] = item_id
        result["name"] = item_name
        result["security"] = security
        result["system_name"] = solar_system_name
        result["system_id"] = solar_system_id
        result["constellation_name"] = constellation_name
        result["constellation_id"] = constellation_id
        result["region_name"] = region_name
        result["region_id"] = region_id

        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011,debug=True)