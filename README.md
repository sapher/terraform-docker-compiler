terraform-docker-compiler
-----------

A terraform module for compiling code in terraform with the help of docker.

This module has been created with the service AWS Lambda in mind. Maybe some change must be made to make it work with other Cloud Provider. 

# Prerequisite

- **Docker**
- **Python 3.7**

# Usage

```terraform
module "compilator" {
  source   = "./module"
  input    = "${path.module}/source"
  output   = "${path.module}/output"
  image    = "node:8.16.0-alpine"
  filename = "lambda.zip"
  script   = "compile.sh"
}
```
## Attributes

*all attributes are required*

- **input** source directory where your code lives
- **output** output directory where you result will be outputed
- **image** docker image to use
- **filename** name of the output file
- **script** relative script file path inside `input` directory

## Compilation script

Compilation is the part that should create yourself. 
The script must compile the code in a directory different than `/input` or `/output`. Only the archive file should be outputed in the folder `/output`.

**Environment variables**

List of variables passed to compilation script :

- **FILENAME** Name of the archive file

**Example**

Here's below an example of a script to compile a npm package.

```bash
# install zip package for alpine
apk add zip

# copy source files to a temp directory
cp -a /input/. /copy

# move to folder
cd /copy

# install npm dependencies
npm ci

# zip current folder /copy to archive file in /output folder
zip -r /output/${FILENAME} .
```

# How it works

A docker container is launch using the `image` passed as attribute.

Two volumes are mounted inside this container, one will bind the `input` directory to `/input` and `output` directory to `/output`.

Then the `script` located inside the `/input` directory is launched to compile the code. A zip file named after `filename` and containing your compiled code must be generated inside the `output` directory.