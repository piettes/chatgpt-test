import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

TRANSPORTATION_FOOTPRINTS = {
    'driving': 0.43,  # kg CO2 per km driven
    'public_transport': 0.04,  # kg CO2 per km taken
    'walking': 0,  # kg CO2 per km walked or biked
}

FOOD_FOOTPRINTS = {
    'meat': 6.6,  # kg CO2 per kg of beef consumed
    'vegetarian': 2,  # kg CO2 per kg of tofu consumed
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
    'geothermal': 0.034,  # kg CO2 per kWh of geothermal power used
}

AVERAGE_DAILY_DRIVING = 13  # km per day
AVERAGE_DAILY_FOOD_CONSUMPTION = 1.5  # kg per day
AVERAGE_HOME_ENERGY_USE = 8000 / 365  # kWh per day
DAYS_IN_YEAR = 365

@app.route('/')
def home():
    return render_template('home.html')

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
    short_descs = ["This is point A", "This is point B", "This is point C", "This is point D", "This is point E",
                   "This is point F"]
    long_descs = ["This is a longer description for point A", "This is a longer description for point B",
                  "This is a longer description for point C", "This is a longer description for point D",
                  "This is a longer description for point E", "This is a longer description for point F"]
    for i in range(6):
        point = {}
        point['label'] = names[i]
        point['value'] = random.randint(1, 10)
        point['short_desc'] = short_descs[i]
        point['long_desc'] = long_descs[i]
        points.append(point)
    return jsonify({'data': points})

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve user inputs from form
    transportation = request.form.get('transportation')
    food = request.form.get('food')
    home_energy = request.form.get('home_energy')

    # Check if all inputs are valid
    if not all([transportation, food, home_energy]):
        return render_template('error.html')

    # Calculate carbon footprint based on user inputs
    transportation_footprint = TRANSPORTATION_FOOTPRINTS.get(transportation, 0)
    food_footprint = FOOD_FOOTPRINTS.get(food, 0)
    home_energy_footprint = HOME_ENERGY_FOOTPRINTS.get(home_energy, 0)

    # Calculate total carbon footprint per year
    total_footprint = (transportation_footprint * AVERAGE_DAILY_DRIVING +
                       food_footprint * AVERAGE_DAILY_FOOD_CONSUMPTION +
                       home_energy_footprint * AVERAGE_HOME_ENERGY_USE) / 1000
    carbon_footprint_per_year = total_footprint * DAYS_IN_YEAR

    # This assumes an average of 13 km driving per day, 3 km walking per day, 1.5 kg of food consumed per day,
    # and an average daily home energy use of 21.92 kWh (calculated by dividing 8000 kWh by 365 days).
    # The days_in_year variable is set to 365. The total_footprint is divided by 1000 to convert it to metric tons of CO2 equivalent,
    # and then multiplied by days_in_year to get the carbon_footprint_per_year.
    # Calculate total carbon footprint

    # total_footprint = transportation_footprint * 10 + food_footprint * 2 + home_energy_footprint * 1000 # assuming 10 km per day, 2 meals per day, and 1000 kWh per year

    # Render template with results
    return render_template('results.html', total_footprint=carbon_footprint_per_year, transportation_footprint=transportation_footprint * AVERAGE_DAILY_DRIVING, food_footprint=food_footprint * AVERAGE_DAILY_FOOD_CONSUMPTION, home_energy_footprint=home_energy_footprint * AVERAGE_HOME_ENERGY_USE)

@app.errorhandler(400)
def bad_request(e):
    return render_template('error.html'), 400

if __name__ == '__main__':
    app.run(debug=True)

