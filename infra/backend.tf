terraform {
  backend "s3" {
    bucket = "ansible-buckets-45673483"
    region = "eu-west-2"
    key    = "ansible/terraform.tfstate"
  }
}