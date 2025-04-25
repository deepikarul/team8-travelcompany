from flask import Blueprint, request, jsonify
from app import mysql

flights_bp = Blueprint('flights', __name__, url_prefix='/flights')

def query_db(query, args=(), fetch=True):
    cur = mysql.connection.cursor()
    cur.execute(query, args)
    if fetch:
        return [dict(zip([col[0] for col in cur.description], row)) for row in cur.fetchall()]
    mysql.connection.commit()

@flights_bp.route('/flights', methods=['GET'])
def get_flights():
    return jsonify(query_db("SELECT * FROM Flights"))

@flights_bp.route('/flights', methods=['POST'])
def add_flight():
    data = request.json
    query_db(
        """INSERT INTO Flights 
        (flightID, airline, departCity, destCity, departTime, arrivalTime, flightPrice) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (
            data['flightID'], data['airline'], data['departCity'], data['destCity'],
            data['departTime'], data['arrivalTime'], data['flightPrice']
        ),
        fetch=False
    )
    return jsonify({'message': 'Flight added successfully'}), 201

@flights_bp.route('/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    data = request.json
    query_db(
        "UPDATE Flights SET flightPrice = %s WHERE flightID = %s",
        (data['flightPrice'], flight_id),
        fetch=False
    )
    return jsonify({'message': 'Flight updated successfully'})

@flights_bp.route('/flights/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    query_db("DELETE FROM Flights WHERE flightID = %s", (flight_id,), fetch=False)
    return jsonify({'message': 'Flight deleted successfully'})

@flights_bp.route('/flights/to/<string:dest_city>', methods=['GET'])
def get_flights_by_destination(dest_city):
    return jsonify(query_db("SELECT * FROM Flights WHERE destCity = %s", (dest_city,)))
