provider "heroku" {
  version = "~> 2.3"
}

variable "my-api-application-name" {
  description = "Application name for the API"
}

resource "heroku_app" "api-server" {
  name   = var.my-api-application-name
  region = "eu"
}

 resource "heroku_build" "api-server" {
   app = heroku_app.api-server.name
   buildpacks = ["https://github.com/heroku/heroku-buildpack-python"]

   source = {
     url      = "https://github.com/Akhilian/ZDD-workshop/archive/v0.2.0.tar.gz"
     version  = "v0.2.0"
   }
 }


output "api-server-url" {
  value = "https://${heroku_app.api-server.name}.herokuapp.com"
}