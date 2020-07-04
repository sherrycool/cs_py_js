from flask import Flask, render_template, request
from models import *
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
	flights = Flight.query.all()
	return render_template("index.html", flights=flights)

@app.route("/book", methods=['POST'])
def book():
	"""Book a flight."""

	# Get from information.
	name = request.form.get("name")
	try:
		flight_id = int(request.form.get("flight_id"))
	except ValueError:
		return render_template("error.html", message="Invalid flight number.")

	# Make sure the flight exists.
	flight = Flight.query.get(flight_id)
	if flight is None:
		return render_template("error.html", message="No such flight with that id.")

	# Add passenger.
	'''
	passenger = Passenger(name=name, flight_id=flight_id)
	db.session.add(passenger)
	db.session.commit()
	'''
	flight.add_passenger(name)
	return render_template("success.html", name=name.title(), flight_id=flight_id)

@app.route("/flights")
def flights():
	# list all flights.
	flights = Flight.query.all()
	return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
	flight = Flight.query.get(flight_id)
	if flight is None:
		return render_template("error.html", message="No such flight with that id.")

	# get all passengers
	#passengers = Passenger.query.filter_by(flight_id=flight_id).all()
	passengers = flight.passengers
	return render_template('flight.html', flight=flight, passengers=passengers)

@app.route('/api/flights/<int:flight_id>')
def flight_api(flight_id):
	# Return details about a single flight.

	# Make sure flight exists.
	flight = Flight.query.get(flight_id)
	if flight is None:
		return jsonify({"error":"Invalid flight_id"}), 422

	# Get all passengers
	passengers = flight.passengers
	names = []
	for passenger in passengers:
		names.append(passenger.name)
	return jsonify({
		"origin": flight.origin,
		"destination": flight.destination,
		"duration": flight.duration,
		"passengers":names
		})


def main():
	app.run(debug=True)

if __name__ == "__main__":
	main()