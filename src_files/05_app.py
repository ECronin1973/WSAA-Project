from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# In-memory data store (for demonstration purposes)
data_store = [
    {"id": 1, "year": 2020, "month": "January", "fatalities": 9},
    {"id": 2, "year": 2020, "month": "February", "fatalities": 19},
    {"id": 3, "year": 2020, "month": "March", "fatalities": 17},
]

# Auto-increment ID for new entries
next_id = len(data_store) + 1

# API Resource for CRUD operations
class FatalitiesResource(Resource):
    # READ: Get all records or a specific record by ID
    def get(self):
        record_id = request.args.get('id')
        if record_id:
            record = next((item for item in data_store if item["id"] == int(record_id)), None)
            if record:
                return record, 200
            return {"message": "Record not found"}, 404
        return data_store, 200

    # CREATE: Add a new record
    def post(self):
        global next_id
        new_record = request.json

        # Validation
        if not all(k in new_record for k in ("year", "month", "fatalities")):
            return {"message": "Missing required fields"}, 400
        if not isinstance(new_record["fatalities"], int) or new_record["fatalities"] < 0:
            return {"message": "Invalid fatalities value"}, 400

        new_record["id"] = next_id
        data_store.append(new_record)
        next_id += 1
        return {"message": "Record created successfully", "record": new_record}, 201

    # UPDATE: Update an existing record by ID
    def put(self, record_id):
        record = next((item for item in data_store if item["id"] == record_id), None)
        if not record:
            return {"message": "Record not found"}, 404

        updated_data = request.json
        record.update(updated_data)
        return {"message": "Record updated successfully", "record": record}, 200

    # DELETE: Delete a record by ID
    def delete(self, record_id):
        global data_store
        record = next((item for item in data_store if item["id"] == record_id), None)
        if not record:
            return {"message": "Record not found"}, 404

        data_store = [item for item in data_store if item["id"] != record_id]
        return {"message": "Record deleted successfully"}, 200


# Add routes to the API
api.add_resource(FatalitiesResource, '/api/fatalities', '/api/fatalities/<int:record_id>')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
# This code provides a simple CRUD API for managing road fatalities data.
# it uses Flask and Flask-RESTful to create the API endpoints.