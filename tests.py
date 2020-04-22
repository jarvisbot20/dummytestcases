import requests

resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if resp.status_code == 200:
    print("Fetch Successful")