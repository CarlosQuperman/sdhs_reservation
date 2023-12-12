from base64 import b64encode
import requests

def send_sms(receivers, message,user_id='', secure='', sender=''):
    params = {
        'user_id': user_id,
        'secure': secure,
        'mode': '1',
        'sphone1': sender[:3],   # 해당 발신번호를 확인하여 변수 변경이 필요함.
        'sphone2': sender[3:7], # 해당 발신번호를 확인하여 변수 변경이 필요함. 
        'sphone3': sender[7:11], # 해당 발신번호를 확인하여 변수 변경이 필요함.
        'rphone': ','.join(receivers),
        'msg': message,
    }


    response = requests.post('https://sslsms.cafe24.com/sms_sender.php',data=params)
    return response.text



