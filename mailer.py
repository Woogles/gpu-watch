import win32com.client

from config import EMAIL_TO


def send_report(html):

    outlook = (
        win32com.client.Dispatch(
            "Outlook.Application"
        )
    )

    mail = (
        outlook.CreateItem(0)
    )

    mail.Subject = (
        "GPU Watch Results"
    )

    mail.To = EMAIL_TO

    mail.HTMLBody = html

    mail.Send()