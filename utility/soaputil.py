import shutil
import time
import traceback
import random, string
import utility.custom_logger as cl
import logging
import requests
import xml.dom.minidom as md


class SoapUtil():

    def sendPayload(self, file, client, reqid, workflow, hiringmanager, recruiter, jobstate, username, firstname,
                    lastname,
                    email, filepath, fileoutput,url):
        f = open(file, encoding="iso-8859-1")
        file = md.parse(f)
        clientname = file.getElementsByTagName("client")
        clientname[0].firstChild.nodeValue = client
        reqNumber = file.getElementsByTagName("reqid")
        reqNumber[0].firstChild.nodeValue = reqid
        requisitionNo = file.getElementsByTagName("reqNo")
        requisitionNo[0].firstChild.nodeValue = reqid
        cruId = file.getElementsByTagName("Cruid")
        cruId[0].firstChild.nodeValue = reqid
        nhCountry = file.getElementsByTagName("Country")
        nhCountry[0].firstChild.nodeValue = "United States"
        jobworkflow = file.getElementsByTagName("workFlow")
        jobworkflow[0].firstChild.nodeValue = workflow
        primaryhm = file.getElementsByTagName("PrimaryHiringManager")
        primaryhm[0].firstChild.nodeValue = hiringmanager
        primaryrecruiter = file.getElementsByTagName("PrimaryRecruiter")
        primaryrecruiter[0].firstChild.nodeValue = recruiter
        stateofjob = file.getElementsByTagName("stateOrProvince")
        stateofjob[0].firstChild.nodeValue = jobstate
        nhusername = file.getElementsByTagName("userName")
        nhusername[0].firstChild.nodeValue = username
        print("UserName: " + nhusername[0].firstChild.nodeValue)
        nhfirstname = file.getElementsByTagName("FirstName")
        nhfirstname[0].firstChild.nodeValue = firstname
        print("Firstname: " + nhfirstname[0].firstChild.nodeValue)
        nhlastname = file.getElementsByTagName("LastName")
        nhlastname[0].firstChild.nodeValue = lastname
        print("LastName: " + nhlastname[0].firstChild.nodeValue)
        nhemail = file.getElementsByTagName("emailAddress")
        nhemail[0].firstChild.nodeValue = email
        print("Newhire Email: " + nhemail[0].firstChild.nodeValue)
        with open(filepath, "w") as fs:
            fs.write(file.toxml())
            fs.close()
            shutil.copyfile(filepath, fileoutput)
        return self.postPayload(url, fileoutput)

    def postPayload(self, url, filepath):
        XML_STRING = open(filepath).read()
        xml = XML_STRING.encode('UTF-8')
        headers = {'Content-Type': 'text/xml;charset=UTF-8'}
        response = requests.request("POST", url, headers=headers, data=xml)
        return response.text

    def sendPayload_iqa(self, file, client, reqid, workflow, hiringmanager, recruiter, jobstate, username, firstname,
                    lastname,
                    email,nh_ssn, filepath, fileoutput, url):
        f = open(file, encoding="iso-8859-1")
        file = md.parse(f)
        clientname = file.getElementsByTagName("client")
        clientname[0].firstChild.nodeValue = client
        reqNumber = file.getElementsByTagName("reqid")
        reqNumber[0].firstChild.nodeValue = reqid
        cruId = file.getElementsByTagName("Candidate_ref_number")
        cruId[0].firstChild.nodeValue = reqid
        nhCountry = file.getElementsByTagName("CountryCode")
        nhCountry[0].firstChild.nodeValue = "United States"
        jobworkflow = file.getElementsByTagName("workFlow")
        jobworkflow[0].firstChild.nodeValue = workflow
        primaryhm = file.getElementsByTagName("manager")
        primaryhm[0].firstChild.nodeValue = hiringmanager
        primaryrecruiter = file.getElementsByTagName("recruiter")
        primaryrecruiter[0].firstChild.nodeValue = recruiter
        stateofjob = file.getElementsByTagName("stateOrProvince")
        stateofjob[0].firstChild.nodeValue = jobstate
        nhfirstname = file.getElementsByTagName("GivenName")
        nhfirstname[0].firstChild.nodeValue = firstname
        print("Firstname: " + nhfirstname[0].firstChild.nodeValue)
        nhlastname = file.getElementsByTagName("LegalName")
        nhlastname[0].firstChild.nodeValue = lastname
        print("LastName: " + nhlastname[0].firstChild.nodeValue)
        uname = file.getElementsByTagName("Id")
        uname[6].lastChild.nodeValue = username

        nhemail = file.getElementsByTagName("InternetEmailAddress")
        nhemail[0].firstChild.nodeValue = email
        print("Newhire Email: " + nhemail[0].firstChild.nodeValue)
        nssn = file.getElementsByTagName("Id")
        nssn[6].lastChild.nodeValue = nh_ssn

        with open(filepath, "w") as fs:
            fs.write(file.toxml())
            fs.close()
            shutil.copyfile(filepath, fileoutput)
        return self.postPayload(url, fileoutput)
