import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# ===== 設定 =====
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_ADDRESS = "nyakkimyaomyao@gmail.com"
EMAIL_PASSWORD = "xcnq jadv wvzg uykv"  # アプリパスワード

TO_EMAIL = "ichiro-shimada@hiroshima-u.ac.jp"

# ===== 日報内容 =====
today = datetime.now().strftime("%Y-%m-%d")
with open("report.txt", "r", encoding="utf-8") as f:
    body = f.read()
    
msg = MIMEText(body)
msg["Subject"] = f"業務記録 {today}"
msg["From"] = EMAIL_ADDRESS
msg["To"] = TO_EMAIL

# ===== 送信 =====
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(msg)

print("送信完了")
