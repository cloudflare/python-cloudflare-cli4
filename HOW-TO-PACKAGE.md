# Packaging instructions

> [!NOTE]
> The `Makefile`, `setup.py`, etc are legacy and not used. We only rely on `pyproject.toml` and related files.
>
> The reason for keeping legacy, unused build files is to avoid touching anything from the original project.

### Install via `rye`

```shell
$ git clone https://github.com/cloudflare/python-cloudflare-cli4.git
$ cd ./python-cloudflare-cli4

$ rye sync --all-features
$ rye run cli4 --help
usage: cli4 [-V|--version] [-h|--help] [-v|--verbose] [-e|--examples] [-q|--quiet] [-j|--json] [-y|--yaml] [-n|--ndjson] [-i|--image] [-r|--raw] [-d|--dump] [-A|--openapi url] [-b|--binary] [-p|--profile profile-name] [-h|--header additional-header] [--get|--patch|--post|--put|--delete] [item=value|item=@filename|@filename ...] /command ...
```

### Install via `pip`

```shell
$ git clone https://github.com/cloudflare/python-cloudflare-cli4.git
$ cd ./python-cloudflare-cli4

$ pip install .
$ cli4 --help
usage: cli4 [-V|--version] [-h|--help] [-v|--verbose] [-e|--examples] [-q|--quiet] [-j|--json] [-y|--yaml] [-n|--ndjson] [-i|--image] [-r|--raw] [-d|--dump] [-A|--openapi url] [-b|--binary] [-p|--profile profile-name] [-h|--header additional-header] [--get|--patch|--post|--put|--delete] [item=value|item=@filename|@filename ...] /command ...
```

### Release to `pypi.org`

1. Login to PyPi with the stainless user: https://pypi.org/user/stainless/ (credentials in 1Password)
2. Go to https://pypi.org/manage/account and create a new API token. Or use one from 1Password if present.

Build a tarball and publish it:

```shell
$ git clone https://github.com/cloudflare/python-cloudflare-cli4.git
$ cd ./python-cloudflare-cli4

$ rye sync --all-features
$ rye build
$ rye run hatch publish
```

If the version has already been released, update the version in `pyproject.toml` and start the process again.
Note that PyPi support versions with a suffix `-<number>` if corrections are needed without touching the
actual version of the CLI.

## Homebrew

The file `./brew-formula-cloudflare-cli4.rb` contains a working Homebrew formula.

To create a new formula, if needed:

```shell
$ brew tab --force homebrew/core
# Create a formula from a git tag. Homebrew only accept stable releases.
$ brew create --python --set-name cloudflare-cli4 'https://github.com/cloudflare/python-cloudflare-cli4/archive/refs/tags/<VERSION>.tar.gz'

# Run checks, fix any reported issues
$ HOMEBREW_NO_INSTALL_FROM_API=1 brew audit --new cloudflare-cli4

# Try to install
$ HOMEBREW_NO_INSTALL_FROM_API=1 brew install cloudflare-cli4

# Ensure it is installed
$ which cli4
/opt/homebrew/bin/cli4

# Ensure it works
$ cli4 --help
usage: cli4 [-V|--version] [-h|--help] [-v|--verbose] [-e|--examples] [-q|--quiet] [-j|--json] [-y|--yaml] [-n|--ndjson] [-i|--image] [-r|--raw] [-d|--dump] [-A|--openapi url] [-b|--binary] [-p|--profile profile-name] [-h|--header additional-header] [--get|--patch|--post|--put|--delete] [item=value|item=@filename|@filename ...] /command ...
```
