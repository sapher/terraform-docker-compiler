output "input_sha" {
  value = "${data.external.input_sha.result["sha"]}"
}

output "output_sha" {
  value = "${data.external.output_exist.result["exist"]}"
}

output "filepath" {
  value = "${var.output}/${var.filename}"
}
