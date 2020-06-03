import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
	flights = db.execute("SELECT origin, destination, duration from flights").fetchall()
	for flight in flights:
		print(f"{flight.orgin} to {flight.destination}, {flight.duration}")

if __name__ == "__main__":
	main()