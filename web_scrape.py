from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/fetch-terms', methods=['POST'])
def fetch_terms():
    data = request.json
    url = data.get('url')

    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch the URL"}), 400

    # Parse the content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract terms and conditions (adjust based on your specific needs)
    terms = soup.find('div', class_='terms-and-conditions')
    if not terms:
        return jsonify({"error": "Could not find terms and conditions"}), 404

    return jsonify({"terms": terms.get_text(strip=True)})

@app.route('/')
def index():
    return "The server is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
