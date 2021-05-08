# Python HAProxy API Development Info

Here you can find some useful scripts and requirements
for the package development process.

We are expecting that of each of the package contributor
or developer will respect our [Development Policies](#Package Development Policies),
requirements and recommendations that could be a found
bellow.

## Package Development Policies

Here is a short list of policies that each of you
shall respect.

This list could be extended in the future...

- Don't be an evil and respect the others

- Use development requirements

- Use development recommendations

## Requirements

- Use pre-commit with repo-provided hooks on each commit

- Use commitizen for do commit messages

## Recommendations

- Try to answer for question "Why I do the change?" in commit message.

- Use repo-provided Makefile to install dev requirements

- Fix the bugs firs and make features after

- Develop and test in separated python virtual environments

## Misc

For easy-to-develop we are providing simple Makefile that
will install some development requirements but not all
of them.

To install it just do `make` into dev directory (
available on Linux OS only.
)

Example:

```shell
    py-haproxy-api/dev $ make
```

Or you can install it by hands...

```shell
    py-haproxy-api $ pip install -r dev/requirements.txt
    py-haproxy-api $ pre-commit install
    py-haproxy-api $ pre-commit install-hooks
```
