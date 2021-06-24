from flask import Flask, render_template, request
import tensorflow as tf 
from tensorflow import keras
from keras.models import load_model
from keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import numpy as np

app = Flask(__name__)

model = load_model('Sports73_model.h5')
@app.route('/', methods = ['GET'])
def home():
	return render_template("index.html")

@app.route('/', methods = ['POST'])
def predict():
	imagefile = request.files['imagefile']
	correct = ['.jpg', '.png', '.jpeg']
	if imagefile.filename[-4:].lower() not in correct:
		return render_template('index.html', prediction = 'Sorry file type not supported')
	imagepath = "./images/"+imagefile.filename
	imagefile.save(imagepath)

	image = load_img(imagepath, target_size = (224,224))
	image = img_to_array(image)
	image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
	image = preprocess_input(image)
	pred = np.argmax(model.predict(image))
	pred = "I think the image is of the sport "+labels[pred]

	return render_template('index.html', prediction = pred, img = imagepath)


labels = {0: 'air hockey',
 1: 'ampute football',
 2: 'archery',
 3: 'arm wrestling',
 4: 'balance beam',
 5: 'barell racing',
 6: 'baseball',
 7: 'basketball',
 8: 'billiards',
 9: 'bmx',
 10: 'bobsled',
 11: 'bowling',
 12: 'boxing',
 13: 'bull riding',
 14: 'canoe slamon',
 15: 'cricket',
 16: 'croquet',
 17: 'curling',
 18: 'fencing',
 19: 'field hockey',
 20: 'figure skating men',
 21: 'figure skating pairs',
 22: 'figure skating women',
 23: 'football',
 24: 'formula 1 racing',
 25: 'frisbee',
 26: 'giant slalom',
 27: 'golf',
 28: 'hammer throw',
 29: 'harness racing',
 30: 'high jump',
 31: 'hockey',
 32: 'horse jumping',
 33: 'horse racing',
 34: 'hurdles',
 35: 'ice climbing',
 36: 'jai alai',
 37: 'javelin',
 38: 'judo',
 39: 'lacrosse',
 40: 'luge',
 41: 'motorcycle racing',
 42: 'nascar racing',
 43: 'olympic wrestling',
 44: 'parallel bar',
 45: 'pole vault',
 46: 'polo',
 47: 'pommel horse',
 48: 'rings',
 49: 'rock climbing',
 50: 'rollerblade racing',
 51: 'rowing',
 52: 'rugby',
 53: 'sailboat racing',
 54: 'shot put',
 55: 'ski jumping',
 56: 'skydiving',
 57: 'snow boarding',
 58: 'snowmobile racing',
 59: 'speed skating',
 60: 'sumo wrestling',
 61: 'surfing',
 62: 'swimming',
 63: 'table tennis',
 64: 'tennis',
 65: 'track bicycle',
 66: 'tug of war',
 67: 'uneven bars',
 68: 'volleyball',
 69: 'water polo',
 70: 'weightlifting',
 71: 'wheelchair basketball',
 72: 'wheelchair racing'}



if __name__ == '__main__':
	app.run(debug = True, port=5000)
	#app.run(host = '0.0.0.0', port=8080)