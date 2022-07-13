
from flask import Flask, jsonify, request

app = Flask(__name__)
lst = []

@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})


@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):

	lst.append({num : num**2})
	return jsonify({'data': lst})


if __name__ == '__main__':
	app.run(debug = True)
