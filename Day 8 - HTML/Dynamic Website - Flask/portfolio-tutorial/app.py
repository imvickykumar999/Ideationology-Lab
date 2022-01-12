
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    vid = request.args.get('vid')

    if vid == None:
        vid = 'KZehm-meGMg'
    return render_template('index.html', vid=vid)

@app.errorhandler(404)
def page_not_found(e):
    return ( render_template('404.html'), 404 )

if __name__ == '__main__':
    app.run(debug=True)
