from flask import Flask, render_template, abort

import data

app = Flask(__name__)

@app.route("/")
def render_index():
    output = render_template('index.html',
                             title=data.title,
                             subtitle=data.subtitle,
                             description=data.description,
                             departures=data.departures,
                             tours=data.tours)
    return output

@app.route("/departures/<departure>/")
def render_departure(departure):
    if departure not in data.departures:
        abort(404)

    choosed_tours = []
    for id, t in data.tours.items():
        if t['departure'] == departure:
            t['id'] = id
            choosed_tours.append(t)

    output = render_template('departure.html', departure=departure, departures=data.departures, tours=choosed_tours)
    return output

@app.route("/tours/<int:id>/")
def render_tour(id):
    if id not in data.tours:
        abort(404)

    output = render_template('tour.html', tour=data.tours[id], departures=data.departures)
    return output


if __name__ == '__main__':
    app.run()