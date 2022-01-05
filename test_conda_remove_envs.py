import pytest
import subprocess

import conda_remove_envs as cenv


VALID_ENV_NAMES = [["test"], ["test", "test2"]]


def create_conda_env(env_list):
    for env in env_list:
        subprocess.run(["conda", "create", "--name", env])


@pytest.mark.parametrize("env_list", VALID_ENV_NAMES)
def test_remove_env(env_list):
    exp_envs = cenv.list_envs()
    create_conda_env(env_list)
    cenv.remove(env_list)
    act_envs = cenv.list_envs()
    assert set(exp_envs) == set(act_envs)
