from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS  # Import CORS
import pandas as pd  # Import pandas for reading CSV files

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
api = Api(app)

# Path to the CSV file
csv_file_path = "../data/five_yr_fatalities.csv"

# Load data from the CSV file
try:
    df = pd.read_csv(csv_file_path)
    if "id" not in df.columns:
        # Add an 'id' column if missing
        df.insert(0, "id", range(1, len(df) + 1))
        df.to_csv(csv_file_path, index=False)  # Save the updated CSV file
    data_store = df.to_dict(orient="records")  # Convert DataFrame to a list of dictionaries
except FileNotFoundError:
    print(f"Error: {csv_file_path} not found. Initializing an empty data store.")
    data_store = []  # If the file is not found, initialize an empty data store

# Auto-increment ID for new entries
next_id = len(data_store) + 1

# Helper function to save data back to the CSV file
def save_to_csv():
    df = pd.DataFrame(data_store)
    df.to_csv(csv_file_path, index=False)

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
        save_to_csv()  # Save changes to the CSV file
        return {"message": "Record created successfully", "record": new_record}, 201

    # UPDATE: Update an existing record by ID
    def put(self, record_id):
        record = next((item for item in data_store if item["id"] == int(record_id)), None)
        if not record:
            return {"message": "Record not found"}, 404

        updated_data = request.json
        record.update(updated_data)
        save_to_csv()  # Save changes to the CSV file
        return {"message": "Record updated successfully", "record": record}, 200

    # DELETE: Delete a record by ID
    def delete(self, record_id):
        global data_store
        record = next((item for item in data_store if item["id"] == int(record_id)), None)
        if not record:
            return {"message": "Record not found"}, 404

        data_store = [item for item in data_store if item["id"] != int(record_id)]
        save_to_csv()  # Save changes to the CSV file
        return {"message": "Record deleted successfully"}, 200

# API Resource for grouped data
class GroupedFatalitiesResource(Resource):
    def get(self):
        # Load the data into a DataFrame
        df = pd.DataFrame(data_store)

        # Group data by Year and Month
        grouped_df = df.groupby(["Year", "Month"], as_index=False).sum()

        # Sort the data by Year and Month
        month_order = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        grouped_df["Month"] = pd.Categorical(grouped_df["Month"], categories=month_order, ordered=True)
        grouped_df = grouped_df.sort_values(by=["Year", "Month"])

        # Convert to a list of dictionaries
        grouped_data = grouped_df.to_dict(orient="records")
        return grouped_data, 200

# Add routes to the API
api.add_resource(FatalitiesResource, '/api/fatalities', '/api/fatalities/<int:record_id>')
api.add_resource(GroupedFatalitiesResource, '/api/grouped-fatalities')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)