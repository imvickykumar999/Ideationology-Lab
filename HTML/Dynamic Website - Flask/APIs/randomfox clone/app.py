
from flask import Flask, jsonify, request, render_template, send_from_directory
import random
app = Flask(__name__)


@app.route('/static/<filename>')
def static_jpg(filename):
    return send_from_directory("static", filename)


@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):
		i = request.args.get('i')

		if i == None:
			num = random.randint(1, 10)
		else:
			num = i
		return render_template('index.html', num=num)


@app.route('/random/', methods = ['GET'])
def static_json():
	num = random.randint(1, 10)
	return jsonify({"image":f"/static/{num}.jpg","link":f"/?i={num}"})


if __name__ == '__main__':
	app.run(debug = True)
