import requests

# Send request to Facebook
response = requests.get("https://www.facebook.com/")

# Print the result
print("Status Code:", response.status_code)
print("\nData received from Facebook:\n")
print(response.text[:500])