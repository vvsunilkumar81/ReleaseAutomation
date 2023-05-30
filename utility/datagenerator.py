"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string
import utility.custom_logger as cl
import logging
import csv
from csv import reader
from csv import DictReader
from resources import tsconfig as utils
import shutil
from datetime import datetime
from datetime import datetime as dt, timedelta
from pytz import timezone
from faker import Faker


class DataGenerator(object):
    log = cl.customLogger(logging.INFO)
    randomString = ''.join((random.choice(string.ascii_lowercase) for x in range(4)))
    ind_time = dt.now(timezone("Asia/Kolkata"))
    currDay = ind_time.strftime("%A")
    currMonth = ind_time.strftime("%B")
    emaildomain = "mailnesia.com"
    currTime = ind_time.strftime("%d%m%Y%H%M%S")
    Faker.seed(0)


    def getNhLastName(self):
        return "AutLast" + self.currDay + self.currMonth + self.randomString

    def getCurrTime(self):
        return self.currTime

    def getNhFirstName(self):
        return "AutFirst" + self.currDay + self.currMonth + self.randomString

    def getNhUsername(self):
        return "aut" + self.currDay + self.currMonth + self.randomString

    def getNhemail(self):
        email = self.getNhUsername() + "@mailnesia.com"
        return email

    def getReqNumber(self):
        return random.randint(20000, 500000)

    def write_header(selfself, filein, test_name, workflowname):
        with open(filein, mode='w') as newhire_file:
            nh_writer = csv.writer(newhire_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # way to write to csv file
            header = ['FirstName', 'LastName', 'UserName', "E-mail", "ReqNumber", "Workflow", "TestName"]
            nh_writer.writerow(header)

    def writing_data_csv(self, filein, test_name, workflowname):
        with open(filein, mode='a') as newhire_file:
            nh_writer = csv.writer(newhire_file, delimiter=',', quotechar='"', skipinitialspace=True,
                                   quoting=csv.QUOTE_MINIMAL)
            nh_writer.writerow(
                [test_name, self.getNhFirstName(), self.getNhLastName(), self.getNhUsername(), self.getNhemail(),
                 self.getReqNumber(), workflowname])

            return True
        newhire_file.close()

    def remove_duplicate(self, filein, fileout):

        with open(filein, 'r') as in_file, open(fileout, 'w') as out_file:
            seen = set()
            for line in in_file:
                if line in seen:
                    continue  # skip duplicate

                seen.add(line)
                out_file.write(line)
            return True

    def getdata(self, file_in, test_name, workflow_name):

        self.writing_data_csv(file_in, test_name, workflow_name)

        with open(file_in, 'r') as read_obj:
            csvFile = csv.DictReader(read_obj)

            # displaying the contents of the CSV file
            for lines in csvFile:
                if lines['TestName'] == test_name:
                    return (
                        lines['FirstName'], lines['LastName'], lines['UserName'], lines['E-mail'], lines['ReqNumber'])
        read_obj.close()

# c = DataGenerator()
# test=c.getdata(utils.testdata_filepath, "CreateNewhire3","CreateNewhire", "BWS_I9_SIMPLE")
# print(test[0])
# print(test[1])
# print(test[2])
# print(test[3])
# print(test[4])
