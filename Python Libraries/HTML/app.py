
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    a=[]
    n=3
    for i in range(1, 11):
        a.append(n*i)
        
    print(a)
    return render_template('index.html', a=a)

@app.errorhandler(404)
def page_not_found(e):
    return ( render_template('404.html'), 404 )

if __name__ == '__main__':
    app.run(debug=True)
