import requests

with open('/home/dilshod/PycharmProjects/Python_21/module_5/lesson_2/tmp/img.png', 'rb') as f:
    response = requests.post('https://telegra.ph/upload', files={'file': f})
    print(response.status_code)
    data = response.json()
    url = "https://telegra.ph" + data[0].get('src').replace(r"\\", '')
    print(url)


# import segno
# qrcode = segno.make_qr("https://kun.uz")
# qrcode.save("kun_uz_qr.png")