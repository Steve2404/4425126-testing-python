import requests


class Employee:

    taux = 1.4

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.taux)

    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last}/{self.month}")
        return response.text if response.ok else response.status_code
