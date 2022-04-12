from dataparse.parse import gather_popular, search_topics
from getdata import getdata
from urllib.parse import quote_plus
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    # return index.html
    return render_template("index.html")


@app.route("/search/<query>")
async def search(query):
    try:
        c = await getdata(
            "https://medium.com/search?source=home&q=" + quote_plus(query)
        )
        ret = await search_topics(c)
        ret = {"content": ret}

        return (
            ret,
            200,
            {"Content-Type": "application/json"},
        )
    except:
        return (
            {"error": "no results found"},
            500,
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


# handle errors
@app.errorhandler(404)
def page_not_found(e):
    return "An error has occured", 404


# run app
app.run(port=80)
