from flask import Blueprint, request, jsonify
from app import mysql

agents_bp = Blueprint('travel_agents', __name__, url_prefix='/agents')

def query_db(query, args=(), fetch=True):
    cur = mysql.connection.cursor()
    cur.execute(query, args)
    if fetch:
        return [dict(zip([col[0] for col in cur.description], row)) for row in cur.fetchall()]
    mysql.connection.commit()

@agents_bp.route('/', methods=['GET'])
def get_agents():
    return jsonify(query_db("SELECT * FROM TravelAgent"))

@agents_bp.route('/', methods=['POST'])
def add_agent():
    data = request.json
    query_db(
        "INSERT INTO TravelAgent (agentID, Fname, Lname, phoneNum) VALUES (%s, %s, %s, %s)",
        (data['agentID'], data['Fname'], data['Lname'], data['phoneNum']),
        fetch=False
    )
    return jsonify({'message': 'Agent added successfully'}), 201

@agents_bp.route('/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    data = request.json
    query_db(
        "UPDATE TravelAgent SET phoneNum = %s WHERE agentID = %s",
        (data['phoneNum'], agent_id),
        fetch=False
    )
    return jsonify({'message': 'Agent updated successfully'})

@agents_bp.route('/<int:agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    query_db("DELETE FROM TravelAgent WHERE agentID = %s", (agent_id,), fetch=False)
    return jsonify({'message': 'Agent deleted successfully'})

@agents_bp.route('/<int:agent_id>/clients', methods=['GET'])
def get_agent_clients(agent_id):
    clients = query_db("""
        SELECT c.* FROM Clients c
        JOIN Helps h ON c.clientID = h.clientID
        WHERE h.agentID = %s
    """, (agent_id,))
    return jsonify(clients)
