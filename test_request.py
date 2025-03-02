import requests

url = "http://127.0.0.1:5000/process_mri"
files = {'file': open("sample.dcm", "rb")}  # Replace with your DICOM file

response = requests.post(url, files=files)

if response.status_code == 200:
    with open("result.png", "wb") as f:
        f.write(response.content)
    print("Processed image saved as result.png")
else:
    print("Error:", response.json())
