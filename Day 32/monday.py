import datetime as dt
import smtplib
import random

my_email =
password =

now = dt.datetime.now()
day = now.weekday()

if (day == 4):
    with open("quotes.txt") as file:
        data = [line.rstrip() for line in file]
        quote = random.choice(data)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(from_addr = my_email,
                                to_addrs = ,
                                msg = "Subject:You got this!\n\n" +
                                        quote
            )
