/****** Object:  Table [staging].[stations]    Script Date: 5/25/2025 10:59:45 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[staging].[stations]') AND type in (N'U'))
DROP TABLE [staging].[stations]
GO
