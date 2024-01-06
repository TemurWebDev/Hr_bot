from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import ContentType

from data.config import ADMINS
from loader import dp, db, bot

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboards.default.vakansiyaKeyRu import citykeyRu,filialkeyRu,positionkeyRu,studentkeyRu,salarykeyRu,phonkeyRu,yuborishkeyRu
from keyboards.default.userkey import boshmenuUs,bekorRu

from handlers.users.hrRu import create_hr_Ru

# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class VakansiyaRu(StatesGroup):
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





@dp.message_handler(text="🖋 Вакансия")
async def startState(message: types.Message):
    user = db.select_user(chat_id=message.from_user.id)
    print(user)
    if user[4]  == "ru":
        await message.answer("Выберите город!",reply_markup=citykeyRu)
        await VakansiyaRu.city.set()
    else:
        await message.answer(message.text)


@dp.message_handler(state=VakansiyaRu.city)
async def answer_city(message: types.Message, state: FSMContext):
    city = message.text

    await state.update_data(
        {"city": city}
    )

    await message.answer("Выбирайте ветку!",reply_markup=filialkeyRu)

    # await PersonalData.email.set()
    await VakansiyaRu.next()


@dp.message_handler(state=VakansiyaRu.filial)
async def answer_city(message: types.Message, state: FSMContext):
    filial = message.text

    await state.update_data(
        {"filial": filial}
    )

    await message.answer("Выберите позицию, которая вас интересует!",reply_markup=positionkeyRu)

    # await PersonalData.email.set()
    await VakansiyaRu.next()


@dp.message_handler(state=VakansiyaRu.position)
async def answer_city(message: types.Message, state: FSMContext):
    position = message.text

    await state.update_data(
        {"position": position}
    )

    await message.answer("Отправьте номер телефона!",reply_markup=phonkeyRu)

    # await PersonalData.email.set()
    await VakansiyaRu.next()



@dp.message_handler(state=VakansiyaRu.phon,content_types=types.ContentTypes.CONTACT)
async def answer_city(message: types.Message, state: FSMContext):
    phon = message.contact.phone_number

    await state.update_data(
        {"phon": phon}
    )

    await message.answer("Напишите свое имя и фамилию \n например: Темур Курбанов.",reply_markup=bekorRu)

    # await PersonalData.email.set()
    await VakansiyaRu.next()



@dp.message_handler(state=VakansiyaRu.name)
async def answer_city(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )

    await message.answer("Дата рождения! Пример: 07.07.1999")

    # await PersonalData.email.set()
    await VakansiyaRu.next()


@dp.message_handler(state=VakansiyaRu.date)
async def answer_city(message: types.Message, state: FSMContext):
    date = message.text

    await state.update_data(
        {"date": date}
    )

    await message.answer("Введите адрес проживания! Пример: Алмазарский район")

    # await PersonalData.email.set()
    await VakansiyaRu.next()


@dp.message_handler(state=VakansiyaRu.addres)
async def answer_city(message: types.Message, state: FSMContext):
    addres = message.text

    await state.update_data(
        {"addres": addres}
    )

    await message.answer("Ты студент!",reply_markup=studentkeyRu)

    # await PersonalData.email.set()
    await VakansiyaRu.next()


@dp.message_handler(state=VakansiyaRu.student)
async def answer_city(message: types.Message, state: FSMContext):
    student = message.text

    await state.update_data(
        {"student": student}
    )

    await message.answer("Отправить картинку",reply_markup=bekorRu)

    # await PersonalData.email.set()
    await VakansiyaRu.next()




@dp.message_handler(content_types=ContentType.ANY,state=VakansiyaRu.img)
async def answer_img(message: types.Message, state: FSMContext):
    if message.content_type == ContentType.PHOTO:
        photo = message.photo[-1]
        file_id = photo.file_id
        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path

    # Rasmni faylga yuklash
        await bot.download_file(file_path, f"handlers/users/file/imgs/{message.from_user.id}.jpg")
        #await message.photo[-1].download()
        await message.answer("Заработная плата, которую вы ожидаете",reply_markup=salarykeyRu)
        await VakansiyaRu.next()
    else:
        await message.answer("Отправить картинку!")




@dp.message_handler(state=VakansiyaRu.salary)
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


    msg = "Была получена следующая информация:\n"
    msg += f"Город - {city}\n"
    msg += f"Филиал - {filial}\n"
    msg += f"Позиция: - {position}\n"
    msg += f"телефон: - {phon}\n"
    msg += f"Имя: - {name}\n"
    msg += f"Дата рождения: - {date}\n"
    msg += f"Адрес: - {addres}\n"
    msg += f"Студент: - {student}\n"
    msg += f"Зарплата: - {salary}\n\n"
    msg += f"Ваша информация верна!"

    await message.answer(msg,reply_markup=yuborishkeyRu)


    malumotlar = [city,filial,position,phon,name,date,addres,student,salary]


    #await bot.send_message(chat_id=1363350178,text=malumotlar)

    img = f"C:/Users/User/Desktop/Hr_bot/handlers/users/file/imgs/{message.from_user.id}.jpg"
    file = f"C:/Users/User/Desktop/Hr_bot/handlers/users/file/files/{message.from_user.id}.pdf"
    
    
    create_hr_Ru(file,img,malumotlar)

    await VakansiyaRu.next()



@dp.message_handler(state=VakansiyaRu.yuborish)
async def yuborish(message: types.Message,state: FSMContext):
    if message.text == "Отправка":
        await message.answer("Отправил!!!",reply_markup=boshmenuUs)
        await state.finish()
        files = f"C:/Users/User/Desktop/Hr_bot/handlers/users/file/files/{message.from_user.id}.pdf"
        with open(files, "rb") as file:
        # Document jo'natish
            await bot.send_document(chat_id=message.from_user.id, document=file)
    elif message.text == "Отказ":
        await message.answer("Отклоненный!!!",reply_markup=boshmenuUs)
        await state.finish()
        await message.answer("Данные не отправлены!")

    


