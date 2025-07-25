import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'
}

@app.route("/")
@app.route("/bbc") #no matter how many routes i write they all will follow this function only
def bbc():
    return get_news('bbc')

@app.route("/cnn")
def cnn():
    return get_news('cnn')

@app.route("/fox")
def fox():
    return get_news('fox')

@app.route("/iol")
def iol():
    return get_news('iol')

def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """
    <html>
        <body>
            <h1>{0} Headlines</h1>
            <b>{1}</b><br/>
            <i>{2}</i><br/>
            <p>{3}</p><br/>
        </body>
    </html>
    """.format(
        publication.upper(),
        first_article.get("title"),
        first_article.get("published"),
        first_article.get("summary")
    )

if __name__ == "__main__":
    app.run(port=5000, debug=True)
