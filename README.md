# EmailScriping
---------------
### flow
1. AWS EventBridge를 통해서 cron을 작성하여 정해진 날짜에 이메일 확인

2. 이메일 확인 후 해당 이메일에서 텍스트와 이미지를 분리

선택사항
----------------
a. 이미지 자체를 curl로 전송

b. 사용한 앱(Swit)은 curl로 text형태의 데이터만 전송이 가능하여 s3에 업로드한 후 lambda 트리거를 통해 curl로 링크 전송
