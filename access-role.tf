resource "aws_iam_role" "s3-access-role" {
  name      = "tf-s3-access-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
}
resource "aws_iam_policy" "s3-access-policy" {
  name      = "tf-s3-access-policy"
  policy    = jsonencode(
    {
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Effect" : "Allow",
          "Action" : [
            "s3:Get*",
            "s3:Describe*"
          ]
          "Resource" : "${aws_s3_bucket.experiment-bucket.arn}"
        }
      ]
    })
}
resource "aws_iam_role_policy_attachment" "attachment" {
  role       = aws_iam_role.s3-access-role.name
  policy_arn = aws_iam_policy.s3-access-policy.arn
}
resource "aws_iam_instance_profile" "inst-profile" {
  name      = "s3-access-profile"
  role      = aws_iam_role.s3-access-role.name
}