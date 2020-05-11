module "atelier_zdd" {
  source = "../../modules/project"
}

output "database_endpoint" {
  value = module.atelier_zdd.database_endpoint
}

