#!"C:\\Program Files\\Python36\\python.exe"

import _mysql
import logging
log_fname = "my_account_app.log"
logging.basicConfig(filename=log_fname,
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                   )

logger = logging.getLogger(__name__)
conn = _mysql.connect("localhost", "root", "root")
try:
    conn.query("create database banking_teja")
except Exception as e:
    logger.debug("Error create database")
    logger.exception(e)

conn = _mysql.connect("localhost", "root", "root", "banking_teja")
logger.debug("Connected to database")
logger.debug("DB operations started....")
try:
    logger.debug("Trying to create tables")

    conn.query(''' 
    CREATE TABLE IF NOT EXISTS `account` (
    `ac_no` varchar(45) NOT NULL,
    `ac_name` varchar(45) default NULL,
    `ac_branch` varchar(45) default NULL,
    `ac_bank` varchar(45) default NULL,
    `ac_bal` int(11) default NULL,
    PRIMARY KEY  (`ac_no`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1
    ''')
    conn.commit()

    conn.query(''' 
    CREATE TABLE IF NOT EXISTS `payee` (
    `ac_no` varchar(45) NOT NULL,
    `ac_name` varchar(45) default NULL,
    `ac_bank` varchar(45) default NULL,
    PRIMARY KEY  (`ac_no`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1
    ''')
    conn.commit()

    conn.query(''' 
    CREATE TABLE IF NOT EXISTS `user_registration` (
    `AC_NO` varchar(45) NOT NULL,
    `AC_NAME` varchar(45) default NULL,
    `AC_BRANCH` varchar(45) default NULL,
    `AC_PWD` varchar(45) default NULL,
    PRIMARY KEY  (`AC_NO`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1
    ''')
    conn.commit()
except Exception as e:
    logger.debug("Error creating tables")
    logger.exception(e)
logger.debug("Tables created.. ")

try:
    logger.debug("Inserting data")
    conn.query("INSERT INTO `user_registration` VALUES ('1234','Teja','RR Nagar','1234')")
    conn.query("INSERT INTO `account` VALUES ('1234','Brahma Teja P','RR Nagar','HDFC',104739),('1235','Ernesto','Bhavanipuram','SBI',113646),('1236','Pramod','Gannavaram','ICICI',90000)")
    conn.commit()
except Exception as e:
    logger.debug("Error inserting data into tables")
    logger.exception(e)
logger.debug("DB operations done....")


class Authentication(object):

    
    def login(ac_no,paswd):
        logger.debug("Checking login from db...")
        conn.query("select ac_no, ac_pwd from user_registration where ac_no='{}'".format(ac_no))
        res = conn.store_result()
        row = res.fetch_row(maxrows=1)
        logger.debug("row returned " + str(row))
        status = False
        if len(row)>0:
            ac,pw = row[0]
            ac = str(ac,'utf-8')
            pw = str(pw,'utf-8')
            
            status = (ac == ac_no) and (pw == paswd)
        logger.debug("Login status {}".format(status))
        return status

    
    def update_password(ac_no, paswd):
        logger.debug("Updating the passowd for account {} with password {}".format(ac_no,paswd))
        logger.debug("quer is "+"update user_registration set ac_pwd = '{}' where ac_no='{}'".format(paswd,ac_no))
        conn.query("update user_registration set ac_pwd = '{}' where ac_no='{}'".format(paswd,ac_no))
        conn.commit()
        logger.debug("passowrd updated")
        res = conn.store_result()


    def get_acc_details(ac_no):
        logger.debug("Getting the account details for account {}".format(ac_no))
        conn.query("select * from account where ac_no='{}'".format(ac_no))
        res = conn.store_result()
        row = res.fetch_row(maxrows=1)
        logger.debug("Records recieved {}".format(row))
        if (len(row)>0):
            return row[0]
        else:
            return None


    def get_all_acc_details():
        logger.debug("Getting all records in the account table")
        conn.query("select * from account")
        res = conn.store_result()
        logger.debug("Returning result set {}".format(res))
        return res


    
    def register_user(ac_no,ac_name,ac_branch,paswd):
        status = None
        logger.debug("Registering the user with ac_no {} ac_name {} ac_branch {} paswd {}".format(ac_no,ac_name,ac_branch,paswd))
        res = Authentication.get_acc_details(ac_no)
        if res is None:
            logger.debug ("User not exists in Account database")
            status = "NU"
        else:
            try:
                logger.debug("Trying to register user using query below")
                logger.debug("insert into user_registration values('{}', '{}', '{}', '{}')".format(ac_no, ac_name, ac_branch, paswd))
                conn.query("insert into user_registration values('{}', '{}', '{}', '{}')".format(ac_no, ac_name, ac_branch, paswd))
                conn.commit()
                status = "UC"
            except Exception as e:
                logger.debug ("Error registering.. User already exists in the database")
                logger.exception(e)
                status = "UE"
        logger.debug("Returning status {} ".format(status))
        return status


class Account(object):

    def add_payee(ac_no, ac_name, ac_bank):
        status = False
        msg = ""
        details = Authentication.get_acc_details(ac_no)
        logger.debug("Adding payee to the db with ac_no {}, ac_name {}, ac_bank {}".format(ac_no,ac_name,ac_bank))
        if details is not None:
            try:
                logger.debug ("Details present in db for ac_no {}".format(ac_no))
                conn.query("insert into payee values('{}', '{}', '{}') ".format(ac_no, ac_name, ac_bank))
                conn.commit()
                conn.query("select ac_no from payee where ac_no = '{}' ".format(ac_no))
                res = conn.store_result()
                row = res.fetch_row(maxrows=1)
                logger.debug (row)
                status = True
                msg = "Payee Added successfully"
            except Exception as e:
                msg = "Payee already added"
        else:
            msg = "Particular account details not present in db"
        
        return (status, msg)


    def remove_payee(ac_no, ac_bank):
        conn.query("delete from payee where ac_no = '{}' and ac_bank ='{}' ".format(ac_no, ac_bank))
        conn.commit()

        return True
        # conn.query("select ac_no, ac_bank from payee where ac_no = '{}' and ac_bank ='{}' ".format(ac_no, ac_bank))
        # res = conn.store_result()
        # rows = res.fetch_row(maxrows=1)
        # if len(rows) ==0:
        #     return True
        # else:
        #     return False

    def money_transfer(ac_no, ac_bank, amount):
        status = False
        logger.debug("transfering money")
        logger.debug("recieved details ac_no {}, ac_bank {}, amount {}".format(ac_no, ac_bank, amount))
        d = Authentication.get_acc_details(ac_no)
        logger.debug ("Previous balance record {}".format(d))
        
        if (d is not None):
            pre_bal = int(d[4])
            new_bal = int(amount) + pre_bal
            conn.query("update account set ac_bal={} where ac_no = '{}'".format(new_bal,ac_no))
            conn.commit()
            d = Authentication.get_acc_details(ac_no)
            logger.debug("Record after update {}".format(d))
            temp = int(d[4])
            status =  True
            return status
        else:
            return status


#print(Account.money_transfer('1234','test','1000'))