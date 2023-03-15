from flask import Flask, render_template, request

app = Flask(__name__)

# Define carbon footprint factors per transportation type in kg CO2 equivalent per km
@app.route('/calculate_transportation_carbon_footprint', methods=['GET', 'POST'])
def calculate_transportation_carbon_footprint(transportation_amount, transportation_type, fuel_type):
    if transportation_type == 'car':
        if fuel_type == 'gasoline':
            carbon_per_km = 0.18  # average carbon emission per km for a car running on gasoline
        elif fuel_type == 'diesel':
            carbon_per_km = 0.16  # average carbon emission per km for a car running on diesel
        else:
            carbon_per_km = 0.0  # set to 0 for invalid fuel type
    elif transportation_type == 'motorcycle':
        if fuel_type == 'gasoline':
            carbon_per_km = 0.12  # average carbon emission per km for a motorcycle running on gasoline
        elif fuel_type == 'diesel':
            carbon_per_km = 0.10  # average carbon emission per km for a motorcycle running on diesel
        else:
            carbon_per_km = 0.0  # set to 0 for invalid fuel type
    elif transportation_type == 'bus':
        if fuel_type == 'diesel':
            carbon_per_km = 0.11  # average carbon emission per km for a bus running on diesel
        else:
            carbon_per_km = 0.0  # set to 0 for invalid fuel type
    else:
        carbon_per_km = 0.0  # set to 0 for invalid transportation type

    total_carbon_footprint = float(transportation_amount) * float(carbon_per_km)

    return total_carbon_footprint

# Define carbon footprint factors per food type in kg CO2 equivalent per kg of food
CARBON_FOOTPRINT_FACTORS = {
    'beef': 27,
    'chicken': 6.9,
    'pork': 5.8,
    'lamb': 39.2,
    'fish': 3.7,
    'eggs': 4.8,
    'cheese': 13.5,
    'rice': 2.7,
    'pasta': 2.5,
    'bread': 1.4,
    'potatoes': 0.2,
    'vegetables': 0.2,
    'fruit': 0.4,
    'nuts': 2.3,
    'beans': 0.9,
    'tofu': 2.0
}

@app.route('/calculate_food_carbon_footprint', methods=['GET', 'POST'])
def calculate_food_carbon_footprint():
    form = FoodForm()
    if form.validate_on_submit():
        food_type = form.food_type.data
        weight = form.weight.data
        carbon_footprint = CARBON_FOOTPRINT_FACTORS.get(food_type) * weight / 1000
        flash(f'Your carbon footprint for {weight}g of {food_type} is {carbon_footprint:.2f} kg CO2e.', 'success')
        return redirect(url_for('calculate_food_carbon_footprint'))
    return render_template('calculate_food_carbon_footprint.html', form=form)

# Define carbon footprint factors per energy type in kg CO2 equivalent per kWh
CARBON_FOOTPRINT_FACTORS = {
    'coal': 0.91,
    'natural_gas': 0.49,
    'petroleum': 0.72,
    'nuclear': 0.02,
    'wind': 0.01,
    'solar': 0.05,
    'hydro': 0.05,
    'biomass': 0.23,
    'geothermal': 0.05
}

@app.route('/calculate_energy_carbon_footprint', methods=['GET', 'POST'])
def calculate_energy_carbon_footprint():
    form = EnergyForm()
    if form.validate_on_submit():
        energy_type = form.energy_type.data
        kwh = form.kwh.data
        carbon_footprint = CARBON_FOOTPRINT_FACTORS.get(energy_type) * kwh
        flash(f'Your carbon footprint for {kwh} kWh of {energy_type} is {carbon_footprint:.2f} kg CO2e.', 'success')
        return redirect(url_for('calculate_energy_carbon_footprint'))
    return render_template('calculate_energy_carbon_footprint.html', form=form)


# Define routes and views for transportation, food and energy use tracking
@app.route('/transport', methods=['GET', 'POST'])
def track_transport():
    if request.method == 'POST':
        amount = request.form['amount']
        transport_type = request.form['transport_type']
        carbon_footprint = calculate_transportation_carbon_footprint(amount, transport_type)
        return render_template('transport.html', carbon_footprint=carbon_footprint)
    else:
        return render_template('transport.html')

@app.route('/food', methods=['GET', 'POST'])
def track_food():
    if request.method == 'POST':
        amount = request.form['amount']
        food_type = request.form['food_type']
        carbon_footprint = calculate_food_carbon_footprint(amount, food_type)
        return render_template('food.html', carbon_footprint=carbon_footprint)
    else:
        return render_template('food.html')

@app.route('/energy', methods=['GET', 'POST'])
def track_energy():
    if request.method == 'POST':
        amount = request.form['amount']
        energy_type = request.form['energy_type']
        carbon_footprint = calculate_energy_carbon_footprint(amount, energy_type)
        return render_template('energy.html', carbon_footprint=carbon_footprint)
    else:
        return render_template('energy.html')

# Define templates for food and energy use tracking pages
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/energy')
def energy():
    return render_template('energy.html')

# Define tips for reducing carbon footprint
def get_transportation_tips():
    # Your code to retrieve tips for reducing transportation-related carbon footprint
    return [
        "Take public transportation",
        "Carpool with friends or coworkers",
        "Bike or walk to nearby destinations",
        "Purchase a hybrid or electric vehicle"
    ]

def get_food_tips():
    # Your code to retrieve tips for reducing food-related carbon footprint
    return [
        "Eat less meat and dairy products",
        "Buy locally-sourced and organic foods",
        "Avoid processed and packaged foods",
        "Reduce food waste by planning meals and composting"
    ]

def get_energy_tips():
    # Your code to retrieve tips for reducing energy-related carbon footprint
    return [
        "Switch to energy-efficient light bulbs",
        "Use a programmable thermostat",
        "Install solar panels or wind turbines",
        "Unplug electronics when not in use"
    ]

# Define routes and views for carbon footprint tracking and tips
@app.route('/index2', methods=['GET', 'POST'])
def index2():
    transportation_tips = get_transportation_tips()
    food_tips = get_food_tips()
    energy_tips = get_energy_tips()

    if request.method == 'POST':
        transportation_amount = request.form['transportation_amount']
        transportation_type = request.form['transportation_type']
        transportation_carbon_footprint = calculate_transportation_carbon_footprint(transportation_amount, transportation_type)

        food_amount = request.form['food_amount']
        food_type = request.form['food_type']
        food_carbon_footprint = calculate_food_carbon_footprint(food_amount, food_type)

        energy_amount = request.form['energy_amount']
        energy_type = request.form['energy_type']
        energy_carbon_footprint = calculate_energy_carbon_footprint(energy_amount, energy_type)

        total_carbon_footprint = transportation_carbon_footprint + food_carbon_footprint + energy_carbon_footprint

        return render_template('results.html', total_carbon_footprint=total_carbon_footprint, transportation_carbon_footprint=transportation_carbon_footprint, food_carbon_footprint=food_carbon_footprint, energy_carbon_footprint=energy_carbon_footprint, transportation_tips=transportation_tips, food_tips=food_tips, energy_tips=energy_tips)
    else:
        return render_template('index.html', transportation_tips=transportation_tips, food_tips=food_tips, energy_tips=energy_tips)

# Define templates for carbon footprint tracking and tips pages
@app.route('/results')
def results():
    # Your code to retrieve carbon footprint results and tips
    return render_template('results.html')

@app.route('/tips')
def tips():
    transportation_tips = get_transportation_tips()
    food_tips = get_food_tips()
    energy_tips = get_energy_tips()
    return render_template('tips.html', transportation_tips=transportation_tips, food_tips=food_tips, energy_tips=energy_tips)

if __name__ == '__main__':
    app.run(debug=True)
