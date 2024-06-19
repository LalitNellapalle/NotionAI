import os
import requests
from datetime import datetime, timezone
from notion_client import Client
from pprint import pprint

NOTION_TOKEN = "secret_01OtDI9rlZsaPJxLkKl8IcQf58TX5mEHzY19zdrDrNe"
DATABASE_ID = "42905751d54a4039bd732326a27f1063"

headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
notion = Client(auth=os.environ["NOTION_TOKEN"])

def printUser(notion):
    list_users_response = notion.users.list()
    pprint(list_users_response)

def main():
    printUser(notion)
    print(1)

