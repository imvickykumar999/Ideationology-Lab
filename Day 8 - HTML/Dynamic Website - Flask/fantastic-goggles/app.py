
from flask import Flask, render_template
app = Flask(__name__)

# print(app)

@app.route('/')
def index():
    # url = 'https://www.youtube.com/watch?v=MUMCZZl9QCY'
    name = 'MUMCZZl9QCY'
    # name = request.args.get('name')
    return render_template('index.html', vid = name)
#
@app.errorhandler(404)
def page_not_found(e):
    return ( render_template('404.html'), 404 )


if __name__ == '__main__':
    app.run(debug=True)
