""" Dependencies """
from threading import Timer
import queue
import json
from IOPi import IOPi
from flask_cors import CORS
from flask import Flask, request, jsonify, json, Response

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

jsonFile = open("config_default.json", "r", encoding="utf-8")
allData = json.load(jsonFile)



################################################################
# IOPi-Objekt erstellen
bus1 = IOPi(0x20)

bus1.set_port_direction(0, 0x00)
bus1.write_port(0, 0xF)


################################################################
# Default Konfiguration
def setDefaultConfig():
    timer = 60
    currentTime = #


################################################################
# App-Routen
    # Status der Pumpe abfragen
@app.route('/api/status', methods=['GET'])
def getData():
    return jsonify(allData)


    # Einschalten der Pumpe
@app.route('/api/setOn', methods=['PUT'])
def setOn():
    bus1.write_port(0, 0x0)
    return jsonify(allData)


    # Ausschalten der Pumpe
@app.route('/api/setOff', methods=['PUT'])
def setOff():
    bus1.write_port(0, 0xF)
    return jsonify(allData)


    # neue Konfiguration erstellen
@app.route('/api/setData', methods=['PUT'])
def setData():
    global allData
    allData = request.json
    return jsonify(allData)

