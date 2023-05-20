output "topic_arn" {
  value = aws_sns_topic.publish_subscribe.arn
}

output "topic_id" {
  value = aws_sns_topic.publish_subscribe.id
}
