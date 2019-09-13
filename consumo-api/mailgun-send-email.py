import requests
import json

def main():
    destination = input("Destination: ")
    subject = input("Assunto: ")
    message = input("Mensagem: ")

    print(send_email(destination, subject, message))

def send_email(destination, subject, message):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox6cdb7da5789f489395ea59059142d42f.mailgun.org/messages",
        auth=("api", "d80e64f3c1ea6e909127e1ff36e5df0e-c27bf672-3b430069"),
        data={
            "from": "Mailgun Sandbox <postmaster@sandbox6cdb7da5789f489395ea59059142d42f.mailgun.org>",
            "to": destination,
            "subject": subject,
            "text": message
        }
    )


if __name__ == "__main__":
    main()