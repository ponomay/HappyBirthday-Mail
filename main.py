##################### Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

my_email = "arthur.*******@gmail.com"
password = "******"


# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        text = open_random_file()
        connect.sendmail(from_addr=my_email, to_addrs=new_dict[current_day][1],
                         msg=f"Subject: Happy birthday \n{text}")


def open_random_file():
    digit = random.randint(1, 3)
    with open(f"./letter_templates/letter_{digit}.txt") as template:
        a = template.read()
        print(a)
        b = a.replace("[NAME]", new_dict[current_day][0])
        return b


# 1 open CSV file
df = pandas.read_csv("birthdays.csv")
# print(df)
# print(df.iterrows())
# print(df["month"])
# print(type(df["month"]))
new_dict = {}
# create dict
# new_tuple = ()
# super_dict = {row[1]: row[0] for row in df.iterrows()}
for index, row in df.iterrows():
    new_tuple = (row["month"], row["day"])
    new_dict[new_tuple] = [row["name"], row["email"]]
print(new_dict)
day = dt.datetime.today()
current_day = (day.month, day.day)
print(current_day)
if current_day in new_dict:
    print("sending email")
    send_email()

