from aiogram import types
from aiogram.dispatcher.filters import CommandStart


from loader import dp
from keyboards.reply.cities import cities
import requests
from datetime import datetime


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=cities)

@dp.message_handler(text="Toshkent")
async def url_handler(message: types.Message):
    url = "https://islomapi.uz/api/present/day?region=Toshkent"
    response = requests.get(url)
    data = response.json()

    region = data["region"]
    date = data["date"]
    hijri_month = data["hijri_date"]["month"]
    bomdod = data["times"]["tong_saharlik"]
    sunrise = data["times"]["quyosh"]
    hijri_day = data["hijri_date"]["day"]
    peshin = data["times"]["peshin"]
    asr = data["times"]["asr"]
    shom = data["times"]["shom_iftor"]
    hozirgi_vaqt = datetime.now()
    kun = data["weekday"]
    time = hozirgi_vaqt.strftime('%H:%M')
    xufton = data['times']["hufton"]

    text = "Namoz Vaqtlari:\n"
    text += "=========================\n"
    text += "📌 《 🏙 Toshkent 》 vaqti bilan\n"
    text += "--------------------------------------------\n"
    text += f"🌍  Hijri oy: - {hijri_month}\n"
    text += f"📅  {hijri_month} oyining {hijri_day} - kuni\n\n"
    text += f"🌓  Tong - saharlik:  - {bomdod}\n"
    text += f"🌞  Quyosh chiqishi: - {sunrise}\n\n"
    text += f"🕰  Bomdod:    -    {bomdod}\n"
    text += f"🕰  Peshin:      -    {peshin}\n"
    text += f"🕰  Asr:            -    {asr}\n"
    text += f"🕰  Shom:          -    {shom}\n"
    text += f"🕰  Xufton:    -    {xufton}\n\n"
    text += f"📅 {date[0:4]} - yil | Oyning {date[5:7]} - kuni | {kun} | Vaqt - {time}"



    await message.answer(text)
    
@dp.message_handler(text="Samarqand")
async def url_handler(message: types.Message):
    url = "https://islomapi.uz/api/present/day?region=Samarqand"
    response = requests.get(url)
    data = response.json()

    region = data["region"]
    date = data["date"]
    hijri_month = data["hijri_date"]["month"]
    bomdod = data["times"]["tong_saharlik"]
    sunrise = data["times"]["quyosh"]
    hijri_day = data["hijri_date"]["day"]
    peshin = data["times"]["peshin"]
    asr = data["times"]["asr"]
    shom = data["times"]["shom_iftor"]
    hozirgi_vaqt = datetime.now()
    kun = data["weekday"]
    time = hozirgi_vaqt.strftime('%H:%M')
    xufton = data['times']["hufton"]

    text = "Namoz Vaqtlari:\n"
    text += "=========================\n"
    text += "📌 《 🏙 Samarqand 》 vaqti bilan\n"
    text += "--------------------------------------------\n"
    text += f"🌍  Hijri oy: - {hijri_month}\n"
    text += f"📅  {hijri_month} oyining {hijri_day} - kuni\n\n"
    text += f"🌓  Tong - saharlik:  - {bomdod}\n"
    text += f"🌞  Quyosh chiqishi: - {sunrise}\n\n"
    text += f"🕰  Bomdod:    -    {bomdod}\n"
    text += f"🕰  Peshin:      -    {peshin}\n"
    text += f"🕰  Asr:            -    {asr}\n"
    text += f"🕰  Shom:          -    {shom}\n"
    text += f"🕰  Xufton:    -    {xufton}\n\n"
    text += f"📅 {date[0:4]} - yil | Oyning {date[5:7]} - kuni | {kun} | Vaqt - {time}"



    await message.answer(text)   




@dp.message_handler(text="Namangan")
async def url_handler(message: types.Message):
    url = "https://islomapi.uz/api/present/day?region=Namangan"
    response = requests.get(url)
    data = response.json()

    region = data["region"]
    date = data["date"]
    hijri_month = data["hijri_date"]["month"]
    bomdod = data["times"]["tong_saharlik"]
    sunrise = data["times"]["quyosh"]
    hijri_day = data["hijri_date"]["day"]
    peshin = data["times"]["peshin"]
    asr = data["times"]["asr"]
    shom = data["times"]["shom_iftor"]
    hozirgi_vaqt = datetime.now()
    kun = data["weekday"]
    time = hozirgi_vaqt.strftime('%H:%M')
    xufton = data['times']["hufton"]

    text = "Namoz Vaqtlari:\n"
    text += "=========================\n"
    text += "📌 《 🏙 Namangan 》 vaqti bilan\n"
    text += "--------------------------------------------\n"
    text += f"🌍  Hijri oy: - {hijri_month}\n"
    text += f"📅  {hijri_month} oyining {hijri_day} - kuni\n\n"
    text += f"🌓  Tong - saharlik:  - {bomdod}\n"
    text += f"🌞  Quyosh chiqishi: - {sunrise}\n\n"
    text += f"🕰  Bomdod:    -    {bomdod}\n"
    text += f"🕰  Peshin:      -    {peshin}\n"
    text += f"🕰  Asr:            -    {asr}\n"
    text += f"🕰  Shom:          -    {shom}\n"
    text += f"🕰  Xufton:    -    {xufton}\n\n"
    text += f"📅 {date[0:4]} - yil | Oyning {date[5:7]} - kuni | {kun} | Vaqt - {time}"



    await message.answer(text)       





@dp.message_handler(text="Jizzax")
async def url_handler(message: types.Message):
    url = "https://islomapi.uz/api/present/day?region=Namangan"
    response = requests.get(url)
    data = response.json()

    region = data["region"]
    date = data["date"]
    hijri_month = data["hijri_date"]["month"]
    bomdod = data["times"]["tong_saharlik"]
    sunrise = data["times"]["quyosh"]
    hijri_day = data["hijri_date"]["day"]
    peshin = data["times"]["peshin"]
    asr = data["times"]["asr"]
    shom = data["times"]["shom_iftor"]
    hozirgi_vaqt = datetime.now()
    kun = data["weekday"]
    time = hozirgi_vaqt.strftime('%H:%M')
    xufton = data['times']["hufton"]
    text = "Namoz Vaqtlari:\n"
    text += "=========================\n"
    text += "📌 《 🏙 Jizzax 》 vaqti bilan\n"
    text += "--------------------------------------------\n"
    text += f"🌍  Hijri oy: - {hijri_month}\n"
    text += f"📅  {hijri_month} oyining {hijri_day} - kuni\n\n"
    text += f"🌓  Tong - saharlik:  - {bomdod}\n"
    text += f"🌞  Quyosh chiqishi: - {sunrise}\n\n"
    text += f"🕰  Bomdod:    -    {bomdod}\n"
    text += f"🕰  Peshin:      -    {peshin}\n"
    text += f"🕰  Asr:            -    {asr}\n"
    text += f"🕰  Shom:          -    {shom}\n"
    text += f"🕰  Xufton:    -    {xufton}\n\n"
    text += f"📅 {date[0:4]} - yil | Oyning {date[5:7]} - kuni | {kun} | Vaqt - {time}"



    await message.answer(text)   
    
@dp.message_handler(text="Buxoro")
async def url_handler(message: types.Message):
    url = "https://islomapi.uz/api/present/day?region=Buxoro"
    response = requests.get(url)
    data = response.json()

    region = data["region"]
    date = data["date"]
    hijri_month = data["hijri_date"]["month"]
    bomdod = data["times"]["tong_saharlik"]
    sunrise = data["times"]["quyosh"]
    hijri_day = data["hijri_date"]["day"]
    peshin = data["times"]["peshin"]
    asr = data["times"]["asr"]
    shom = data["times"]["shom_iftor"]
    hozirgi_vaqt = datetime.now()
    kun = data["weekday"]
    time = hozirgi_vaqt.strftime('%H:%M')
    xufton = data['times']["hufton"]
    text = "Namoz Vaqtlari:\n"
    text += "=========================\n"
    text += "📌 《 🏙 Buxoro 》 vaqti bilan\n"
    text += "--------------------------------------------\n"
    text += f"🌍  Hijri oy: - {hijri_month}\n"
    text += f"📅  {hijri_month} oyining {hijri_day} - kuni\n\n"
    text += f"🌓  Tong - saharlik:  - {bomdod}\n"
    text += f"🌞  Quyosh chiqishi: - {sunrise}\n\n"
    text += f"🕰  Bomdod:    -    {bomdod}\n"
    text += f"🕰  Peshin:      -    {peshin}\n"
    text += f"🕰  Asr:            -    {asr}\n"
    text += f"🕰  Shom:          -    {shom}\n"
    text += f"🕰  Xufton:    -    {xufton}\n\n"
    text += f"📅 {date[0:4]} - yil | Oyning {date[5:7]} - kuni | {kun} | Vaqt - {time}"



    await message.answer(text)           

@dp.message_handler(text="Andijan")
async def url_handler(message: types.Message):
    url = "https://islomapi.uz/api/present/day?region=Andijon"
    response = requests.get(url)
    data = response.json()

    region = data["region"]
    date = data["date"]
    hijri_month = data["hijri_date"]["month"]
    bomdod = data["times"]["tong_saharlik"]
    sunrise = data["times"]["quyosh"]
    hijri_day = data["hijri_date"]["day"]
    peshin = data["times"]["peshin"]
    asr = data["times"]["asr"]
    shom = data["times"]["shom_iftor"]
    hozirgi_vaqt = datetime.now()
    kun = data["weekday"]
    time = hozirgi_vaqt.strftime('%H:%M')
    xufton = data['times']["hufton"]
    text = "Namoz Vaqtlari:\n"
    text += "=========================\n"
    text += "📌 《 🏙 Andijan 》 vaqti bilan\n"
    text += "--------------------------------------------\n"
    text += f"🌍  Hijri oy: - {hijri_month}\n"
    text += f"📅  {hijri_month} oyining {hijri_day} - kuni\n\n"
    text += f"🌓  Tong - saharlik:  - {bomdod}\n"
    text += f"🌞  Quyosh chiqishi: - {sunrise}\n\n"
    text += f"🕰  Bomdod:    -    {bomdod}\n"
    text += f"🕰  Peshin:      -    {peshin}\n"
    text += f"🕰  Asr:            -    {asr}\n"
    text += f"🕰  Shom:          -    {shom}\n"
    text += f"🕰  Xufton:    -    {xufton}\n\n"
    text += f"📅 {date[0:4]} - yil | Oyning {date[5:7]} - kuni | {kun} | Vaqt - {time}"



    await message.answer(text) 