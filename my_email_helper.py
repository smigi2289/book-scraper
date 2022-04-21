import smtplib;

def send_email(from_email,from_password,to_address,message,subject=""):
    
    email_message=f"Subject:{subject}\n\n{message}"
    
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=from_email,password=from_password)
    connection.sendmail(from_addr=from_email,to_addrs=to_address,msg=email_message)
    connection.close()

def send_email_from_me(to_address,message,subject=""):
    my_email = "roymailingemail2289@gmail.com"
    my_password = "MailingEmail16842"
    send_email(my_email,my_password,to_address,message,subject)
    
