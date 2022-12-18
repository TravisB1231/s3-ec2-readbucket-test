provider "aws" {
  region = "us-east-1"
}
resource "aws_s3_bucket" "experiment-bucket" {
  bucket = "tb-support-private-bucket"
}
resource "aws_s3_bucket_acl" "exp-acl" {
  bucket = aws_s3_bucket.experiment-bucket.id
  acl    = "private"
}
resource "aws_s3_bucket_policy" "exp-pol" {
  bucket = aws_s3_bucket.experiment-bucket.id
  policy = jsonencode(
    {
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Sid" : "Statement1",
          "Effect" : "Allow",
          "Principal" : {
            "AWS" : [
              "${aws_iam_role.s3-access-role.arn}"
            ]
          },
          "Action" : [
            "s3:GetObject"
          ],
          "Resource": "arn:aws:s3:::${aws_s3_bucket.experiment-bucket.bucket}/*"
        }
      ]
  })
}
