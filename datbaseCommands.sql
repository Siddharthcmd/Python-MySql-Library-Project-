create database MainLibraryDatabase;
use MainLibraryDatabase;

CREATE TABLE PUBLISHER(
	NAME VARCHAR (20) PRIMARY KEY,
	PHONE varchar(10),
	ADDRESS VARCHAR(20)
    );

create table Book (
	book_id integer primary key,
	title varchar(20),
    author varchar(20),
    publisher varchar(20),
    year_of_publish integer,
    foreign key (publisher) references PUBLISHER (NAME) on delete cascade
    );
    
create table LibraryBranch(
	branchId integer primary key,
    branchName varchar(20),
    branchAddress varchar(20)
    );

CREATE TABLE BOOK_COPIES(
	NoOfCopies INTEGER,
	bookId integer,
	branchId integer, foreign key(branchId) REFERENCES LibraryBranch (branchId) ON DELETE
	CASCADE, foreign key (bookId) REFERENCES Book (book_id) ON DELETE CASCADE,
	PRIMARY KEY (bookId,branchId)
    );

CREATE TABLE BOOK_LENDING(
	DATE_OUT date,
	DUE_DATE date,
	BOOK_ID integer, foreign key(BOOK_ID) REFERENCES Book (book_id) ON DELETE CASCADE,
	BRANCH_ID integer, foreign key(BRANCH_ID) references LibraryBranch (branchId) ON DELETE CASCADE,
	CARD_NO integer,
	primary key(BOOK_ID,BRANCH_ID,CARD_NO)
	);

delimiter //
create trigger decrement
after insert on BOOK_LENDING
FOR each row
begin
UPDATE BOOK_COPIES SET NoOfCopies=NoOfCopies-1 where bookId=new.BOOK_ID and branchId=new.BRANCH_ID;
end;//
delimiter ;


delimiter //
create trigger increment
after delete on BOOK_LENDING
FOR each row
begin
UPDATE BOOK_COPIES SET NoOfCopies=NoOfCopies+1 where bookId=old.BOOK_ID and branchId=old.BRANCH_ID;
end;//
delimiter ;
