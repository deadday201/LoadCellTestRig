#!/usr/bin/python
import RPI.GPIO as GPIO
import time
import sys
import csv
from hx711 import HX711
from flask import Flask, request, redirect, render_template

def cleanAndExit():
