from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from reportlab.lib.utils import ImageReader
from aiogram.types import ContentType

from data.config import ADMINS
from loader import dp, db, bot

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboards.default.vakansiyaKeyUs import citykeyUs,filialkeyUs,positionkeyUs,studentkeyUs,salarykeyUs,phonkeyUs,yuborishkeyUs
from keyboards.default.userkey import boshmenuUs,bekorUs

from handlers.users.hrUs import create_hr_Us

# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class VakansiyaUs(StatesGroup):
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





@dp.message_handler(text="🖋 Job vacancy")
async def startState(message: types.Message):
    user = db.select_user(chat_id=message.from_user.id)
    if user[4] == "en":
        await message.answer("Choose a city!",reply_markup=citykeyUs)
        await VakansiyaUs.city.set()
    else:
        await message.answer(message.text)


@dp.message_handler(state=VakansiyaUs.city)
async def answer_city(message: types.Message, state: FSMContext):
    city = message.text

    await state.update_data(
        {"city": city}
    )

    await message.answer("Choose a branch!",reply_markup=filialkeyUs)

    # await PersonalData.email.set()
    await VakansiyaUs.next()


@dp.message_handler(state=VakansiyaUs.filial)
async def answer_city(message: types.Message, state: FSMContext):
    filial = message.text

    await state.update_data(
        {"filial": filial}
    )

    await message.answer("Choose the position that interests you!",reply_markup=positionkeyUs)

    # await PersonalData.email.set()
    await VakansiyaUs.next()


@dp.message_handler(state=VakansiyaUs.position)
async def answer_city(message: types.Message, state: FSMContext):
    position = message.text

    await state.update_data(
        {"position": position}
    )

    await message.answer("Send a phone number!",reply_markup=phonkeyUs)

    # await PersonalData.email.set()
    await VakansiyaUs.next()



@dp.message_handler(state=VakansiyaUs.phon,content_types=types.ContentTypes.CONTACT)
async def answer_city(message: types.Message, state: FSMContext):
    phon = message.contact.phone_number

    await state.update_data(
        {"phon": phon}
    )

    await message.answer("Write your first and last name\nexample: Temurbek Qurbonov",reply_markup=bekorUs)

    # await PersonalData.email.set()
    await VakansiyaUs.next()



@dp.message_handler(state=VakansiyaUs.name)
async def answer_city(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )

    await message.answer("Date of birth! Example: 07.07.1999")

    # await PersonalData.email.set()
    await VakansiyaUs.next()


@dp.message_handler(state=VakansiyaUs.date)
async def answer_city(message: types.Message, state: FSMContext):
    date = message.text

    await state.update_data(
        {"date": date}
    )

    await message.answer("Enter your residential address! Example: Almazor district")

    # await PersonalData.email.set()
    await VakansiyaUs.next()


@dp.message_handler(state=VakansiyaUs.addres)
async def answer_city(message: types.Message, state: FSMContext):
    addres = message.text

    await state.update_data(
        {"addres": addres}
    )

    await message.answer("You are students!",reply_markup=studentkeyUs)

    # await PersonalData.email.set()
    await VakansiyaUs.next()


@dp.message_handler(state=VakansiyaUs.student)
async def answer_city(message: types.Message, state: FSMContext):
    student = message.text

    await state.update_data(
        {"student": student}
    )

    await message.answer("Send a picture",reply_markup=bekorUs)

    # await PersonalData.email.set()
    await VakansiyaUs.next()




@dp.message_handler(content_types=ContentType.ANY,state=VakansiyaUs.img)
async def answer_img(message: types.Message, state: FSMContext):
    if message.content_type == ContentType.PHOTO:
        photo = message.photo[-1]
        file_id = photo.file_id
        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path

    # Rasmni faylga yuklash
        await bot.download_file(file_path, f"handlers/users/file/imgs/{message.from_user.id}.jpg")
        #await message.photo[-1].download()
        await message.answer("The salary you expect",reply_markup=salarykeyUs)
        await VakansiyaUs.next()
    else:
        await message.answer("Send a picture!!")




@dp.message_handler(state=VakansiyaUs.salary)
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


    msg = "The following information was received:\n"
    msg += f"City - {city}\n"
    msg += f"Filial - {filial}\n"
    msg += f"Position: - {position}\n"
    msg += f"Phon: - {phon}\n"
    msg += f"Name: - {name}\n"
    msg += f"Date: - {date}\n"
    msg += f"Addres: - {addres}\n"
    msg += f"Student: - {student}\n"
    msg += f"Salary: - {salary}\n\n"
    msg += f"Your information is correct!"

    await message.answer(msg,reply_markup=yuborishkeyUs)


    malumotlar = [city,filial,position,phon,name,date,addres,student,salary]


    #await bot.send_message(chat_id=1363350178,text=malumotlar)

    img = f"C:/Users/User/Desktop/Hr_bot/handlers/users/file/imgs/{message.from_user.id}.jpg"
    file = f"C:/Users/User/Desktop/Hr_bot/handlers/users/file/files/{message.from_user.id}.pdf"
    
    
    create_hr_Us(file,img,malumotlar)

    await VakansiyaUs.next()



@dp.message_handler(state=VakansiyaUs.yuborish)
async def yuborish(message: types.Message,state: FSMContext):
    if message.text == "Sending":
        await message.answer("Sent!!!",reply_markup=boshmenuUs)
        await state.finish()
        files = f"C:/Users/User/Desktop/Hr_bot/handlers/users/file/files/{message.from_user.id}.pdf"
        with open(files, "rb") as file:
        # Document jo'natish
            await bot.send_document(chat_id=message.from_user.id, document=file)
    elif message.text == "Refusal":
        await message.answer("Rejected",reply_markup=boshmenuUs)
        await state.finish()
        await message.answer("Data not sent!")

    


