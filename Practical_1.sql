Create Database ABC_Computer;
Create table Computer
	(SerialNumber int,
    Make Varchar(12),
    Model Varchar(24),
    ProcessorType Varchar(24),
    ProcessorSpeed Int,
    MainMemory Varchar(15),
    DiskSize Varchar(15));
Select * from Computer;
Insert into Computer (SerialNumber, Make, Model, ProcessorType, ProcessorSpeed, MainMemory, DiskSize)
		Value ("9871234", "HP", "Pavillion 500-210qe", "intel i5-4530", "3.00", "6.0 Gbytes", "1.0 Tbytes"),
        ("9871245", "HP", "Pavilion 500-210qe", "Intel i5-4531", "3.00", "6.0 Gbytes", "1.0 Tbyte"),
        ("9871256", "HP", "Pavilion 500-210qe", "Intel i5-4532", "3.00", "6.0 Gbytes", "1.0 Tbytes"),
        ("9871267", "HP", "Pavilion 500-210qe", "Intel i5-4533", "3.00", "6.0 Gbytes", "1.0 Tbytes"),
        ("9871278", "HP", "Pavilion 500-210qe", "Intel i5-4534", "3.00", "6.0 Gbytes", "1.0 Tbytes"),
        ("9871289", "HP", "Pavilion 500-210qe", "Intel i5-4535", "3.00", "6.0 Gbytes", "1.0 Tbytes"),
        ("6541001", "Dell", "OptiPlex 9020", "Intel i7-4770", "3.00", "8.0 Gbytes", "1.0 Tbytes"),
        ("6541002", "Dell", "OptiPlex 9021", "Intel i7-4771", "3.00", "8.0 Gbytes", "1.0 Tbytes"),
        ("6541003", "Dell", "OptiPlex 9022", "Intel i7-4772", "3.00", "8.0 Gbytes", "1.0 Tbytes"),
        ("6541004", "Dell", "OptiPlex 9023", "Intel i7-4773", "3.00", "8.0 Gbytes", "1.0 Tbytes"),
        ("6541005", "Dell", "OptiPlex 9024", "Intel i7-4774", "3.00", "8.0 Gbytes", "1.0 Tbytes"),
        ("6541006", "Dell", "OptiPlex 9025", "Intel i7-4775", "3.00", "8.0 Gbytes", "1.0 Tbytes");
Select * from Computer Where Make = "HP";
Select * from Computer Where Make = "Dell"; 
Alter Table Computer Add Column Graphics Varchar(40) not null After DiskSize;
Update Computer Set Graphics = "Integrated Intel HD Graphics 4600";
Alter Table Computer Drop ProcessorSpeed;








