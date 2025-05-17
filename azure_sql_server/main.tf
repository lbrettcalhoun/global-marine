terraform {
  required_version = ">= 1.11.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_mssql_server" "self" {
  name                         = var.server_name
  azuread_administrator {
    login_username = var.admin_username
    object_id = var.admin_id
    azuread_authentication_only = true
  }
  location                     = var.location
  resource_group_name          = var.resource_group_name

  version                      = "12.0"
}

resource "azurerm_mssql_firewall_rule" "self" {
  name             = "OnPrem"
  server_id        = azurerm_mssql_server.self.id
  start_ip_address = var.ip
  end_ip_address   = var.ip
}


