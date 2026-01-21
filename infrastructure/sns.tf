
resource "aws_sns_topic" "publish_subscribe" {
  name         = var.topic_name
  display_name = "SNS POC Topic"
}
