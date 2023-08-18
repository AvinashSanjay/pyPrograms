create table eb(cust_id int(6), name varchar(255), toc char(1), prv_reading int(8), new_reading int(8), no_of_units int(6), bill_amount float(8,2));
insert into eb values  (12357, 'yogabalaji', 'H', 233467, 233690, null, null),(12358, 'Dolukbalaji', 'I', 833467, 834690, null, null),(12359, 'balaji', 'C', 294467, 294690, null, null),(12322, 'Guru', 'I', 89467, 89789, null, null),(12377, 'Gokul', 'C', 253467, 253690, null, null);
update table eb set no_of_units=(new_reading-prv_reading);
update table eb set bill_amount=no_of_units*9.8 where toc=='H';
update table eb set bill_amount=no_of_units*21.3 where toc=='I';
update table eb set bill_amount=no_of_units*16 where toc=='C';
