import yagmail

yag = yagmail.SMTP("sadjr2833@wrdsb.ca", "Valley==River+4")


contents = [
    "Hello world",
    "newline, yayay",
    "What's up"
]

recipients = ["spams4894@gmail.com", "rashed.sadjad@gmail.com"]

print("Please type in a list of emails to send:")

while True:
  userInput = input("")
  if userInput == "send":
    break
  recipients.append(userInput)

print("sending...")

yag.send(subject="Test", contents=contents)

print("Email successfully sent!")