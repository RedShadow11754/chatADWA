import smtplib

class EmailHandler:
    def __init__(self,feed):
        self.status = "Failed"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("abelalex530@gmail.com", "ccnq ryrs pesy jpzj")
            connection.sendmail(from_addr="abelalex530@gmail.com", to_addrs="abelalex122129@gmail.com",
                                msg=f"Subject:start your Monday\n\n{feed}")
            connection.close()
            self.status = "Success"

    def status_email(self):
        return {"status":self.status}