# pym - a Python Package Manager
> Why a python package manager? In order to have a more cleaner way to handle python versioning and dependencies listing, therefore deprecating `requirements.txt`

```bash
pip install ppm
```

## Usage
First you need a file named
```
reqs.yaml
```

To install all the packages from a repository, just run the following command (note: this will create an automatic `python_modules` on your project, so you dont have to worry to do it manually)
```bash
ppm install
```
