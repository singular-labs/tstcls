# Contribution

## How to upload new version?

- You should have permissions to the package in pypi and to the repository in github
- Update version in setup.py. Version format is: YEAR.QUARTER.SEQUENCE_NUMBER
- Commit your changes and push them into master.
- Run `python setup.py sdist`
- Run `twine upload dist/*` (You should have run `pip install twine` to install twine)
- Create github release with the version as name.

