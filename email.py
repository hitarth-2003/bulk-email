import smtplib
import csv
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ================= CONFIG =================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"
DELAY = 2  # seconds between emails

CSV_FILE = "contacts.csv"
TEMPLATE_FILE = "template.txt"

# ==========================================

# Read template file
def load_template():
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as file:
        return file.read()

# Replace placeholders with actual data
def personalize(template, data):
    for key, value in data.items():
        template = template.replace(f"{{{{{key}}}}}", value)
    return template

# Send email function
def send_email(receiver_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        print(f"[SUCCESS] Email sent to {receiver_email}")

    except Exception as e:
        print(f"[FAILED] {receiver_email} -> {e}")

# Main logic
def main():
    template = load_template()

    with open(CSV_FILE, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            email_body = personalize(template, row)
            subject = f"Hello {row['name']}!"

            send_email(row["email"], subject, email_body)

            time.sleep(DELAY)  # prevent spam blocking

if __name__ == "__main__":
    main()


    # dscdscdc
    # dsfdcdf