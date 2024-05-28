import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--changed_files", default="conf/**")
args = parser.parse_args()
changed_files = args.changed_files

def main(changed_files):
    with open(changed_files) as json_file:
        teams = json.load(json_file)
    for team_data in teams:
        print(team_data['name'])
        print(team_data['roll'])
main(changed_files)
