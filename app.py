from flask import Flask, render_template
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the data
# df = pd.read_csv('static/ratings_Electronics.csv', header=None)
# df.columns = ['user_id', 'prod_id', 'rating', 'timestamp']
# df = df.drop('timestamp', axis=1)
# df_copy = df.copy(deep=True)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the recommendation logic
@app.route('/recommend', methods=['POST'])
def recommend():
    # Perform analysis and recommendation logic here
    
    # Dummy product details (replace with your actual logic)
    top_products = [
        {"id": "prodduct123", "name": "Product 1", "image": "product123.jpeg"},
        {"id": "product456", "name": "Product 2", "image": "product456.jpeg"},
        {"id": "product789", "name": "Product 3", "image": "product789.jpeg"},
        {"id": "product89", "name": "Product 4", "image": "product89.jpeg"},
        {"id": "proudct10", "name": "Product 5", "image": "product10.jpeg"}
    ]
    
    return render_template('result.html', top_products=top_products)

if __name__ == '__main__':
    app.run(debug=True)
