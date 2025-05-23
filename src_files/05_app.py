# 05_app.py
# This script sets up a Flask web application to serve road fatalities data.
# It provides RESTful API endpoints for CRUD operations on the data stored in a CSV file.
# Author: Edward Cronin (g00425645)

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)
api = Api(app)

# Path to the CSV file
csv_file_path = "../data/five_yr_fatalities.csv"

# Helper class to manage data storage
class DataStore:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        try:
            self.df = pd.read_csv(self.csv_file)
            if "id" not in self.df.columns:
                self.df.insert(0, "id", range(1, len(self.df) + 1))
                self.save()
        except FileNotFoundError:
            print(f"Error: {self.csv_file} not found. Initializing an empty data store.")
            self.df = pd.DataFrame(columns=["id", "Year", "Month", "Fatalities"])

    def save(self):
        self.df.to_csv(self.csv_file, index=False)

    def get_all(self):
        return self.df.to_dict(orient="records")

    def get_by_id(self, record_id):
        return self.df.loc[self.df["id"] == record_id].to_dict(orient="records")

    def add_record(self, record):
        new_id = self.df["id"].max() + 1 if not self.df.empty else 1
        record["id"] = new_id
        self.df = pd.concat([self.df, pd.DataFrame([record])], ignore_index=True)
        self.save()
        return record

    def update_record(self, record_id, updates):
        index = self.df.index[self.df["id"] == record_id].tolist()
        if not index:
            return None
        self.df.loc[index[0], updates.keys()] = updates.values()
        self.save()
        return self.df.loc[index[0]].to_dict()

    def delete_record(self, record_id):
        index = self.df.index[self.df["id"] == record_id].tolist()
        if not index:
            return None
        self.df = self.df.drop(index[0])
        self.save()
        return True

# Initialize the data store
data_store = DataStore(csv_file_path)

class FatalitiesResource(Resource):
    def get(self):
        record_id = request.args.get("id")
        if record_id:
            record = data_store.get_by_id(int(record_id))
            if record:
                return record[0], 200
            return {"message": "Record not found"}, 404
        return data_store.get_all(), 200

    def post(self):
        new_record = request.json
        required_fields = {"Year", "Month", "Fatalities"}
        if not required_fields.issubset(new_record):
            return {"message": "Missing required fields"}, 400
        if not isinstance(new_record["Fatalities"], int) or new_record["Fatalities"] < 0:
            return {"message": "Invalid fatalities value"}, 400
        created_record = data_store.add_record(new_record)
        return {"message": "Record created successfully", "record": created_record}, 201

    def put(self, record_id):
        updates = request.json
        updated_record = data_store.update_record(record_id, updates)
        if not updated_record:
            return {"message": "Record not found"}, 404
        return {"message": "Record updated successfully", "record": updated_record}, 200

    def delete(self, record_id):
        if data_store.delete_record(record_id):
            return {"message": "Record deleted successfully"}, 200
        return {"message": "Record not found"}, 404

class GroupedFatalitiesResource(Resource):
    def get(self):
        df = data_store.df
        grouped_df = df.groupby(["Year", "Month"], as_index=False).sum()
        month_order = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        grouped_df["Month"] = pd.Categorical(grouped_df["Month"], categories=month_order, ordered=True)
        grouped_df = grouped_df.sort_values(by=["Year", "Month"])
        return grouped_df.to_dict(orient="records"), 200

api.add_resource(FatalitiesResource, "/api/fatalities", "/api/fatalities/<int:record_id>")
api.add_resource(GroupedFatalitiesResource, "/api/grouped-fatalities")

if __name__ == "__main__":
    app.run(debug=True)
