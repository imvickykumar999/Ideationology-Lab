
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/index')
def index():
    name = request.args.get('name')
    return render_template('index.html', name = name)

@app.route('/')
def video():
    vid = request.args.get('vid')
    # print(vid)

    if vid == None:
        vid = '9Nk6pfep6BE'
    return render_template('video.html', vid = vid)

@app.errorhandler(404)
def page_not_found(e):
    return ( render_template('404.html'), 404 )

if __name__ == '__main__':
    app.run(debug=True)
