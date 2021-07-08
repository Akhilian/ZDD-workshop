output "personal_access_role" {
  value = data.aws_iam_policy_document.asa_personal_access.json
}