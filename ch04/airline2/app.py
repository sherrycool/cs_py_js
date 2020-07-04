from flask import Flask, render_template, request
from models import *

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
	passengers = Passenger.query.filter_by(flight_id=flight_id).all()
	return render_template('flight.html', flight=flight, passengers=passengers)




def main():
	app.run(debug=True)

if __name__ == "__main__":
	main()