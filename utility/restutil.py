import json
import time
import requests


class RestUtil():

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)

    def gktoken(self, client_name, admin_user, password, token_url):
        authUser = client_name + ":" + admin_user
        postdata = {"client_id": "2xApp", "grant_type": "password", "username": authUser, "client_secret": "admin",
                    "password": password, "user_oauth_approval": "true"}
        response = requests.post(token_url, data=postdata, verify=False)
        print(response)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
        else:
            print(f"Hello,there's a {response.status_code} error with your request")
        return self.getgktoken(response)

    def getgktoken(self, response):
        tokenstring = response.text
        mydict = json.loads(tokenstring)
        return (mydict.get('access_token'))

    def getssoId(self, client_name, token, user_name, query_url):
        bearer_token = 'Bearer' + ' ' + token
        headers = {'Accept-Encoding': 'gzip,deflate', 'Authorization': bearer_token, 'Content-Type': 'application/json'}
        data = {"clientName": client_name, "queryName": "get_specified_users", "params": {"user_name": user_name}}
        qresponse = requests.post(url=query_url, headers=headers, json=data, verify=False)
        qstring = qresponse.text
        print(qstring)
        dict = json.loads(qstring)
        list = dict.get('results')
        key = "sso_id"
        found = False
        for d in list:
            if key in d:
                found = True
                print(f"{key} in query: {d[key]}")
            else:
                pass
        if found == False:
            print(f"query :{key} is not found")
        return str(d[key])

    def updateUserProfile(self, token, sso_id, update_user_url):
        bearer_token = 'Bearer' + ' ' + token
        update_ssourl = update_user_url + sso_id
        headers = {'Accept-Encoding': 'gzip,deflate', 'Authorization': bearer_token, 'Content-Type': 'application/json'}
        data = {"enabled": "true", "passwordExpired": "false", "accountExpired": "false", "accountLocked": "false",
                "password": "QAtest234!"}
        qr_esponse = requests.put(url=f"{update_ssourl}", headers=headers, json=data, verify=False)
        return qr_esponse.text

    def getpasswordtoken(self, token, client_name, user_name, get_password_url):
        bearer_token = 'Bearer' + ' ' + token
        updaate_password_url = get_password_url + client_name + "/password/token"
        headers = {'Accept-Encoding': 'gzip,deflate', 'Authorization': bearer_token,
                   'Content-Type': 'application/json'}

        data = {"username": user_name, "password": "QAtest234!"}
        create_password = requests.post(url=f"{updaate_password_url}", headers=headers, params=data, verify=False)
        token_string = create_password.text
        token_dict = json.loads(token_string)
        return (token_dict.get('access_token'))

    def getChallengeQnsSaveanswers(self, token, client_name, get_password_url):
        bearer_token = 'Bearer' + ' ' + token
        password_challengelist = get_password_url + client_name + "/password/challenge/list"
        headers = {'Accept-Encoding': 'gzip,deflate', 'Authorization': bearer_token, 'Content-Type': 'application/json'}
        getchallenge_qns = requests.get(url=f"{password_challengelist}", headers=headers, verify=False)
        qnsList = getchallenge_qns.json()
        time.sleep(5)
        cQ = 'cQuestions'
        for key, value in qnsList.items():
            if key == 'requiredNumCQ':
                numberOfQuestionsNeeded = value
                print(numberOfQuestionsNeeded)
        for key, value in qnsList.items():
            if key == 'challengeQuestions':
                questionIds = value
            queryParameters = []

        for i in range(5):
            queryParameters.append(
                cQ + "." + str(questionIds[i].get('clientCQuestionId')) + "=" + "answer" + str(i))
            if (i != numberOfQuestionsNeeded):
                queryParameters.append('&')
        str1 = ""
        for ele in queryParameters:
            str1 += ele
        print(str1)
        queryparams = 'dummy&' + str1
        data = {"param": queryparams}
        updaate_passwordurl = get_password_url + client_name + "/password/challenge/save" + "?param=" + queryparams
        savechallenge_qns = requests.post(url=f"{updaate_passwordurl}", headers=headers, verify=False)
        return savechallenge_qns.text

    def resetPassword(self, token, client_name, user_name, password, get_password_url):
        bearer_token = 'Bearer' + ' ' + token
        update_password_url = get_password_url + client_name + "/password/reset"
        headers = {'Accept-Encoding': 'gzip,deflate', 'Authorization': bearer_token, 'Content-Type': 'application/json'}
        data = {"newPassword": password, "confirmPassword": password}
        reset_password = requests.post(url=f"{update_password_url}", headers=headers, params=data, verify=False)
        return reset_password.text

    def password_reset_sequence(self, client_name, admin_user, adminp_assword, nhusername, nhpassword, url, queryurl,
                                updateUserurl, getpasswordurl):

        token = self.gktoken(client_name, admin_user, adminp_assword, url)

        sso_id = self.getssoId(client_name, token, nhusername, queryurl)

        response = self.updateUserProfile(token, sso_id, updateUserurl)
        print(response)
        nh_token = self.getpasswordtoken(token, client_name, nhusername, getpasswordurl)

        nh_token1 = self.getpasswordtoken(token, client_name, nhusername, getpasswordurl)

        response_nh = self.resetPassword(nh_token, client_name, nhusername, nhpassword, getpasswordurl)

        saveqns_text = self.getChallengeQnsSaveanswers(nh_token1, client_name, getpasswordurl)

        nh_newtoken = self.gktoken(client_name, nhusername, nhpassword, url)
