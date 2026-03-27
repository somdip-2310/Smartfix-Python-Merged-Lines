from flask import Flask, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route("/")
def index():
    # Simple test: create a numpy array, pandas df, and sklearn model
    arr = np.array([1, 2, 3, 4, 5])
    df = pd.DataFrame({"values": arr})
    model = LinearRegression()
    return jsonify({
        "status": "ok",
        "numpy_sum": int(arr.sum()),
        "pandas_shape": list(df.shape),
        "model": str(type(model).__name__)
    })

@app.route("/health")
def health():
    return jsonify({"healthy": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
