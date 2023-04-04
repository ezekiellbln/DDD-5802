Create database Exercise1;
Create table EMP_1
(
EMP_Num Char(3),
EMP_Lname Varchar(15),
EMP_Fname Varchar(15),
EMP_Initial Char(1),
EMP_Hiredate date,
Job_Code Char(3)
)
;
Insert into EMP_1 (EMP_Num, EMP_Lname, EMP_Fname, EMP_Initial, EMP_Hiredate, Job_Code)
	value ('1', 'Bönsch', 'Stephan', 'T', '2022-11-29', '501'),
        ('2', 'Narfidort', 'Fischl', 'L', '2023-05-03', '502'),
        ('3', 'Brötzmann', 'Elia', 'A', '2002-07-25', '503');
Select * From EMP_1 Where Job_Code = '502';

Select * From EMP_1;
Delete from exercise1.EMP_1 where EMP_Num = '1';
Delete from exercise1.EMP_1 where EMP_Num = '2';
Delete from exercise1.EMP_1 where EMP_Num = '3';

Insert into exercise1.EMP_1 (EMP_Num, EMP_Lname, EMP_Fname, EMP_Initial, EMP_Hiredate, Job_Code)
	Value ('101', 'Nevas', 'John', 'G', '1994-11-08', '502'),
		('102', 'Senior', 'David', 'H', '1987-07-12', '501'),
        ('103', 'Arbos', 'June', 'E', '1996-12-01', '500'),
        ('104', 'Ramoras', 'Anne', 'K', '1998-11-15', '501'),
        ('105', 'Joson', 'Alice', 'P', '1993-02-01', '502'),
        ('106', 'Smith', 'William', 'D', '1990-06-23', '500'),
        ('107', 'Alonso', 'Mara', 'F', '1991-10-10', '500'),
        ('108', 'Washington', 'Raf', 'S', '1989-08-22', '501'),
        ('109', 'Field', 'Larry', 'W', '1999-07-18', '501');
        
Update exercise1.EMP_1 set Job_Code = '501' where EMP_Num = '106';

SET SQL_SAFE_UPDATES = 0;
Delete from exercise1.EMP_1 where EMP_Lname = 'Smith';
