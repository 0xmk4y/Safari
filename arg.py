import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--url', type=str, required=True)
parser.add_argument('--username', type=str, required=True)
parser.add_argument('--wordlist', type=str, required=True)


args = parser.parse_args()

print(args.name)