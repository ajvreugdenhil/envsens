# -*- coding: utf-8 -*-
# Description: Custom environment sensor plugin
# Author: Bangedaon | Arjan Vreugdenhil

from bases.FrameworkServices.SimpleService import SimpleService
import serial
import json

ORDER = [
    'temperature',
    'humidity'
]

CHARTS = {
  "temperature": {
    'options': [None, "Temperature", "Celcius", "envsens", "envsens.temp", "line"],
    'lines': [
      ["temperature_0", "temperature", "absolute", 1, 100]
    ]},
  "humidity": {
    'options': [None, "Humidity", "%", "envsens", "envsens.humd", "line"],
    'lines': [
      ["humidity_0", "humidity", "absolute", 1, 100]
    ]}
}

baudRate = 9600

class Service(SimpleService):
    def __init__(self, configuration=None, name=None):
        SimpleService.__init__(self, configuration=configuration, name=name)
        self.order = ORDER
        self.definitions = CHARTS
        self.c = None
        for i in range(64):
            if self.c is None:
                try:
                    port = '/dev/ttyUSB' + str(i)
                    self.c = serial.Serial(port, baudRate)
                except:
                    pass

    def get_data(self):
        data = dict()
        if self.c is not None:
            self.c.flushInput()
            self.c.flushOutput()
            try:
                self.c.write('\x41') # A
                response = self.c.readline().decode("utf-8").strip()
                try:
                  json_object = json.loads(response)
                except:
                  self.error("Json Parsing Failed")
                data['temperature_0'] = json_object["Temperature"] * 100
                data['humidity_0'] = json_object["Humidity"] * 100
            except:
                self.error("An unexpected error occurred")
                return None
        return data or None
