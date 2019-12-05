provider "external" {}

data "external" "input_sha" {
  program = ["python", "${path.module}/scripts/sha.py"]

  query = {
    dir = var.input
  }
}

data "external" "output_exist" {
  program = ["python", "${path.module}/scripts/file.py"]

  query = {
    file = "${var.output}/${var.filename}"
  }
}

resource "null_resource" "make" {
  triggers = {
    input_sha = data.external.input_sha.result["sha"]
    output_exist = data.external.output_exist.result["exist"]
  }

  provisioner "local-exec" {
    command = "${path.module}/scripts/build.py"

    environment = {
      IMAGE      = var.image
      INPUT_DIR  = var.input
      OUTPUT_DIR = var.output
      SCRIPT     = var.script
      FILENAME   = var.filename
    }
  }

  provisioner "local-exec" {
    when    = "destroy"
    command = "rm -f ${var.output}/${var.filename}"
  }
}
