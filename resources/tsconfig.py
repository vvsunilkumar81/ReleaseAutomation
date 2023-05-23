import inspect,os

#FileSystem Objects
b_o_filename = "success_payload.xml"
b_o_filename_iqa= "iqaTestclient_payload.xml"
b_o_filename_iqa_output="iqaTestclient_output_payload.xml"
b_o_filename_output="success_output_payload.xml"
chromedriver="chromedriver.exe"
geckodriver="geckodriver.exe"
logfilename="logfile.log"
configfile="config.cfg"
testdata_dummy="testdata_dummy.csv"
testdata="testdata.csv"
ipfilename="config.ini"
project_root = os.path.dirname(os.path.dirname(__file__))
logfilepath = os.path.join(project_root, 'logs\\')+logfilename
b_o_filepath = os.path.join(project_root, 'resources\\')+b_o_filename

b_o_filepath_output = os.path.join(project_root, 'resources\\')+b_o_filename_output
b_o_filepath_iqa_output = os.path.join(project_root, 'resources\\')+b_o_filename_iqa_output

chromedriver_path= os.path.join(project_root, 'resources\\')+chromedriver
ffdriver_path= os.path.join(project_root, 'resources\\')+geckodriver
configfilepath=os.path.join(project_root, 'resources\\')+configfile
testdata_dummy_filepath=os.path.join(project_root, 'resources\\')+testdata_dummy
testdata_filepath=os.path.join(project_root, 'resources\\')+testdata
ipfilepath=os.path.join(project_root)+"\\"+ipfilename
#Rest services URIs
b2O_resource_path = "/kr-KenexaRecruiter/Integration2XBService"
gktoken_resource_path= "/api/oauth/token"
query_resource_path = "/api/User/q"
updateUser_resource_path = "/api/User/"
getPassword_resource_path = "/api/"
#Page titles
homepagetitle="Onboard home | Onboard Manager | Infinite BrassRing Platform"
#Workflows & Task Names
notemplate_task_name="Automation_NoTemplate"
ob_end_task_name="Onboard End"

def whoami():
    return inspect.stack()[1][3]

