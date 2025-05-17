variable "admin_id" {
  type        = string
  description = "The Object ID of the administrator account."
}

variable "admin_username" {
  type        = string
  description = "The Entra ID administrator account for the SQL server."
}

variable "ip" {
  type = string
  description = "The IP address for the Azure SQL Firewall Rule. "
}

variable "location" {
  type        = string
  description = "The location for the SQL server."
  default     = "eastus"
}

variable "resource_group_name" {
  type = string
  description = "The resource group for the SQL Server/"
}

variable "server_name" {
  type = string
  description = "The name of the SQL Server."
}
