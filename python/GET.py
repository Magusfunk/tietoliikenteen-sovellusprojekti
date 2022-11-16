import requests
import csv
url = ("http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=60")
response = requests.get(url).text

with open('./export.csv', mode='w') as f:
    f.write(response)