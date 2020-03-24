import requests

# reference: https://notify-bot.line.me/doc/en/
# reference: https://jkjung-avt.github.io/line-notify/
def Notify(token, msg="Hello", stickerPackageId=None, stickerId=None, img=None):
    headers = {'Authorization': 'Bearer ' + token}
    if stickerPackageId and stickerId:
        payload = {'message':msg, 'stickerPackageId':stickerPackageId, 'stickerId':stickerId}
    else:
        payload = {'message': msg}
    files = {'imageFile': open(img, 'rb')} if img else None
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload, files=files)
    if files:
        files['imageFile'].close()
    return r.status_code


if __name__=="__main__":
    # 欲傳送的訊息內容
    message = '測試一下！'
    # 您的權杖內容
    token = ''

    Notify(token, message)