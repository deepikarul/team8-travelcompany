from flask import Blueprint, request, jsonify
from app import mysql

packages_bp = Blueprint('travel_packages', __name__, url_prefix='/packages')

def query_db(query, args=(), fetch=True):
    cur = mysql.connection.cursor()
    cur.execute(query, args)
    if fetch:
        return [dict(zip([col[0] for col in cur.description], row)) for row in cur.fetchall()]
    mysql.connection.commit()

@packages_bp.route('/packages', methods=['GET'])
def get_packages():
    packages = query_db("SELECT * FROM TravelPackages")
    return jsonify(packages)

@packages_bp.route('/packages', methods=['POST'])
def add_package():
    data = request.json
    query_db(
        "INSERT INTO TravelPackages (packageID, name, destination, totalPrice) VALUES (%s, %s, %s, %s)",
        (data['packageID'], data['name'], data['destination'], data['totalPrice']),
        fetch=False
    )
    return jsonify({'message': 'Package added successfully'}), 201

@packages_bp.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    data = request.json
    query_db(
        "UPDATE TravelPackages SET totalPrice = %s WHERE packageID = %s",
        (data['totalPrice'], package_id),
        fetch=False
    )
    return jsonify({'message': 'Package updated successfully'})

@packages_bp.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    query_db("DELETE FROM TravelPackages WHERE packageID = %s", (package_id,), fetch=False)
    return jsonify({'message': 'Package deleted successfully'})

@packages_bp.route('/packages/<int:package_id>/activities', methods=['GET'])
def get_package_activities(package_id):
    activities = query_db("""
        SELECT a.* FROM Activities a
        JOIN PackageActivities pa ON a.activityID = pa.activityID
        WHERE pa.packageID = %s
    """, (package_id,))
    return jsonify(activities)
