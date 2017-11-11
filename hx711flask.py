#!/usr/bin/python
import RPI.GPIO as GPIO
import time
import sys
import csv
from hx711 import HX711
from flask import Flask, request, redirect, render_template

def cleanAndExit():
	print ("cleaning...")
	GPIO.cleanup()
	print ("bye")
	sys.exit()

hx = HX711(5,6)
hx.set_reading_format("LSB", "MSB")
#calibrate to generate the reference unit value
hx.set_reference_unit(1)
hx.reset()
hx.tare()
datafile = open('loadData.csv', 'w')
app = Flask(__name__)
@app.route('/')
def hiThere():
	return render_template('index.html')
