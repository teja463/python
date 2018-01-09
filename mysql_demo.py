import _mysql

conn = _mysql.connect("localhost", "root", "root")
conn.query("drop database banking_teja")
conn.query("create database banking_teja")
                
conn = _mysql.connect("localhost", "root", "root", "banking_teja")
conn.query(''' CREATE TABLE IF NOT EXISTS `account` (
  `ac_no` varchar(45) NOT NULL,
  `ac_name` varchar(45) default NULL,
  `ac_branch` varchar(45) default NULL,
  `ac_bank` varchar(45) default NULL,
  `ac_bal` int(11) default NULL,
  PRIMARY KEY  (`ac_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1



CREATE TABLE IF NOT EXISTS `payee` (
  `ac_no` varchar(45) NOT NULL,
  `ac_name` varchar(45) default NULL,
  `ac_bank` varchar(45) default NULL,
  PRIMARY KEY  (`ac_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE IF NOT EXISTS `user_registration` (
  `AC_NO` varchar(45) NOT NULL,
  `AC_NAME` varchar(45) default NULL,
  `AC_BRANCH` varchar(45) default NULL,
  `AC_PWD` varchar(45) default NULL,
  PRIMARY KEY  (`AC_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

INSERT INTO `user_registration` VALUES ('1234','Teja','RR Nagar','1234')

INSERT INTO `account` VALUES ('1234','Brahma Teja P','RR Nagar','HDFC',104739),('1235','Ernesto','Bhavanipuram','SBI',113646),('1236','Pramod','Gannavaram','ICICI',90000)
''')
