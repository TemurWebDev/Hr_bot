from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_hr_Us(file_path, image_path,data):
    c = canvas.Canvas(file_path, pagesize=letter)

    #c.setFillColorRGB(*background_color_top)


    #c.rect(350, 600, letter[0], letter[1], fill=True)

    
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))

    # Rasmni olish
    img = ImageReader(image_path)

    # Rasmni chap tarafga joylashtirish
    c.drawImage(img, 400, 600, width=110, height=130)

    #O'ng tarafdagi matn
    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("DejaVuSerif", 20)
    c.drawString(110,700, data[4][:20])


    # c.setFillColorRGB(0, 0, 0)  # kok rang
    # c.setFont("Helvetica-Bold", 20)
    # c.drawString(230,700, "QURBONOV")

    # c.setFillColorRGB(0, 0, 0)  # kok rang
    # c.setFont("Helvetica-Bold", 20)
    # c.drawString(110,670, "SODIQ O'G'LI")

    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("DejaVuSerif", 20)
    c.drawString(110,670, f" < {data[2][:17]}  >")

    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Times-Roman", 20)
    c.drawString(110,640, f"Phon:  {data[3][:13]}")

    c.rect(100,600,420,130)

    c.rect(100,150,420,370)

    c.line(310,150,310,520)


    # c.setFillColorRGB(0, 0, 1)  # kok rang
    # c.setFont("Helvetica-Bold", 20)
    # c.drawString(100,540, "Javoblar")


    c.setFillColorRGB(0.8, 0.8, 1)


    #c.rect(350, 600, letter[0], letter[1], fill=True)

    c.rect(100,490,420,30,fill=True)

    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Helvetica-Bold", 18)
    c.drawString(180,500, "Question")


    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Helvetica-Bold", 18)
    c.drawString(380,500, "Answer")


    # c.setFillColorRGB(0, 0, 0)  # kok rang
    # c.setFont("Times-Roman", 18)
    # c.drawString(110,460, "Addres")


    boshlanish_s = 460

    savollar = ["City","Branch","Date of birth","Addres","Student","Monthly salary"]

    javoblar = [data[0],data[1],data[5],data[6],data[7],data[8]]


    for savol in savollar:
        c.setFillColorRGB(0, 0, 0)  # kok rang
        c.setFont("DejaVuSerif", 18)
        c.drawString(110,boshlanish_s, savol)
        boshlanish_s = boshlanish_s-30
        


    boshlanish_j = 460

    for javob in javoblar:
        c.setFillColorRGB(0, 0, 0)  # kok rang
        c.setFont("DejaVuSerif", 18)
        c.drawString(320,boshlanish_j, javob[:18])
        boshlanish_j = boshlanish_j-30
        




    
    c.save()

#if __name__ == "__main__":

    #background_color_top = (0.8, 0.8, 1)

    # image_file_path = "file/imgs/tima.jpg"
    # pdf_file_path = "file/files/hrfile.pdf"
    # create_image_with_greeting(pdf_file_path, image_file_path)
    # print(f"PDF file created at: {pdf_file_path}")
