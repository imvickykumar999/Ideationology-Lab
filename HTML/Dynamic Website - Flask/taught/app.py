
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    h=[]
    for i in range(1, 11):
        h.append(i*3)
    return render_template('index.html', hw=h)

@app.route('/greet')
def greet():
    return render_template('greet.html')

if __name__ == '__main__':
    app.run(debug=True)
