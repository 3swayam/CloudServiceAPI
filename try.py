import requests

# Define the URL of your Flask app
url = 'http://127.0.0.1:5000/add'

# Define the request parameters
params = {'a': '5', 'b': '10'}  # Parameters to be sent in the request

# Make the POST request with parameters
response = requests.post(url, data=params)

# Check the response status code
if response.status_code == 200:
    # Print the response content (result)
    print("Result:", response.json()['result'])
else:
    print("Error:", response.json())
