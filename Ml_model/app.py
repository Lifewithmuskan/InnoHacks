from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

my_catalog_app = Flask("my_catalog_app")

# Load your Myntra dataset from a CSV file (replace 'myntra_dataset.csv' with your actual filename)
myntra_data = pd.read_csv('C:/Users/DELL/OneDrive/Desktop/KaTaLoG/myntra_dataset.csv')

# Process text data for machine learning comparison
def process_text_data(data):
    vectorizer = CountVectorizer().fit_transform(data)
    return cosine_similarity(vectorizer)

@my_catalog_app.route('/')
def index():
    return render_template('index.html')

@my_catalog_app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']
        
        # Process the uploaded file and convert to lists
        if file:
            uploaded_data = pd.read_csv(file)
            uploaded_lists = uploaded_data.values.tolist()

            # Process text data for machine learning comparison
            uploaded_similarity_matrix = process_text_data(uploaded_data['product_description'])

            # Compare with Myntra dataset
            myntra_similarity_matrix = process_text_data(myntra_data['product_description'])

            # Get the column names of the uploaded data
            column_names = uploaded_data.columns.tolist()

            # Perform further processing and get desired results

            # For simplicity, return the similarity matrices and column names in the response
            return jsonify({
                'column_names': column_names,
                'uploaded_similarity_matrix': uploaded_similarity_matrix.tolist(),
                'myntra_similarity_matrix': myntra_similarity_matrix.tolist()
            })

    # If the function reaches this point without returning a response,
    # return a 400 Bad Request response indicating that the request was malformed
    return jsonify({'error': 'Malformed request'}), 400

if __name__ == '__main__':
    my_catalog_app.run(debug=True)
