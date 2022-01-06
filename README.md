# Remove conda environments

Remove multiple conda environments.

The tool was created to bulk-remove conda environments to avoid the need to have multiple `conda env remove -n NAME` commands. Instead, you can now remove multiple environments with

```text
python conda_remove_envs.py -n NAME1 NAME2 ...
```

## Usage

Remove one environment

```text
python conda_remove_envs.py -n NAME
```

Remove multiple environments

```text
python conda_remove_envs.py -n NAME1 NAME2
```

## Install

Clone the project

```text
git clone https://github.com/trevor-moon/conda-remove-envs.git
```

Change to the install location

```text
cd conda-remove-envs
```

Use

```text
python conda-remove-envs.py --help
```

## Roadmap

- [ ] Publish to channels ([issue #4](https://www.github.com/trevor-moon/conda-remove-envs/issues/4))
- [ ] Bash wrapper for python script
- [ ] Setup CI & CD tools ([issue #12](https://www.github.com/trevor-moon/conda-remove-envs/issues/12))

## Contributing

See [good first issues](https://www.github.com/trevor-moon/conda-remove-envs/issues/) for quick contributions.

Take a look at the [open issues](https://www.github.com/trevor-moon/conda-remove-envs/issues/) and [open pull requests](https://www.github.com/trevor-moon/conda-remove-envs/pulls) for other tasks.

If you find any issues or want a new feature, consider [create an issue](https://www.github.com/trevor-moon/conda-remove-envs/issues/) or [create a pull-request](https://www.github.com/trevor-moon/conda-remove-envs/pulls/new).

## Contact

You can contact me at through [email](mailto:trevor.r.moon@gmail.com) or [discord](https://discordapp.com/users/477451290469859339) with the subject of the message "conda-remove-envs". That way I know why you're messaging :smile:

## License

[![The MIT License](https://img.shields.io/badge/license-MIT-gree?style=flat)](LICENSE)
