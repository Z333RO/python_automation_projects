url = "https://raw.githubusercontent.com/Z333RO/security-tools-public/main/arp_spoof_detector.py"

import requests

req = requests.get(url)
# print(req.content)
content = req.content

with open('download.py', 'wb') as file: #change download.py to the corresponding file type
    file.write(content)