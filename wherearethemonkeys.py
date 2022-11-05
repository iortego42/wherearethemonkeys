#!/usr/local/bin/python3
import yaml
from os import getenv
from dotenv import load_dotenv

load_dotenv()

U_ID = getenv("UID")
SECRET_ID = getenv("SECRETID")

config_template = f"""
---
  intra:
    client: "{U_ID}" #UID
    secret: "{SECRET_ID}" #SECRET
    uri: "https://api.intra.42.fr/v2/oauth/token"
    endpoint: "https://api.intra.42.fr/v2"
    scopes: ""
"""

config_template = yaml.safe_load(config_template)
with open("config.yml", 'w') as config:
    yaml.dump(config_template, config, explicit_start=True)


from intra import ic


with open("monkeys") as file:
    user_out = file.read().replace('\n', ',')

payload = {
        "filter[login]": user_out
}

if not ic.client_id or not ic.client_secret:
    print("\033c------\033[31mERROR\033[0m-------\nPlease edit your config.yml file and add your user id and secret id")
else:
    response = ic.pages_threaded("users", params=payload)

    print("\033c-----------\033[32mCONNECTED\033[0m-----------")
    for user in response:
        if user['location'] != None:
            print(f"  - {user['login']} loged in {user['location']}")

    print("\n---------\033[31mNOT CONNECTED\033[0m---------")
    for user in response:
        if user['location'] == None:
            print(f"  - {user['login']}")
    print("\n")
