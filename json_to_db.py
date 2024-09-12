import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("db_token")
args = parser.parse_args()
db_token = args.db_token
conn_str = f"DRIVER={{SQL Server}};{db_token}"
print(conn_str)
