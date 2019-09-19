import requests
import json

def main():
    destination = input("Destination: ")
    subject = input("Assunto: ")
    message = input("Mensagem: ")

    print(send_email(destination, subject, message).text)

def send_email(destination, subject, message):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox643ecff7351d4ddd9bce0a8ed2482a06.mailgun.org/messages",
        auth=("api", "7d1e827b02e27fb9de45a18af53145ee-bbbc8336-d3501f8a"),
        data={
             "from": "Mailgun Sandbox <postmaster@sandbox643ecff7351d4ddd9bce0a8ed2482a06.mailgun.org>",
             "to": destination,
             "subject": subject,
             "text": message
         }
    )


if __name__ == "__main__":
    main()