import pytest
import subprocess
import warnings

import conda_remove_envs as cenv

VALID_ENV_NAMES = [["test"], ["test", "test2"]]
CLI_STR = "python conda_remove_envs.py"


def create_env(env: str):
    subprocess.run(f"conda create --name {env}".split())


@pytest.mark.parametrize("envlist", VALID_ENV_NAMES)
def test_removal_by_name_should_pass(envlist):
    expected = cenv.list_envs()
    for env in envlist:
        create_env(env)
    cmd = CLI_STR + " -n " + " ".join(envlist)
    subprocess.run(cmd.split())
    actual = cenv.list_envs()
    assert expected == actual


def test_list_envs():
    actual = cenv.list_envs()
    actual.sort()
    expected = list(set(actual))
    expected.sort()
    assert actual == expected


def test_remove_base_warning():
    with pytest.warns(UserWarning) as record:
        warnings.warn("Cannot remove 'base' environment", UserWarning)
    cenv.remove_env("base")
    assert record[0].message.args[0] == "Cannot remove 'base' environment"
