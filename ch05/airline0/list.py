import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/test')
db = scoped_session(sessionmaker(bind=engine))

def main():
	flights_info = db.execute("SELECT * FROM flights").fetchall()  # get a list
	for flight in flights_info:
		print(f"Flights from {flight.origin} to {flight.destination} lasting {flight.duration} minutes.")

if __name__ == "__main__":
	main()