import os
import requests

# Define the URL of the file to be downloaded
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/220px-GitHub_Invertocat_Logo.svg.png"

# Define the folder name and file name
folder_name = "image"
file_name = "GitHub_Invertocat_Logo.png"

# Create the folder if it does not exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Fetch the file from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the file to the specified folder
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"File downloaded and saved at {file_path}")
else:
    print(f"Failed to download the file. HTTP Status Code: {response.status_code}")
