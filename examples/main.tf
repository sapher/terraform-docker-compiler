module "compilator" {
  source   = "git://github.com/sapher/terraform-docker-compiler"
  image    = "node:8.16.0-alpine"
  input    = "${abspath(path.module)}/input"
  output   = "${abspath(path.module)}/output"
  script   = "script.sh"
  filename = "lambda.zip"
}
