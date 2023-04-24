from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

@app.route("/")
def index():
    return redirect("/select")

@app.route("/select", methods = ["GET", "POST"])
def select():

    conn = sqlite3.connect('catalog/catalog.db')
    db = conn.cursor()
    db.execute("SELECT DISTINCT model FROM legkovye")

    models = []

    for row in db:
        models.append(row[0])

    conn.close()

    return render_template("select.html", models = models)

@app.route("/model_line")
def model_line():
    model = request.args.get("model")
    conn = sqlite3.connect('catalog/catalog.db')
    db = conn.cursor()
    db.execute("SELECT  DISTINCT model_line FROM legkovye WHERE model = :model", {'model': model})

    model_lines = []

    for row in db:
        model_lines.append(row[0])

    conn.close()

    return jsonify(model_lines)

#from here on I neded to more arguments to pass, but I knoe how to pass only one argument, thus I need to split it into several
@app.route("/model_type")
def model_type():
    argument = request.args.get("model_line")
    model = argument.split('>|<')[0]
    model_line = argument.split('>|<')[1]
    conn = sqlite3.connect('catalog/catalog.db')
    db = conn.cursor()
    db.execute("SELECT DISTINCT model_type FROM legkovye WHERE model = :model AND model_line = :model_line", {'model': model, 'model_line': model_line})

    model_types = []

    for row in db:
        model_types.append(row[0])

    conn.close()

    return jsonify(model_types)

@app.route("/date")
def date():
    argument = request.args.get("model_type")
    model = argument.split('>|<')[0]
    model_line = argument.split('>|<')[1]
    model_type = argument.split('>|<')[2]
    conn = sqlite3.connect('catalog/catalog.db')
    db = conn.cursor()
    db.execute("SELECT DISTINCT f, t FROM legkovye WHERE model = :model AND model_line = :model_line AND model_type = :model_type", {'model': model, 'model_line': model_line, 'model_type': model_type})

    dates = []

    for row in db:
        dates.append(row[0])
        dates.append(row[1])

    conn.close()

    return jsonify(dates)

@app.route("/battery")
def battery():
    argument = request.args.get("date")
    model = argument.split('>|<')[0]
    model_line = argument.split('>|<')[1]
    model_type = argument.split('>|<')[2]
    date = argument.split('>|<')[3]
    conn = sqlite3.connect('catalog/catalog.db')
    db = conn.cursor()
    db.execute("SELECT DISTINCT ae, prem, plus, econ FROM legkovye WHERE model = :model AND model_line = :model_line AND model_type = :model_type AND t > :date AND f < :date", {'model': model, 'model_line': model_line, 'model_type': model_type, 'date': date})

    battery = []

    for row in db:
        for r in row:
            if r != None:
                battery.append(r)

    conn.close()

    return jsonify(battery)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
