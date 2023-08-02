import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from datetime import datetime, date

date_format = "%Y-%m-%d"
month_list = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
jdata = ''

def getmonthindex(mnth):
    try:
        return month_list.index(mnth)+1
    except:
        return -1

def compare_today(birthday_obj):
    if(birthday_obj!=None):
        return birthday_obj.date() == date.today()
    else:
        return False

def sendmail(emp):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("satyajitbbsingh@gmail.com", "mdmwpjaontxtssor")
    message = "Message_you_need_to_send"
    s.sendmail("satyajitbbsingh@gmail.com", "satyajitbbsingh@gmail.com", message)
    s.quit()
    # print('mailing birthday report')
    # fromaddr = 'satyajit_baliarsingh@apple.com'
    # toaddr = 'satyajit_baliarsingh@apple.com'
    # msg = MIMEMultipart()
    # msg['From'] = toaddr
    # msg['To'] = toaddr
    # msg['Subject'] = "!! Apple BHDC Birthday Reminder !!"
    #
    # body = """
    #             Hi,
    #
    #             Today is the birthday of Mr/Mrs """+emp.name+"""
    #
    #             Thanks,
    #             Satyajit
    #         """
    #
    # msg.attach(MIMEText(body, 'alternative'))
    # toaddr = [toaddr]
    # # with smtplib.SMTP('relay.apple.com',timeout=(400)) as server:
    # with smtplib.SMTP('relay.apple.com', timeout=(400)) as server:
    #     server.ehlo()
    #     server.starttls()
    #     server.ehlo()
    #     text = msg.as_string()
    #     server.sendmail(fromaddr, toaddr, text)
    #     server.quit()

class Employee():
    "this hold all the apple bhdc emplyee details required for birthday celbration"
    def __init__(self, EmpObj):
        global date_format
        self.id = EmpObj['ID']
        self.name = EmpObj['Name']
        self.phone_number = EmpObj['Phone Number']
        self.birth_date = EmpObj['Birth Date']
        self.birth_month = EmpObj['Birth Month'].upper()
        self.birth_date_obj = None

    def set_birth_dat(self):
        global date_format
        if(getmonthindex(self.birth_month) != -1):
            date_string = f"{datetime.now().year}-{getmonthindex(self.birth_month)}-{self.birth_date}"
            self.birth_date_obj = datetime.strptime(date_string, date_format)


if __name__ == '__main__':
    # read json file

    file_path = 'birthdaylist.json'
    with open(file_path, 'r') as file:
        # json_data = json.loads(file)
        jdata = json.load(file)
        for item in jdata:
            emp = Employee(item)
            emp.set_birth_dat()
            if(compare_today(emp.birth_date_obj)):
                print(f"today is the birthday of {emp.name} as of {emp.birth_date_obj.date()}")
                sendmail(emp)