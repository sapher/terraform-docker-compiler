import json
import hashlib, os, sys

# Read stdin
def read_in():
    return {x.strip() for x in sys.stdin}

# Get hash of all files in a dir
def get_hash_of_dir(directory):
  SHAhash = hashlib.sha1()
  if not os.path.exists (directory):
    return -1
    
  try:
    for root, dirs, files in os.walk(directory):
      for names in files:
        filepath = os.path.join(root,names)
        try:
          f1 = open(filepath, 'rb')
        except:
          # You can't open the file for some reason
          f1.close()
          continue

	while 1:
	  # Read file in as little chunks
  	  buf = f1.read(4096)
	  if not buf : break
	  SHAhash.update(hashlib.sha1(buf).hexdigest())
        f1.close()

  except:
    import traceback
    # Print the stack traceback
    traceback.print_exc()
    return -2

  return SHAhash.hexdigest()

if __name__ == "__main__":
  lines = read_in()
  for line in lines:
    if line:
      jsondata = json.loads(line)
      sha = get_hash_of_dir(jsondata['dir'])
      print(json.dumps({ "sha": sha }))