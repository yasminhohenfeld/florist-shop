from flask import Flask

from controllers import flowers

app = Flask(__name__)


@app.route("/amor")
def get_amor():
    return flowers.get_flower()


app.run(port=3000)
