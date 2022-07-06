import os
import yagmail
import datetime
import time


def automail(rmail):
    receiver = rmail
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    body = "Attendence File"
    filename = "Attendance"+os.sep+"Attendance_"+date+".csv"

    yag = yagmail.SMTP("report.auttendo@gmail.com", "wzywwejszzxuizvh")

    yag.send(
        to=receiver,
        subject="Attendance Report",
        contents=body,
        attachments=filename
    )
