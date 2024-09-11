import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("db_token")
args = parser.parse_args()
conn_str = args.db_token
print(conn_str)
