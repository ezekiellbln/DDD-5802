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
