from flask import Flask

app = Flask(__name__)


# @app.route("/")
def index():
    return """
    <h1> HELLO </h1>
    <ul>
        <li>4</li>
        <li>5</li>
        <li>6</li>
    </ul>
    """

app.add_url_rule('/', view_func=index)

app.run(debug=True)
