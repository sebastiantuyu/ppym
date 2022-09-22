from typing import MutableSequence
import yaml
import os, sys, re

requiredFiles = [
  "reqs.example.yaml",
  "reqs.yaml",
  "python_modules"
]

def folderParser(line: str) -> bool:
  return re.compile(r"/a-zA-Z0-9/")

def checkState():
  with os.popen("ls -d ./python_modules/lib/python3.9/site-packages/*") as f:
    [print(line) for line in f.readlines()]

def checkFileExists(files: MutableSequence[str]) -> bool:
  all_files_exists = []
  with os.popen("ls -lh") as f:
    for line in f.readlines():
      [all_files_exists.append(fileName in line) for fileName in files]
  return all_files_exists.count(True) == files.__len__()


def add_package_to_state(packageName: str):
  with os.popen("ls -d */") as f:
    [print(line) for line in f.readlines()]
  pass


def install_package(packageName: str):
  try:
    r = os.system(f"pip install {packageName}")
    if r == 0:
      add_package_to_state(packageName)
  except:
    print("package doesnt exist or is not available")

def installer():
  checkState()
  # with open("reqs.example.yaml", "r") as stream:
  #   reqs = yaml.safe_load(stream)
  #   [install_package(p) for p in reqs['requirements']]
  # pass


if __name__ == '__main__':
  # Run ppym
  command = sys.argv[1]
  if checkFileExists(requiredFiles):
    # argv 1 -> command to run
    if command == 'run': installer()
    if command == 'install' or command == 'i': installer()
  else:
    raise Exception('Do you have your reqs.yaml file?')
