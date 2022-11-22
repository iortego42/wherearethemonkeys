#!/usr/local/bin/python3
import yaml
from os import getenv
from dotenv import load_dotenv
import sys
from intra import ic



def charge_env() -> None:
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

class Locator:
    def __init__(self, users_input=""):
        try:
            with open(sys.argv[1]) as file:
                self.user_out = file.read().replace('\n', ',')
        except(FileNotFoundError):
            print("\033[31mERROR\nFile not founded")
            exit()
        except (IndexError):
            if users_input:
                self.user_out = users_input
            else:
                print("\033[31mERROR\nNo users input given")
                exit()
        self.payload = {
            "filter[login]": self.user_out
        }
        if not ic.client_id or not ic.client_secret:
            print ("\033[31mERROR\nIncorrect API credentials")

    def shell_list(self) -> None:
        response = ic.pages_threaded("users", params=self.payload)

        print("\033c-----------\033[32mCONNECTED\033[0m-----------")
        for user in response:
            if user['location'] != None:
                print(f"  - \x1b[96m{user['login']}\033[0m loged in {user['location']}")

        print("\n---------\033[31mNOT CONNECTED\033[0m---------")
        for user in response:
            if user['location'] == None:
                print(f"  - {user['login']}")
        print("\n")

    def list(self) -> dict:
        response = ic.pages_threaded("users", params=self.payload)
        usersdict = {}
        for user in response:
            usersdict[user['login']] = user['location']
        return usersdict


locator = Locator()

locator.shell_list()
print(locator.list())
