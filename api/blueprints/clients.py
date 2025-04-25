from flask import Blueprint, request, jsonify
from app import mysql

clients_bp = Blueprint('clients', __name__, url_prefix='/clients')

def query_db(query, args=(), fetch=True):
    cur = mysql.connection.cursor()
    cur.execute(query, args)
    if fetch:
        result = [dict(zip([col[0] for col in cur.description], row)) for row in cur.fetchall()]
        return result
    mysql.connection.commit()

@clients_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = query_db("SELECT * FROM Clients")
    return jsonify(clients)

@clients_bp.route('/clients', methods=['POST'])
def add_client():
    data = request.json
    query_db(
        "INSERT INTO Clients (clientID, Fname, Lname, phoneNum) VALUES (%s, %s, %s, %s)",
        (data['clientID'], data['Fname'], data['Lname'], data['phoneNum']),
        fetch=False
    )
    return jsonify({'message': 'Client added successfully'}), 201

@clients_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.json
    query_db(
        "UPDATE Clients SET phoneNum = %s WHERE clientID = %s",
        (data['phoneNum'], client_id),
        fetch=False
    )
    return jsonify({'message': 'Client updated successfully'})

@clients_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    query_db("DELETE FROM Clients WHERE clientID = %s", (client_id,), fetch=False)
    return jsonify({'message': 'Client deleted successfully'})

@clients_bp.route('/clients/<int:client_id>/packages', methods=['GET'])
def get_client_packages(client_id):
    packages = query_db("""
        SELECT p.* FROM TravelPackages p
        JOIN ClientPackages cp ON p.packageID = cp.packageID
        WHERE cp.clientID = %s
    """, (client_id,))
    return jsonify(packages)
