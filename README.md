# NOAA Global Marine Data

### A set of Terraform modules and Flyway Migration scripts for storing NOAA global marine data from -10_-10_-20_00.csv. 

## Notes:
1. TF variables can be passed in on command line or via terraform.tfvars (not included in this repo).
2. Need an Entra ID account with appropriate permissions to create the associated resources (not included in this repo). 
3. Need Entra ID account(s) to be used for SQL Server Azure AD administrator.
4. Environment variables:
  - $env:SERVER = "SERVERNAME"
  - $env:USER = "USERNAME"
  - $env:PASS = "PASSWORD"
  - $env:DATA = "PATHTOCSVDATA"
  - $env:DATABASE = "DATABASENAME"
5. IF YOU MODIFY THE TABLE STRUCTURE, you MUST manually generate the SQL Server BCP FMT file: bcp [SCHEMA].[TABLE] format nul -d $env:DATABASE -S $env:SERVER. -U $env:USER -P $env:PASS -f $env:DATA\$stations.fmt -c -t "," -r "\r\n".

## Recommendations: Manually create a SQL database with the Azure Portal using the "Want to try Azure SQL Database for free?" offer.

### What you get:
1. An Azure SQL Server.
2. A staging schema.
3. A stations table.
4. A SQL Server BCP FMT file for the NOAA NCEI global marine data.
4. A Python script to preprocess the raw CSV files
5. 4095 records of global marine data for March 2025. 

### Missing:
1. An Azure SQL Database. Why? Because there is no way to take advantage of the "free" offer with Terraform.
2. -10_-10_-20_00.csv: The NOAA NCEI global marine data. Download from: https://www.ncei.noaa.gov/data/global-marine/. WARNING: The NOAA NCEI CSV files have varying numbers of fields. The files require preprocessing with preprocess.py.

### STEPS:
1. Run TF to create the Azure SQL Server
2. Manually create an Azure SQL Database (free trial)
3. Set the environment variables (see Notes)
4. Preprocess at least 1 CSV file: python preprocess.py -- -10_-20_-20_-10.csv -10_-20_-20_-10_pre.csv
5. Run Flyway to create the schema, table, and load data with callback script
6. (Optional) Load more data: bcp SCHEMA.TABLE in .\FILENAME.csv -d $env:DATABASE -S $env:SERVER -e .\FILENAME_pre.err -G -U "$env:USER" -P ${env:PASS}-f .\stations.fmt -F 2
7. (Optional) Clean up: flyway -url="jdbc:sqlserver://${env:SERVER}:1433;database=${env:DATABASE};encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;authentication=ActiveDirectoryPassword" -user="${env:USER}" -password="${env:PASS}" -cleanDisabled=false clean

