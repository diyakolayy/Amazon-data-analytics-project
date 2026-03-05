from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# load dataset
df = pd.read_csv("cleaned_data.csv")

@app.route("/products")
def get_products():
    data = df.head(100).to_dict(orient="records")
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)