import subprocess as sp
import argparse
import re


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


def cli():
    """Run command-line program"""
    args = parse_args()
    for env in args.name:
        remove_env(env)


if __name__ == "__main__":
    cli()
