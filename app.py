from flask import Flask, request, jsonify
from flask_cors import CORS
from service.SchedulingService import SchedulingService
from models.WildFireData import WildFireData
import csv
import io

app = Flask(__name__)
CORS(app)

@app.route('/process_csv', methods=['POST'])
def process_csv():
    try:
        # Read the CSV data from the request body
        csv_data = request.data.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(csv_data))

        # Process the CSV data (example: convert to list of dictionaries)
        wildFireList = []
        headers = next(csv_reader)
        for row in csv_reader:
            accident_data = dict(zip(headers, row))
            wildFireList.append(WildFireData(accident_data['timestamp'], accident_data['fire_start_time'], accident_data['location'], accident_data['severity']))

        # print(wildFireList)
        service_response = SchedulingService(wildFireList).orchestrate_wild_fires()
        # print(service_response.get_report())

        # Return a JSON response
        return jsonify({"status": "success", "data": service_response.get_report()}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11000)