IF NOT EXISTS (SELECT name FROM sys.schemas WHERE name = N'staging')
  EXEC('CREATE SCHEMA [staging] AUTHORIZATION [dbo]');
GO