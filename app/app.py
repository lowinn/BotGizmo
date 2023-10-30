import requests
from string import Template

blog_id = int(input("Enter blog id: "))

uri = f"https://jsosnplaceholder.typicode.com/posts/{blog_id}"

try:
    server = requests.get(uri)
    if server.status_code == 200:
        print("Request was successful.")
        print("Response content:")
        print(server.text)
    else:
        print(f"Request failed with status code {server.status_code}.")
except RuntimeError:
    print(f"An error occurred while making the request. {RuntimeError.with_traceback}")
