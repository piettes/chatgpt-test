from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

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


@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve user inputs from form
    transportation = request.form['transportation']
    food = request.form['food']
    home_energy = request.form['home_energy']

    # Calculate carbon footprint based on user inputs
    if transportation == 'driving':
        transportation_footprint = 0.43 # kg CO2 per km driven
    elif transportation == 'public_transport':
        transportation_footprint = 0.04 # kg CO2 per km taken
    elif transportation == 'walking':
        transportation_footprint = 0 # kg CO2 per km walked or biked

    if food == 'meat':
        food_footprint = 6.6 # kg CO2 per kg of beef consumed
    elif food == 'vegetarian':
        food_footprint = 2 # kg CO2 per kg of tofu consumed

    if home_energy == 'electricity':
        home_energy_footprint = 0.527  # kg CO2 per kWh of electricity used
    elif home_energy == 'natural_gas':
        home_energy_footprint = 0.184  # kg CO2 per kWh of natural gas used
    elif home_energy == 'coal':
        home_energy_footprint = 1.001  # kg CO2 per kWh of coal used
    elif home_energy == 'petroleum':
        home_energy_footprint = 0.717  # kg CO2 per kWh of petroleum used
    elif home_energy == 'nuclear':
        home_energy_footprint = 0.018  # kg CO2 per kWh of nuclear power used
    elif home_energy == 'wind':
        home_energy_footprint = 0.012  # kg CO2 per kWh of wind power used
    elif home_energy == 'solar':
        home_energy_footprint = 0.055  # kg CO2 per kWh of solar power used
    elif home_energy == 'hydro':
        home_energy_footprint = 0.018  # kg CO2 per kWh of hydro power used
    elif home_energy == 'biomass':
        home_energy_footprint = 0.230  # kg CO2 per kWh of biomass power used
    elif home_energy == 'geothermal':
        home_energy_footprint = 0.034  # kg CO2 per kWh of geothermal power used
    else:
        print("Invalid input. Please enter a valid energy source.")
        home_energy_footprint = 0

    # Set average values
    average_daily_driving = 13  # km per day
    # average_daily_walking = 3  # km per day
    average_daily_food_consumption = 1.5  # kg per day
    average_home_energy_use = 8000 / 365  # kWh per day
    days_in_year = 365

    # Calculate total carbon footprint per year
    total_footprint = (transportation_footprint * average_daily_driving +
                        # walking_footprint * average_daily_walking +
                        food_footprint * average_daily_food_consumption +
                        home_energy_footprint * average_home_energy_use) / 1000
    carbon_footprint_per_year = total_footprint * days_in_year

    # This assumes an average of 13 km driving per day, 3 km walking per day, 1.5 kg of food consumed per day,
    # and an average daily home energy use of 21.92 kWh (calculated by dividing 8000 kWh by 365 days).
    # The days_in_year variable is set to 365. The total_footprint is divided by 1000 to convert it to metric tons of CO2 equivalent,
    # and then multiplied by days_in_year to get the carbon_footprint_per_year.
    # Calculate total carbon footprint

    #total_footprint = transportation_footprint * 10 + food_footprint * 2 + home_energy_footprint * 1000 # assuming 10 km per day, 2 meals per day, and 1000 kWh per year

    # Render template with results
    return render_template('results.html', total_footprint=carbon_footprint_per_year)

if __name__ == '__main__':
    app.run(debug=True)
