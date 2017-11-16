import pymysql
import json
import sys
import logging
import DbConfig as cfg

# RDS configurations
rds_host = cfg.mysql['host']
name = cfg.mysql['user']
password = cfg.mysql['passwd']
db_name = cfg.mysql['db']

fields = "employeeid,name,dept,salary"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")


def handler(event, context):
    values = event['employeeid'] + "," + event['name'] + event['dept'] + ",'" + event['salary']

    item_count = 0
    with conn.cursor() as cur:
        cur.execute('insert into employee (' + fields + ') values(' + values + ')')
    conn.commit()
    cur.execute("select * from employee")
    for row in cur:
        item_count += 1
        logger.info(row)
        # print(row)
    return "Added %d items from RDS MySQL table" % (item_count)
