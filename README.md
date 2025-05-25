# NOAA Global Marine Data

### A set of Terraform modules and Flyway Migration scripts for storing NOAA global marine data from -10_-10_-20_00.csv. 

## Notes:
1. TF variables can be passed in on command line or via terraform.tfvars (not included in this repo).
2. Need an Entra ID account with appropriate permissions to create the associated resources (not included in this repo). 
3. Need Entra ID account(s) to be used for SQL Server Azure AD administrator.
4. Environment variables must be manually created for the Flyway callback script afterMigrations.ps1:
  - $env:SERVER = "SERVERNAME"
  - $env:USER = "USERNAME"
  - $env:PASS = "PASSWORD"
  - $env:DATA = "PATHTOCSVDATA\"
5. You MUST manually edit the NOAA NCEI March 2025 CSV file (-10_-10_-20_00.csv): remove all double quotes. Do this step BEFORE you run the Flyway migration.
6. IF YOU MODIFY THE TABLE STRUCTURE, you MUST manually generate the SQL Server BCP FMT file: bcp [SCHEMA].[TABLE] format nul -d DATABASENAME -S "SERVERNAME" -U "USERNAME" -P PASSWORD -f .\data\stations.fmt -c -t "," -r "\n".
7. IF YOU GENERATE THE SQL SERVER BCP FMT FILE, you MUST manually edit the FMT file: change "\r\n" to "\n"

## Recommendations: Manually create a SQL database with the Azure Portal using the "Want to try Azure SQL Database for free?" offer.

### What you get:
1. An Azure SQL Server.
2. A staging schema.
3. A stations table.
4. A SQL Server BCP FMT file for the NOAA NCEI global marine data.
5. 4095 records of global marine data for March 2025. 

### Missing:
1. An Azure SQL Database. Why? Because there is no way to take advantage of the "free" offer with Terraform.
2. -10_-10_-20_00.csv: The NOAA NCEI global marine data. Download from: https://www.ncei.noaa.gov/data/global-marine/. WARNING: The NOAA NCEI CSV files have varying numbers of fields. This repo works only with -10_-10_-20_00.csv.

### STEPS:
1. Run TF to create the Azure SQL Server
2. Manually create an Azure SQL Database (free trial)
3. Run Flyway to create the schema, table, and load data with callback script

