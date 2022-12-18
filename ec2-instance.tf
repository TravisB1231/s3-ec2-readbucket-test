resource "aws_instance" "exp-instance" {
  ami           = "ami-0574da719dca65348"
  instance_type = "t2.micro"
  iam_instance_profile = aws_iam_instance_profile.inst-profile.name

  tags = {
    Name        = "tb-support-ubuntu-tf-s3-exp"
  }
}