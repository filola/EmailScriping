import imaplib
import email
import requests
import json
import subprocess
from io import BytesIO

# Save Image function
# def save_image(data, name):
#     """Save the image data as a file and return the URL"""
#     file_path = os.path.join(os.getcwd(), name)
#     with open(file_path, 'wb') as f:
#         f.write(data)
    # return file_path

# Swit webhook URL
webhook_url = "https://hook.swit.io/chat/{chat_id}/{webhook_id}"

# Connect to the Gmail account
imap = imaplib.IMAP4_SSL('imap.gmail.com')
email_address = 'email 주소'
app_password = 'email 2차 인증키'

# Log in to the Gmail account
imap.login(email_address, app_password)

# Select the inbox
imap.select("INBOX")

# 사서함의 모든 메일의 uid 정보 가져오기
# 만약 특정 발신 메일만 선택하고 싶다면 'ALL' 대신에 '(FROM "xxxxx@naver.com")' 입력
status, messages = imap.uid('search', None, '(FROM "gahyun@amazon.com")')

messages = messages[0].split()

# 0이 가장 마지막 메일, -1이 가장 최신 메일 (ex. [b'2832', b'2853', b'2908'])
recent_email = messages[-1]

# fetch Email
res, msg = imap.uid('fetch', recent_email, "(RFC822)")

# Encoding message
raw = msg[0][1]

# Decoding message
raw_readable = msg[0][1].decode('utf-8')

raw_email = msg[0][1]
email_message_instance = email.message_from_string(raw_readable)
whole_body = ''
image_urls = []

for part in email_message_instance.walk():
    if part.get_content_type() == "text/plain": # ignore attachments/html
        body = part.get_payload(decode=True)
        # print("body: " + body)
        whole_body += body.decode('utf-8') + ' '
    if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
        print("image content")
        # image_name = part.get_filename()
        image_data = part.get_payload(decode=True)
        print(type(image_data))
        
        # image_url = save_image(image_data)
        # image_urls.append(image_url)
        break
    else:
        continue

imap.close()
imap.logout()

# data = {"url": "https://getfile.fmkorea.com/getfile.php?code=3f06151e3c2e756d09dbab894493a688&file=https%3A%2F%2Fgifsf.com%2Ffiles%2Fattach%2Fimages%2F136387%2F740%2F013%2F005%2F8d2a7c5c0b9801405158fae1354ff22a.jpg&"}

# # json.dumps() 함수를 사용하여 데이터를 JSON 문자열로 변환합니다.
# data_str = json.dumps(data)

# # subprocess 모듈의 run() 함수를 사용하여 curl 명령어를 실행합니다.
# result = subprocess.run(["curl", "-X", "POST", "-H", "Content-Type: application/json", "-d", data_str, url], capture_output=True)

# # 결과 출력
# print(result.stdout.decode())

with open('/Users/qu_chs/work/plating/', "rb") as f:
    response = requests.post(
        webhook_url.format(chat_id='chat_id', webhook_id='webhook_id'),
        files={"file": f},
)

print(response.status_code)