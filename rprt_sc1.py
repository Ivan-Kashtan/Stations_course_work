from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak, Image
from reportlab.lib.units import cm
from reportlab.lib import colors

from eq import fml
from page_number import addPageNumber
from paragraph_styles import *
# from report import sp_15, sp_20, sp_25, sp_30

from in_dat import n_g
from sc1 import *
from load import p_g_,q_g_, p_ld_min_sm
from line import *
doc = SimpleDocTemplate(
    'sc1.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=3 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='кз К1 РУСН')

sp_20 = Spacer(0, 20)
sp_1 = Spacer(0, 1 * cm)
sp_25 = Spacer(0, 25)
sp_30 = Spacer(0, 30)
sp_50 = Spacer(0, 50)

f = [Paragraph('Расчет токов короткого замыкания', style=st_b),
     # Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Станции\Курсовая\Компас\Схемы\2 вар. из примера.png',
     #       width=15*cm, height=10*cm, kind='proportional'),
     # Paragraph('Рисунок 4 - Схема замещения для расчета токов короткого замыкания',
     # style=s_c_t),
     Paragraph('Для расчета используем метод ППОЕ', style=s_m),
     Paragraph('Примем следующие значения базисной мощности и напряжения', style=st_0_20),
     fml(f'$S_б = {s_b}$ МВ \u00B7 А; \\quad $U_{{БН}} = {u_b[0]}$ кВ; \\quad $U_{{БС}} = {u_b[1]}$ кВ; '
         f'\\quad $U_{{БВ}} = {u_b[2]}$ кВ;'),
     # fml(f'$U_{{БН}} = {u_b[0]}$ кВ; \\quad'),
     Paragraph('Базисные токи', style=st_0_20),
     fml(f'$I_б = {s_b}$ МВ \u00B7 А; \\quad $U_{{БН}} = {u_b[0]}$ кВ; \\quad $U_{{БС}} = {u_b[1]}$ кВ; '
         f'\\quad $U_{{БВ}} = {u_b[2]}$ кВ;'),
     Paragraph('Прямая последовательность', style=st_0_20),
     # Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Станции\Курсовая\Компас\Схемы\2 вар. из примера.png',
     #       width=15*cm, height=10*cm, kind='proportional'),
     # Paragraph('Рисунок 5 - эквивалентная схема замещения прямой последовательности для расчета тока кз в точке К1',
     # style=s_c_t),
     Paragraph('Индуктивное сопротивление', style=st_0_20),
     fml(f'$x_{{Б_\u0020 11}} = \\dfrac {{ x_{{г1}} + x_т}} {{n_1}}; \\quad'
         f'x_{{Б_\u0020 11}} = \\dfrac{{{x_g[0]:.3f} + {x_t[0]:.3f} }} {{{n1_c}}} = {x_b[0, 0]:.3f}$'),
     sp_30,
     fml(f'$x_{{Б_\u0020 21}} = x_{{г1}} + x_{{т}}; \\quad'
         f'x_{{Б_\u0020 21}} = {x_g[0]:.3f} + {x_t[0]:.3f} = {x_b[0, 1]}$'),
     sp_20,
     fml(f'$x_{{Б_\u0020 31}} = \\dfrac {{x_{{г1}} + x_{{АТ_\u0020 Н}} }} {{2}}; \\quad'
         f'x_{{Б_\u0020 31}} = \\dfrac {{{x_g[0]:.3f} + {x_at[0]:.3f} }} {{{n_at}}} = {x_b[0, 1]:.3f}$'),
     sp_20,
     fml(f'$x_{{с_\u0020 э1}} = \\dfrac {{x_{{л1}} }} {{n_ln}}; \\quad'
         f'x_{{Б_\u0020 31}} = \\dfrac {{{x_g[0]:.3f} + {x_at[0]:.3f} }} {{{n_at}}} = {x_b[0, 1]:.3f}$'),
     sp_20,
     fml(f'$x_{{с_\u0020 э1}} = \\dfrac {{x_{{л1}} }} {{n_ln}}; \\quad'
         f'x_{{Б_\u0020 31}} = \\dfrac {{{x_g[0]:.3f} + {x_at[0]:.3f} }} {{{n_at}}} = {x_b[0, 1]:.3f}$'),

     ]

doc.build(f, onLaterPages=addPageNumber)
