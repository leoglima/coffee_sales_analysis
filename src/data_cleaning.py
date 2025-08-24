import pandas as pd
import re

def load_and_clean_data(file_path):
    with open(file_path, 'r') as f:
        raw = f.read()
    pattern = r'(\d{4}-\d{2}-\d{2}),(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}),(card|cash),([^,]*),([\d.]+),([^,]+?)(?=\d{4}-\d{2}-\d{2}|$)'
    matches = re.findall(pattern, raw)
    df = pd.DataFrame(matches, columns=['Date', 'Timestamp', 'Payment Method', 'Customer ID', 'Price', 'Product'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Price'] = df['Price'].astype(float)
    df['Product'] = df['Product'].str.strip()
    return df

# Exemplo de uso
if __name__ == "__main__":
    df = load_and_clean_data('../data/coffee_sales.csv')
    print(df.head())