import smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def otp_on_email(email_id):
    fromaddr = "atharvp45@gmail.com"
    senders_pass = "78694eddy45"
    toaddr = email_id

    msg = MIMEMultipart()
    msg["from"] = fromaddr
    msg["to"] = toaddr
    msg["Subject"] = "OTP by ZeeBank"

    otp = random.randrange(100001,999999)
    body = "Your OTP is [{}]".format[otp]

    msg.attach(MIMEText(body,"plain"))
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.startls()
    s.login(fromaddr, senders_pass)
    text = msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()
    c_txt = "OTP sent to ({}******{})".format(toaddr[0:2],toaddr[6:])
    print(c_txt)
    return otp

user_email = input("Enter your email : ")
generated_otp = otp_on_email(user_email)

user_entered_otp = int(input("Enter OTP : "))
if generated_otp == user_entered_otp:
    print("OTP matched")
else:
    print("You entered wrong OTP")