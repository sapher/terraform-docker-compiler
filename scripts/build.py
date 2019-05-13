#!/usr/bin/python
import os

# Retrieve envs
image = os.environ['IMAGE']
input_dir = os.environ['INPUT_DIR']
output_dir = os.environ['OUTPUT_DIR']
script = os.environ['SCRIPT']
filename = os.environ['FILENAME']

# Create output directory, make sure it exist
try:
    os.makedirs(output_dir)
except:
    pass

# Launch docker command for building
os.system("docker run --env FILENAME={0} -v {1}:/input:ro -v {2}:/output -w /input {3} /bin/sh {4}".format(filename, input_dir, output_dir, image, script))