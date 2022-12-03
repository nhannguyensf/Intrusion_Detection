import telegram

def send_telegram(photo_path="alert.png"):
    try:
        my_token = "5811414502:AAGx1n_NTi8ev93uD9cZLXLiRZYsvGJRB5s"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="1871882149", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")