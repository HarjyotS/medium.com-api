from dataparse.parse import gather_popular, search_topics
from getdata import getdata
from urllib.parse import quote_plus
import json
from flask import Flask


app = Flask(__name__)


@app.route("/")
async def hello_world():
    return "Hello, World!"


@app.route("/search/<query>")
async def search(query):
    c = await getdata("https://medium.com/search?source=home&q=" + quote_plus(query))
    ret = await search_topics(c)
    ret = {"content": ret}

    return (
        ret,
        200,
        {"Content-Type": "application/json"},
    )


@app.route("/popular")
async def popular():
    c = await getdata("https://medium.com/topic/popular")
    ret = await gather_popular(c)
    ret = {"content": ret}

    return (
        ret,
        200,
        {"Content-Type": "application/json"},
    )


# run app
app.run(port=8080)
