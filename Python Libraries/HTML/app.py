
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    import requests
    import json

    link = "https://api.imgflip.com/get_memes"
    f = requests.get(link)
    d = f.text
    res = json.loads(d)
    v = res['data']
    mv = list(v.values())[0]

    return render_template('index.html', mv=mv)


@app.route('/news')
def news():

    from bs4 import BeautifulSoup
    import requests

    url = 'https://inshorts.com/en/read/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    heading = soup.findAll('span', attrs = {'itemprop':'headline'})
    imagex = soup.findAll('div', attrs = {'class':'news-card-image'})
    bodyx = soup.findAll('div', attrs = {'itemprop':'articleBody'})
    readmore = soup.findAll('div', attrs = {'class':'read-more'})

    lst = [heading, imagex, bodyx, readmore]
    return render_template('news.html',
                            lst=lst
                          )


@app.errorhandler(404)
def page_not_found(e):
    return ( render_template('404.html'), 404 )

if __name__ == '__main__':
    app.run(debug=True)
