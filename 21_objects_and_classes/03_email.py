class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


indexes = []
emails = []
command = input()
while command != "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()
indexes = [int(x) for x in input().split(", ")]

for index in indexes:
    if 0 <= index < len(emails):
        emails[index].sent()
for email in emails:
    print(email.get_info())