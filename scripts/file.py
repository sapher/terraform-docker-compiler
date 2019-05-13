#!/usr/bin/python
import os, sys, json, hashlib

def read_in():
    return {x.strip() for x in sys.stdin}

def get_digest(file_path):
    h = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()

if __name__ == "__main__":
  lines = read_in()
  for line in lines:
    if line:
      jsondata = json.loads(line)
      input = jsondata['file']
      exist = os.path.isfile(input)
      if exist is True:
        sys.stdout.write(json.dumps({ "exist": "1" }))
      else:
        sys.stdout.write(json.dumps({ "exist": "0" }))
