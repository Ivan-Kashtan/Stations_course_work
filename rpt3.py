from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak
from reportlab.lib.units import cm
from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet

from gen import *
from load import *
from paragraph_styles import *
# from page_number import *
from title_list import *
from eq import *
from in_dat import *


# import var1 as v1
# import var2 as v2
# import var3 as v3
# import line as ln

def p_n(canvas, doc):
    # номера страниц
    page_num = canvas.getPageNumber()
    text = str(page_num)
    # canvas.drawRightString(20*cm, 2*cm, text)
    # canvas.textsize = 12
    # canvas.fonts = 'Times-Roman'
    canvas.drawString(12*cm, 1*cm, text)


# styles = getSampleStyleSheet()
doc = SimpleDocTemplate(
    'rpt2.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=3 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='Проектирование электрической части КЭС 5600 МВт')
