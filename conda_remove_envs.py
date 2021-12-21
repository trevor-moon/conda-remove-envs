import subprocess as sp
import argparse
import re


parser = argparse.ArgumentParser(description="Remove conda environment(s)")
parser.add_argument("-a", "--all", action="store_true", help="Remove all except base")
parser.add_argument(
    "-n", "--name", metavar="NAMES", nargs="+", help="Remove conda environments NAMES"
)
args = parser.parse_args()

proc = sp.run(["conda", "env", "list"], stdout=sp.PIPE)
out = proc.stdout.decode("utf-8")

env_list = []
if args.all:
    env_list = re.findall("[\w-]+\s\s", out)
    for i, env in enumerate(env_list):
        env_list[i] = env.strip()
        # print(env_list
else:
    env_list = args.name

for env in env_list:
    sp.run(["conda", "env", "remove", "-n", env])
    print("remove env: {}".format(env))
