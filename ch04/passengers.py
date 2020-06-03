import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/test')
db = scoped_session(sessionmaker(bind=engine))

def main():
	# list all flights.
	flights = db.execute("SELECT id, origin, destination from flights").fetchall()
	for flight in flights:
		print(f"Flight {flight.id}: {flight.origin} to {flight.destination}")

	# prompt user to choose a flight:
	flight_id = int(input("\nFlight id:"))
	flight = db.execute("SELECT origin, destination, duration from flights where id = :id",
		{"id": flight_id}).fetchone()

	# make sure flight is valid
	if flight is None:
		return "Sorry, no such flight here."
	print(f"Flight {flight_id}: {flight.origin} to {flight.destination}")

	# list passengers
	passengers = db.execute("SELECT name from passengers where flight_id = :flight_id",
		{"flight_id": flight_id}).fetchall()

	if len(passengers)==0:
		return "No passengers fly with such flight."
	print("\nPassengers:")
	for passenger in passengers:
		print(f" {passenger.name} ")

if __name__ == '__main__':
	main()