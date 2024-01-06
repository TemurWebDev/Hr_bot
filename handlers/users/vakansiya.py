from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from reportlab.lib.utils import ImageReader
from aiogram.types import ContentType

from data.config import ADMINS
from loader import dp, db, bot

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboards.default.vakansiyaKey import citykey,filialkey,positionkey,studentkey,salarykey,phonkey,yuborishkey
from keyboards.default.userkey import boshmenuUz,bekorUz

from handlers.users.hr import create_image_with_greeting

# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class Vakansiya(StatesGroup):
    city = State()
    filial = State()
    position = State()
    phon = State()
    name = State()
    date = State()
    addres = State()
    student = State()
    img = State()
    salary = State()
    yuborish = State()





@dp.message_handler(text="🖋 Vakansiya")
async def startState(message: types.Message):
    user = db.select_user(chat_id=message.from_user.id)
    if user[4] == "uz":
        await message.answer("Shaharni tanlang!",reply_markup=citykey)
        await Vakansiya.city.set()
    else:
        await message.answer(message.text)


@dp.message_handler(state=Vakansiya.city)
async def answer_city(message: types.Message, state: FSMContext):
    city = message.text

    await state.update_data(
        {"city": city}
    )

    await message.answer("Filialni tanlang!",reply_markup=filialkey)

    # await PersonalData.email.set()
    await Vakansiya.next()


@dp.message_handler(state=Vakansiya.filial)
async def answer_city(message: types.Message, state: FSMContext):
    filial = message.text

    await state.update_data(
        {"filial": filial}
    )

    await message.answer("Sizni qiziqtirgan lavozimni tanlang",reply_markup=positionkey)

    # await PersonalData.email.set()
    await Vakansiya.next()


@dp.message_handler(state=Vakansiya.position)
async def answer_city(message: types.Message, state: FSMContext):
    position = message.text

    await state.update_data(
        {"position": position}
    )

    await message.answer("Telefon nomer yuboring!",reply_markup=phonkey)

    # await PersonalData.email.set()
    await Vakansiya.next()



@dp.message_handler(state=Vakansiya.phon,content_types=types.ContentTypes.CONTACT)
async def answer_city(message: types.Message, state: FSMContext):
    phon = message.contact.phone_number

    await state.update_data(
        {"phon": phon}
    )

    await message.answer("To'liq FISh \nnamuna: Temurbek Qurbonov Sodiq o'g'li",reply_markup=bekorUz)

    # await PersonalData.email.set()
    await Vakansiya.next()



@dp.message_handler(state=Vakansiya.name)
async def answer_city(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )

    await message.answer("Tug'ilgan sana! \nnamuna: 07.07.1999")

    # await PersonalData.email.set()
    await Vakansiya.next()


@dp.message_handler(state=Vakansiya.date)
async def answer_city(message: types.Message, state: FSMContext):
    date = message.text

    await state.update_data(
        {"date": date}
    )

    await message.answer("Yashash manzilingizni kiriting! \nnamuna:Olmazor tumani")

    # await PersonalData.email.set()
    await Vakansiya.next()


@dp.message_handler(state=Vakansiya.addres)
async def answer_city(message: types.Message, state: FSMContext):
    addres = message.text

    await state.update_data(
        {"addres": addres}
    )

    await message.answer("Siz studentmisz!",reply_markup=studentkey)

    # await PersonalData.email.set()
    await Vakansiya.next()


@dp.message_handler(state=Vakansiya.student)
async def answer_city(message: types.Message, state: FSMContext):
    student = message.text

    await state.update_data(
        {"student": student}
    )

    await message.answer("Rasm yuboring",reply_markup=bekorUz)

    # await PersonalData.email.set()
    await Vakansiya.next()




@dp.message_handler(content_types=ContentType.ANY,state=Vakansiya.img)
async def answer_img(message: types.Message, state: FSMContext):
    if message.content_type == ContentType.PHOTO:
        photo = message.photo[-1]
        file_id = photo.file_id
        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path

    # Rasmni faylga yuklash
        await bot.download_file(file_path, f"handlers/users/file/imgs/{message.from_user.id}.jpg")
        #await message.photo[-1].download()
        await message.answer("Siz kutyotgan maosh",reply_markup=salarykey)
        await Vakansiya.next()
    else:
        await message.answer("Rasm yuboring!!")




@dp.message_handler(state=Vakansiya.salary)
async def answer_city(message: types.Message, state: FSMContext):
    maosh = message.text

    await state.update_data(
        {"maosh": maosh}
    )

    data = await state.get_data()
    city = data.get("city")
    filial = data.get("filial")
    position = data.get("position")
    phon = data.get("phon")
    name = data.get("name")
    date = data.get("date")
    addres = data.get("addres")
    student = data.get("student")
    salary = data.get("maosh")


    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Shahar - {city}\n"
    msg += f"Filial - {filial}\n"
    msg += f"Position: - {position}\n"
    msg += f"Phon: - {phon}\n"
    msg += f"Name: - {name}\n"
    msg += f"Date: - {date}\n"
    msg += f"Addres: - {addres}\n"
    msg += f"Student: - {student}\n"
    msg += f"Salary: - {salary}\n\n"
    msg += f"Ma'lumotlaringiz to'g'rimi!"

    await message.answer(msg,reply_markup=yuborishkey)


    malumotlar = [city,filial,position,phon,name,date,addres,student,salary]


    #await bot.send_message(chat_id=1363350178,text=malumotlar)

    img = f"C:/Users/User/Desktop/Hr_bot/handlers/users/file/imgs/{message.from_user.id}.jpg"
    file = f"C:/Users/User/Desktop/Hr_bot/handlers/users/file/files/{message.from_user.id}.pdf"
    
    
    create_image_with_greeting(file,img,malumotlar)

    await Vakansiya.next()



@dp.message_handler(state=Vakansiya.yuborish)
async def yuborish(message: types.Message,state: FSMContext):
    if message.text == "Yuborish":
        await message.answer("Yuborildi!!!",reply_markup=boshmenuUz)
        await state.finish()
        files = f"C:/Users/User/Desktop/Hr_bot/handlers/users/file/files/{message.from_user.id}.pdf"
        with open(files, "rb") as file:
        # Document jo'natish
            await bot.send_document(chat_id=message.from_user.id, document=file)
    elif message.text == "Rad etish":
        await message.answer("Rad etildi",reply_markup=boshmenuUz)
        await state.finish()
        await message.answer("Malumotlar yuborilmadi!")

    


