from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

'''
@app.route('/graph')
def graph():
    return render_template('graph.html')   


# Endpoint that returns data in JSON format
@app.route('/data')
def get_data():
    
    data = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'values': [100, 200, 300, 400, 500, 600],
        'descriptions': ['January data', 'February data', 'March data', 'April data', 'May data', 'June data']
   
    }
    
    return jsonify(data)

@app.route('/points')
def get_points():
    points = []
    names = ["Point A", "Point B", "Point C", "Point D", "Point E", "Point F"]
    short_descs = ["This is point A", "This is point B", "This is point C", "This is point D", "This is point E", "This is point F"]
    long_descs = ["This is a longer description for point A", "This is a longer description for point B", "This is a longer description for point C", "This is a longer description for point D", "This is a longer description for point E", "This is a longer description for point F"]
    for i in range(6):
        point = {}
        point['label'] = names[i]
        point['value'] = random.randint(1, 10)
        point['short_desc'] = short_descs[i]
        point['long_desc'] = long_descs[i]
        points.append(point)
    return jsonify({'data': points})
'''


# Constants
KM_PER_DAY = 10
MEALS_PER_DAY = 2
KWH_PER_YEAR = 1000

# Carbon footprint values
TRANSPORTATION_FOOTPRINTS = {
    'driving': 0.43,  # kg CO2 per km driven
    'public_transport': 0.04,  # kg CO2 per km taken
    'walking': 0  # kg CO2 per km walked or biked
}

FOOD_FOOTPRINTS = {
    'meat': 6.6,  # kg CO2 per kg of beef consumed
    'vegetarian': 2  # kg CO2 per kg of tofu consumed
}

HOME_ENERGY_FOOTPRINTS = {
    'electricity': 0.527,  # kg CO2 per kWh of electricity used
    'natural_gas': 0.184,  # kg CO2 per kWh of natural gas used
    'coal': 1.001,  # kg CO2 per kWh of coal used
    'petroleum': 0.717,  # kg CO2 per kWh of petroleum used
    'nuclear': 0.018,  # kg CO2 per kWh of nuclear power used
    'wind': 0.012,  # kg CO2 per kWh of wind power used
    'solar': 0.055,  # kg CO2 per kWh of solar power used
    'hydro': 0.018,  # kg CO2 per kWh of hydro power used
    'biomass': 0.230,  # kg CO2 per kWh of biomass power used
    'geothermal': 0.034  # kg CO2 per kWh of geothermal power used
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/graph')
def graph():
    # Create data for graph
    labels = ['Transportation', 'Food', 'Home Energy']
    sizes = [np.random.randint(5, 50), np.random.randint(5, 50), np.random.randint(5, 50)]
    colors = ['yellowgreen', 'gold', 'lightskyblue']

    # Plot graph
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    # Save graph to file
    filename = 'static/images/graph.png'
    fig.savefig(filename)

    # Render template with graph
    return render_template('graph.html', graph=filename)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve user inputs from form
    transportation = request.form['transportation']
    food = request.form['food']
    home_energy = request.form['home_energy']

    # Calculate carbon footprint based on user inputs
    try:
        transportation_footprint = TRANSPORTATION_FOOTPRINTS[transportation]
    except KeyError:
        return render_template('error.html', message="Invalid transportation option")

    try:
        food_footprint = FOOD_FOOTPRINTS[food]
    except KeyError:
        return render_template('error.html', message="Invalid food option")

    try:
        home_energy_footprint = HOME_ENERGY_FOOTPRINTS[home_energy]
    except KeyError:
        return render_template('error.html', message="Invalid home energy option")

    # Calculate total carbon footprint
    total_footprint = (
        transportation_footprint * KM_PER_DAY
        + food_footprint * MEALS_PER_DAY
        + home_energy_footprint * KWH_PER_YEAR)

    # Render template with results
    return render_template('results.html', total_footprint=total_footprint)

if __name__ == '__main__':
    app.run(debug=True)
