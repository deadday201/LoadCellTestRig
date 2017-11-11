#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import csv
from hx711 import Hx711
from flask import Flask, request, redirect, render_template

def cleanAndExit():
	print ("Cleaning...")
	GPIO.cleanup()
	print ("Bye")
	sys.exit()

hx = HX711(5,6)
hx.set_reading_format("LSB","MSB")
#calibrate to generate the reference unit value
hx.set_reference_unit(1)
hx.reset()
hx.tare()
dataFile = open('loadData.csv', 'w')
while True:
	try:
		val = hx.get_weight(5)
		print val
		with dataFile:
			writer = csv.writer(dataFile)
			writer.writerow(val)
		hx.power_down()
		hx.power_up()
		time.sleep(0.5)
	except (KeyboardInterrupt, SystemExit)
		cleanAndExit()
