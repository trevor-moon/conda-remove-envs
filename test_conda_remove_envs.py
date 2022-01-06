import pytest
import subprocess

import conda_remove_envs as cenv


VALID_ENV_NAMES = [["test"], ["test", "test2"]]


def create_env(env: str):
    subprocess.run(f"conda create --name {env}".split())


def cli_str() -> str:
    return "python conda_remove_envs.py"


@pytest.mark.parametrize("envlist", VALID_ENV_NAMES)
def test_removal_by_name_should_pass(envlist):
    expected = cenv.list_envs()
    for env in envlist:
        create_env(env)
    cmd = cli_str() + " -n " + " ".join(envlist)
    subprocess.run(cmd.split())
    actual = cenv.list_envs()
    assert expected == actual
