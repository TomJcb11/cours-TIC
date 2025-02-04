USE X_Factor
GO

-- create table of contestants
CREATE TABLE tblFinalist(
	FinalistId int PRIMARY KEY IDENTITY(1,1),
	FinalistName nvarchar(50),
	FinishingPosition int,
	SeriesNumber int,
	CategoryId int,
	ImportNote nvarchar(50)
)


-- create table of categories for contestants
CREATE TABLE tblCategory(
	CategoryId int PRIMARY KEY,
	CategoryName nvarchar(50)
)

-- add in most of the categories
INSERT INTO tblCategory(CategoryId, CategoryName) VALUES (1, N'16-24s')
INSERT INTO tblCategory(CategoryId, CategoryName) VALUES (2, N'Boys')
INSERT INTO tblCategory(CategoryId, CategoryName) VALUES (3, N'Girls')
INSERT INTO tblCategory(CategoryId, CategoryName) VALUES (4, N'Groups')
INSERT INTO tblCategory(CategoryId, CategoryName) VALUES (5, N'Not found')
