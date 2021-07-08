resource "aws_ecs_task_definition" "api" {
    family                  = "zdd-workshop-api-asa"
    cpu                     = 512
    memory                  = 1024
    container_definitions   = templatefile("${path.module}/task_definition.json", {
        task_name       = "zdd-workshop-api-asa",
        task_image      = "akhilian/atelier-zdd-plane:latest",
        database_uri    = aws_db_instance.database.endpoint,
        log_group_region = "eu-west-1",
        log_group_stream_prefix = "api_asa"
    })
    network_mode            = "awsvpc"
    requires_compatibilities = ["FARGATE"]
}

data "aws_ecs_cluster" "atelier_zdd" {
    cluster_name = "atelier_zdd"
}

resource "aws_ecs_service" "api" {
    name            = "zdd-workshop-api-asa"
    cluster         = data.aws_ecs_cluster.atelier_zdd.arn
    task_definition = aws_ecs_task_definition.api.arn
    desired_count   = 2
    launch_type     = "FARGATE"

    load_balancer {
        container_name      = aws_ecs_task_definition.api.family
        container_port      = 80
        target_group_arn    = aws_lb_target_group.api.arn
    }

    network_configuration {
        subnets         = [aws_subnet.subnet_zone_a.id, aws_subnet.subnet_zone_b.id]
        security_groups = [aws_security_group.private_ecs.id]
        assign_public_ip = true
    }

    depends_on  = [aws_alb_listener.api]
}

resource "aws_security_group" "private_ecs" {
    name        = "private_ecs_asa"
    description = "Private access to ECS"
    vpc_id      = aws_vpc.default.id
}

resource "aws_security_group_rule" "private_ingress_from_port_80" {
    type              = "ingress"
    from_port         = 0
    to_port           = 0code 
    protocol          = "tcp"
    cidr_blocks       = [aws_vpc.default.cidr_block]
    security_group_id = aws_security_group.private_ecs.id
}

resource "aws_security_group_rule" "private_egress_to_any_port_in_vpc" {
    type              = "egress"
    from_port         = 0
    to_port           = 65535
    protocol          = "tcp"
    cidr_blocks       = ["0.0.0.0/0"]
    security_group_id = aws_security_group.private_ecs.id
}


resource "aws_alb" "api" {
    name        = "lb-api-asa"
    load_balancer_type = "application"
    subnets     = [aws_subnet.subnet_zone_a.id, aws_subnet.subnet_zone_b.id]
    security_groups = [aws_security_group.public_api_alb.id]
}

resource "aws_security_group" "public_api_alb" {
    name        = "public_api_alb-asa"
    description = "Public Access for API ALB"
    vpc_id      = aws_vpc.default.id
}

resource "aws_security_group_rule" "ingress_from_port_80" {
    type              = "ingress"
    from_port         = 80
    to_port           = 80
    protocol          = "tcp"
    cidr_blocks       = ["0.0.0.0/0"]
    security_group_id = aws_security_group.public_api_alb.id
}

resource "aws_security_group_rule" "egress_to_any_port_in_vpc" {
    type              = "egress"
    from_port         = 0
    to_port           = 0
    protocol          = "tcp"
    cidr_blocks       = [aws_vpc.default.cidr_block]
    security_group_id = aws_security_group.public_api_alb.id
}

resource "aws_lb_target_group" "api" {
    name        = "zdd-workshop-api-asa"
    port        = 80
    protocol    = "HTTP"
    vpc_id      = aws_vpc.default.id
    target_type = "ip"

    health_check {
        path        = "/status"
        port        = 80
        protocol    = "HTTP"
    }

    depends_on  = [aws_alb.api]
}

resource "aws_alb_listener" "api" {
    load_balancer_arn   = aws_alb.api.arn
    port                = "80"
    protocol            = "HTTP"

    default_action {
        type             = "forward"
        target_group_arn = aws_lb_target_group.api.arn
    }
}

# resource "aws_cloudwatch_log_group" "api" {
#   name = "zdd-workshop-api-asa"

#   tags = {
#     Application = "API"
#   }

#   retention_in_days = 1
# }