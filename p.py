# create smtp session 
s = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 is a port number
# start TLS for E-mail security 
s.starttls()
# Log in to your gmail account
s.login("sender_email" , "sender_email_password")
otp = random.randint(1000, 9999)
otp = str(otp)
        
s.sendmail("sender_email" , receiver_email , otp)
print("OTP sent succesfully..")
# close smtp session
s.quit()