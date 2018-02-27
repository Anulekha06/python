#email
import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("anulekha2112016@gmail.com","********")
msg="hi, how are you? "
s.sendmail("anulekha2112016@gmail.com","yashaswithakur1234@gmail.com",msg)
print("success")
s.quit()
