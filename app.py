import pandas as pd
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Mock property data (replace with real API or database connection)
properties = [
    {
        "address": "123 Elm St, Memphis, TN",
        "price": 85000,
        "monthly_rent": 1350,
        "expenses": 300,
        "seller_financing": True
    },
    {
        "address": "456 Oak Ave, Birmingham, AL",
        "price": 90000,
        "monthly_rent": 1300,
        "expenses": 250,
        "seller_financing": False
    },
    {
        "address": "789 Pine Dr, Cleveland, OH",
        "price": 80000,
        "monthly_rent": 1250,
        "expenses": 200,
        "seller_financing": True
    }
]

@app.route('/')
def index():
    return "Section 8 Property Filter API is running. Use /filter to see results."

@app.route('/filter', methods=['GET'])
def filter_properties():
    df = pd.DataFrame(properties)
    df["monthly_cash_flow"] = df["monthly_rent"] - df["expenses"]
    filtered = df[(df["seller_financing"] == True) & (df["monthly_cash_flow"] > 0)]
    result = filtered.to_dict(orient="records")
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
