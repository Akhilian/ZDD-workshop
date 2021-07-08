data "aws_iam_policy_document" "asa_personal_access" {
  statement {

    actions = [
      "iam:Get*Role*",
      "iam:List*Role*",
      "iam:PassRole",
    ]

    resources = [
      "<name of the role>" # "arn:aws:iam::<aws_account_number>:role/ecs_tasks_access"
    ]
  }

  statement {

    actions = [
      "iam:*InstanceProfile*",
    ]

    resources = [
      "*",
    ]
  }
}