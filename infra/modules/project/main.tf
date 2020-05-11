resource "aws_db_instance" "database" {
  engine         = "postgres"
  engine_version = "10.12"

  allocated_storage    = 20
  storage_type         = "gp2"
  instance_class       = "db.t2.micro"
  name                 = "plane_tracker"
  username             = "captain"
  password             = "captainsully"
  parameter_group_name = "default.postgres10"
  skip_final_snapshot  = true
}

output "database_endpoint" {
  value = aws_db_instance.database.endpoint
}