import smtplib
import datetime as dt
import pandas
import random

now = dt.datetime.now()
month = now.month
day = now.day

my_email =
password =

df = pandas.read_csv("birthdays.csv")
df = df[(df.month == month) & (df.day == day)].values.tolist()

for data in df:
    letter = "letter_templates/letter_" + str(random.randint(1,3)) + ".txt"
    with open(letter, "r") as file:
        msg = file.read()
        msg = msg.replace("[NAME]", data[0])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(from_addr = my_email,
        to_addrs = data[1],
        msg = msg
        )
