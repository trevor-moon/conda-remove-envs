import pytest
import subprocess

import conda_remove_envs as cenv


VALID_ENV_NAMES = [["test"], ["test", "test2"]]


def create_env(env: str):
    subprocess.run(f"conda create --name {env}".split())


def create_conda_env(env_list):
    for env in env_list:
        create_env(env)


def cli_str() -> str:
    return "python conda_remove_envs.py"


@pytest.mark.parametrize("envlist", VALID_ENV_NAMES)
def test_removal_by_name_should_pass(envlist):
    expected = cenv.list_envs()
    create_conda_env(envlist)
    cmd = cli_str() + " -n " + " ".join(envlist)
    subprocess.run(cmd.split())
    actual = cenv.list_envs()
    assert expected == actual


@pytest.mark.parametrize("env_list", VALID_ENV_NAMES)
def test_remove_env(env_list):
    exp_envs = cenv.list_envs()
    create_conda_env(env_list)
    cenv.remove(env_list)
    act_envs = cenv.list_envs()
    assert set(exp_envs) == set(act_envs)
