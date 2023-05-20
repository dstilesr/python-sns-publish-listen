
resource "aws_sns_topic" "publish_subscribe" {
  name         = "publish-subscribe-poc"
  display_name = "SNS POC Topic"
}
