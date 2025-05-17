# NOAA Global Marine Data

### A set of Terraform modules for storing NOAA global marine data

## Notes:
1. Variables can be passed in on command line or via terraform.tfvars (not included in this repo).
2. Need an Entra ID account with appropriate permissions to create the associated resources (not included in this repo). 
3. Need Entra ID account(s) to be used for SQL Server Azure AD administrator.

## Recommendations: Manually create a SQL database with the Azure Portal using the "Want to try Azure SQL Database for free?" offer.

### What you get:
1. An Azure SQL Server.

### Missing:
1. An Azure SQL Database. Why? Because there is no way to take advantage of the "free" offer with Terraform.

