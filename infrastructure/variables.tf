variable "region" {
  type        = string
  default     = "us-west-2"
  description = "Region in which to deploy resources"
}

variable "topic_name" {
  type        = string
  default     = "publish-subscribe-poc"
  description = "Name of the SNS topic to create"
}
