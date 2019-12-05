terraform-docker-compiler
-----------

A terraform module for compiling any code in terraform with the help of docker.

This module has been created with the service AWS Lambda in mind.

:warning: use at your own risk, any help is appreciated :heart:

# Prerequisite

- **[Docker](https://docs.docker.com/v17.09/engine/installation/#supported-platforms)**
- **[Python](https://realpython.com/installing-python/)** - 
- **[Terraform](https://learn.hashicorp.com/terraform/getting-started/install.html)**
- **[Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)**

You need these programs installed on your host.

# How it works

A docker container is launch using the `image` passed as attribute. It's better to use a very lightweight image here, as it will speed up compilation time.

Two volumes are mounted inside this container, one will bind the `input` directory on your host to `/input` directory on the container and the same for happened with the `output` directory.

Then the `script` located inside the `/input` directory is launched to compile the code. A zip file named after `filename` and containing your compiled code must be generated inside the `output` directory by the script.

This module is generic, it doesn't support any programming language. So you need to create your own compilation script.

# Usage

```terraform
module "compilator" {
  source   = "git://github.com/sapher/terraform-docker-compiler?ref=v0.12"
  input    = "${abspath(path.module)}/input"
  output   = "${abspath(path.module)}/output"
  image    = "node:8.16.0-alpine"
  filename = "lambda.zip"
  script   = "compile.sh"
}
```

:warning: `abspath(path.module)` is need for the module to get the absolute paths

## Attributes

*all attributes are required*

- **input** source directory where your code lives
- **output** output directory where your compiled code would be outputed
- **image** docker image to use
- **filename** name of the output file
- **script** relative script file name inside `input` directory

## Compilation script

Compilation of the actual code is the part that should create yourself. 
The script must compile the code in a directory different than `/input` or `/output`. Only the archive file should be outputed in the folder `/output`.

**Environment variables**

List of variables passed to compilation script :

- **FILENAME** Name of the archive file

**Example**

Here's below an example of a script to compile a npm package with the image `node:8.16.0-alpine`.

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

## Some thoughts

- Will add time to your terraform deployment
- Should not be used in my opinions
- ... :heart: