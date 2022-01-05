import subprocess as sp
import argparse
import re


# parser = argparse.ArgumentParser(description="Remove conda environment(s)")
# parser.add_argument("-a", "--all", action="store_true", help="Remove all except base")
# parser.add_argument(
#     "-n", "--name", metavar="NAMES", nargs="+", help="Remove conda environments NAMES"
# )
# args = parser.parse_args()

# proc = sp.run(["conda", "env", "list"], stdout=sp.PIPE)
# out = proc.stdout.decode("utf-8")

# env_list = []
# if args.all:
#     env_list = re.findall("[\w-]+\s\s", out)
#     for i, env in enumerate(env_list):
#         env_list[i] = env.strip()
#         # print(env_list
# else:
#     env_list = args.name

# for env in env_list:
#     sp.run(["conda", "env", "remove", "-n", env])
#     print("remove env: {}".format(env))


def parse_args():
    parser = argparse.ArgumentParser(description="Remove conda environment(s)")
    parser.add_argument(
        "-a", "--all", action="store_true", help="Remove all except base"
    )
    parser.add_argument(
        "-n",
        "--name",
        metavar="NAMES",
        nargs="+",
        help="Remove conda environments NAMES",
    )
    args = parser.parse_args()
    return args


def list_envs():
    """Returns conda environments as list"""
    # conda env list output
    proc = sp.run(["conda", "env", "list"], stdout=sp.PIPE)
    out = proc.stdout.decode("utf-8")
    # return conda envs as list
    env_list = re.findall("[\w-]+\s\s", out)
    for i, env in enumerate(env_list):
        env_list[i] = env.strip()
    return env_list


def remove_env(env):
    """Remove conda environment by name"""
    sp.run(["conda", "env", "remove", "-n", env])


def remove(env):
    """Remove conda environment(s) by name"""
    for e in env:
        remove_env(e)


if __name__ == "__main__":
    args = parse_args()
    env_list = list_envs()
    if not args.all:
        env_list = args.name
    remove(env_list)
