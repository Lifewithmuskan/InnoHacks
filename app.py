import pandas as pd

def extract_product_names(csv_file):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)
        
        # Extract the product names from the 'product_name' column
        product_names = df['name'].tolist()
        
        return product_names
    except Exception as e:
        print("Error:", e)
        return []

# Replace 'your_csv_file.csv' with the path to your CSV file
product_names = extract_product_names('C:/Users/DELL/OneDrive/Desktop/finalllll_project/sample.csv')

# Print the list of product names
print(product_names)
