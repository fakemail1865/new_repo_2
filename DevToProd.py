from github import Github
import requests
import io

# Create a PyGitHub object using your GitHub API access token
g = Github("fakemail1865","omarnavaro2")

# Get the repository and file you want to access
repo = g.get_repo("fakemail1865/new_repo_2")
file = repo.get_contents("CustomerB2C [0.0].xml")

# Read the contents of the file as a raw string
payload = file.decoded_content.decode('utf-8')

#convert to octet stream
payload_bytes = payload.encode('utf-8')
payload = io.BytesIO(payload_bytes)

# Print the contents of the file
#print(payload)

# Set the URL for the Semarchy import-replace API
name = 'CustomerB2C'
key = '0.0'
url = "http://a7525abf4703b4bd8a72adf63f003c94-754996992.ap-south-1.elb.amazonaws.com/semarchy/api/rest/app-builder/models/{0}/editions/{1}/content".format(name,key)

print(url)
# Set the headers for the API call
headers = {
    'Authorization': 'Basic c2VtYWRtaW46c2VtYWRtaW4=',
    "Content-Type": "application/octet-stream"
}

# Set the data for the API call


# Send the API request to import and replace the model
response = requests.post(url, headers=headers, data=payload)

# Check the status code of the API response
if response.status_code == 200:
    print("Model imported and replaced successfully")
else:
    print(response.text)

