import requests
import json
# from akun import config

def get(params):
    url = 'https://siat.untad.ac.id/api/index.php?op=data&service'
    header = {"Authorization" : "Basic NGM1MDYzNWQyZTY3M2NmZWMzMjcyNjJkZWNiNDExMGViOTU2NzNhNjpNV00wWVRZMFpESTBPVEF4TURBNU9XUm1OVFZrTVdVMU5EazNOalZtTldVeVpUZG1aVGt6TmpoaU1EQXhOMlJqTXpFek5tSmxNVGszTW1FME5Ea3pNV0l5TldFNE5XRmtNRGRpTWpkalltVT0="} 
    response = requests.get(url, params=params, headers=header)
    return json.loads(response.text)

def post(params):
    url = 'https://siat.untad.ac.id/api/index.php?op=data&service=InsertKRS'
    header = {"Authorization" : "Basic NGM1MDYzNWQyZTY3M2NmZWMzMjcyNjJkZWNiNDExMGViOTU2NzNhNjpNV00wWVRZMFpESTBPVEF4TURBNU9XUm1OVFZrTVdVMU5EazNOalZtTldVeVpUZG1aVGt6TmpoaU1EQXhOMlJqTXpFek5tSmxNVGszTW1FME5Ea3pNV0l5TldFNE5XRmtNRGRpTWpkalltVT0="} 
    response = requests.post(url, data=params, headers=header)
    return json.loads(response.text)