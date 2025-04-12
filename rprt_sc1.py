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
     Paragraph('Примем следующие значения базисной мощности и базисных напряжений', style=st_0_10),
     fml(f'$S_б = {s_b}$ МВ \u00B7 А; $ \\quad U_{{б_\u0020 Н}} = {u_b[0]}$ кВ; $\\quad U_{{б_\u0020 С}}={u_b[1]}$ кВ;'
         f'$ \\quad U_{{б_\u0020 В}} = {u_b[2]}$ кВ;'),
     # fml(f'$U_{{БН}} = {u_b[0]}$ кВ; \\quad'),
     Paragraph('Базисные токи', style=st_5_10),
     fml(f'$I_{{б_\u0020 1}} = {i_b[0]:.2f}$ кА; $\\quad I_{{б_\u0020 2}} = {i_b[1]:.2f}$ кА; $\\quad '
         f'I_{{б_\u0020 3}} = {i_b[2]:.2f}$ кА;'),
     Paragraph('Параметры генератора', style=st_5_10),
     fml(f'$E_г = 1 + x\'\'_d \\sin \\phi_г; \\quad'
         f'E_г = 1 + {x_d__:.3f} \\cdot {sin_g:.3f} = {e_g:.3f}$'),
     sp_20,
     fml(f'$x_{{г1}} = x\'\'_d \\cdot \\dfrac {{S_б}} {{S_{{г_\u0020 ном}} }}; \\quad'
         f'x_{{г1}} = {x_d__:.3f} \\cdot \\dfrac {{{s_b:.0f}}} {{{s_g:.1f}}} = {x_g[0]:.3f}$'),
     sp_30,
     fml(f'$x_{{г2}} = x_2 \\cdot \\dfrac {{S_б}} {{S_{{г_\u0020 ном}} }}; \\quad'
         f'x_{{г2}} = {x2:.3f} \\cdot \\dfrac {{{s_b}}} {{{s_g:.1f}}} = {x_g[1]:.3f}$'),
     sp_20,
     fml(f'$r_г = \\dfrac {{x_{{г1}}}} {{\\omega T_{{ar}} }}; \\quad'
         f'r_г = \\dfrac {{ {x_g[0]:.3f} }} {{ {omega:.0f} \\cdot {t_ar:.3f} }} = {r_g:.3f}$'),

     Paragraph('Параметры трансформатора блока, подключенного к РУСН', style=st_20_20),
     fml(f'$x_т = u_к \\dfrac {{S_б}} {{S_{{т_\u0020 ном}}}}; \\quad'
         f'x_г = {u_sc_tb[0] / 100} \\dfrac {{ {s_b} }} {{ { s_tb[0] } }} = {x_t[0]:.3f}$'),
     sp_20,
     fml(f'$r_т = \\dfrac {{\u0394 P_к S_б}} {{S^2_{{т \u0020 ном}} }}; \\quad'
         f'r_т = \\dfrac {{ {p_sc_tb[0]} \\cdot {s_b} }} {{ {s_tb[0]:.0f}^2}} = {r_t[0]:.3f}$'),
     Paragraph('Параметры автотрансформатора', style=st_20_20),
     # fml(f'$u_{{к_\u0020 В}} = 0,5 \\left( u_{{В_\u0020 Н}} + u_{{В_\u0020 С}} - u_{{Н_\u0020 С}} \\right); \\quad'
     #     f'u_{{к_\u0020 В}} = 0,5 \\left( {u_sc_at[1]} + {u_sc_at[0]} - {u_sc_at[2]} \\right) = {u_sc_at_c[0]:.2f}$'),
     # sp_20,
     # fml(f'$u_{{к_\u0020 С}} = 0,5 \\left( u_{{Н_\u0020 С}} + u_{{В_\u0020 С}} - u_{{В_\u0020 Н}} \\right); \\quad'
     #     f'u_{{к_\u0020 С}} = 0,5 \\left( {u_sc_at[2]} + {u_sc_at[0]} - {u_sc_at[1]} \\right) = '
     #     f'{0.5*(u_sc_at[2] + u_sc_at[0] - u_sc_at[1]):.2f} \u2192 0 $'),
     # sp_20,
     # fml(f'$u_{{к_\u0020 Н}} = 0,5 \\left( u_{{В_\u0020 Н}} + u_{{Н_\u0020 С}} - u_{{В_\u0020 С}} \\right); \\quad'
     #     f'u_{{к_\u0020 Н}} = 0,5 \\left( {u_sc_at[1]} + {u_sc_at[2]} - {u_sc_at[0]} = {u_sc_at_c[2]:.2f}\\right)$'),
     # sp_30,
     # fml(f'$x_{{АТ_\u0020 В}} = u_{{к_\u0020 В}} \\dfrac {{S_б}} {{ S_{{т_\u0020 ном}} }}; \\quad'
     #     f'x_{{АТ_\u0020 В}} = {u_sc_at_c[0]:.2f} \\dfrac {{{s_b}}}  {{{s_at}}} = {x_at[0]:.3f}$'),
     # sp_30,
     # fml(f'$x_{{АТ_\u0020 Н}} = u_{{к_\u0020 Н}} \\dfrac {{S_б}} {{S_{{т_\u0020 ном}} }}; \\quad'
     #     f'x_{{АТ_\u0020 Н}} = {u_sc_at_c[2]:.2f} \\dfrac {{{s_b}}}  {{{s_at}}} = {x_at[2]:.3f}$'),
     # sp_30,
     # fml(f'$r_{{АТ_\u0020 В}} = \\dfrac {{\u0394 P_к S_б}} {{S^2_{{т \u0020 ном}} }}; \\quad'
     #     f'r_{{АТ_\u0020 В}} = \\dfrac {{ {p_sc_at} \\cdot {s_b} }} {{ {s_at}^2}} = {r_at[0]:.3f}$'),
     # sp_30,
     # fml(f'$r_{{АТ_\u0020 Н}} = \\dfrac {{\u0394 P_к S_б}} {{S^2_{{т \u0020 ном}} }}; \\quad'
     #     f'r_{{АТ_\u0020 Н}} = \\dfrac {{ {p_sc_at} \\cdot {s_b}}} {{{s_at[2]}^2}} = {r_at[2]:.3f}$'),
     fml(f'$x_{{АТ_\u0020 В}} = {x_at[0]}; \\quad x_{{АТ_\u0020 С}} = {x_at[1]}; \\quad x_{{АТ_\u0020 Н}} = {x_at[2]}'),
     sp_20,
     fml(f'$r_{{АТ_\u0020 В}} = {r_at[0]}; \\quad r_{{АТ_\u0020 С}} = {r_at[1]}; \\quad r_{{АТ_\u0020 Н}} = {r_at[2]}'),

     Paragraph('Параметры линий и системы', style=st_20_20),
     fml(f'$E_с = {e_s}$'),
     sp_30,
     fml(f'$x_с = \\dfrac {{S_б}} {{S\'\'_кз}}; \\quad x_с = \\dfrac {{{s_b}}} {{{s_sc}}} = {x_n:.3f} $'),
     sp_30,
     fml(f'$r_с = {r_n} $'),
     sp_30,
     fml(f'$x_{{л1}} = x_{{уд}} L_л \\dfrac  {{S_б}} {{U_б^2}}; \\quad '
         f'x_{{л1}} = {ln.x} \\cdot {l_ln} \\dfrac  {{{s_b}}} {{ {u_b[2]}^2 }} = {x_ln[0]:.3f} $'),
     Paragraph('Прямая последовательность', style=st_i_5_2),
     # Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Станции\Курсовая\Компас\Схемы\2 вар. из примера.png',
     #       width=15*cm, height=10*cm, kind='proportional'),
     # Paragraph('Рисунок 5 - эквивалентная схема замещения прямой последовательности для расчета тока кз в точке К1',
     # style=s_c_t),
     Paragraph('Индуктивное сопротивление', style=st_0_20),
     fml(f'$x_{{Б_\u0020 11}} = \\dfrac {{ x_{{г1}} + x_т}} {{n_1}}; \\quad'
         f'x_{{Б_\u0020 11}} = \\dfrac{{{x_g[0]:.3f} + {x_t[0]:.3f} }} {{{n1_c}}} = {x_b[0, 0]:.3f}$'),
     sp_20,
     fml(f'$x_{{Б_\u0020 21}} = x_{{г1}} + x_{{т}}; \\quad'
         f'x_{{Б_\u0020 21}} = {x_g[0]:.3f} + {x_t[0]:.3f} = {x_b[0, 1]:.3f}$'),
     sp_30,
     fml(f'$x_{{Б_\u0020 31}} = \\dfrac {{x_{{г1}} + x_{{АТ_\u0020 Н}} }} {{2}}; \\quad'
         f'x_{{Б_\u0020 31}} = \\dfrac {{{x_g[0]:.3f} + {x_at[2]:.3f} }} {{{n_at}}} = {x_b[0, 1]:.3f}$'),
     sp_30,
     fml(f'$x_{{с_\u0020 э1}} = \\dfrac {{x_{{л1}} }} {{n_л}} + x_с; \\quad'
         f'x_{{с_\u0020 э1}} = \\dfrac {{{x_ln[1]:.5f} }} {{{n_ln}}} + {x_n:.3f}= {x_n_e[1]:.3f}$'),
     sp_30,
     fml(f'$x_{{АТ_\u0020 э1}} = \\dfrac {{x_{{АТ_\u0020 В}} }} {{n_{{АТ}} }}; \\quad'
         f'x_{{АТ_\u0020 э1}} = \\dfrac {{ {x_at[0]:.3f} }} {{{n_at}}} = {x_at_e:.3f}$'),
     sp_30,
     fml(f'$x_{{э_\u0020 11}} = \\dfrac {{x_{{Б_\u0020 11}} x_{{Б_\u0020 31}} }} '
         f'{{x_{{Б_\u0020 11}} + x_{{Б_\u0020 31}} }}; \\quad'
         f'x_{{АТ_\u0020 э1}} = \\dfrac {{ {x_b[0, 0]:.3f} \\cdot {x_b[0, 2]:.3f} }} {{{x_b[0, 0]:.3f} + '
         f'{x_b[0, 2]:.3f} }} = {x_e1[0]:.3f}$'),
     sp_30,
     fml(f'$x_{{э_\u0020 21}} = \\dfrac {{x_{{с_\u0020 э1}} x_{{Б_\u0020 21}} }} '
         f'{{x_{{с_\u0020 э1}} + x_{{Б_\u0020 21}} }}; \\quad'
         f'x_{{э_\u0020 21}} = \\dfrac {{ {x_b[0, 0]:.3f} \\cdot {x_b[0, 2]:.3f} }} '
         f'{{{x_b[0, 0]:.3f} + {x_b[0, 2]:.3f} }} = {x_e2[0]:.3f}$'),
     sp_30,
     fml(f'$x_{{К1_\u2211}} = \\dfrac {{ x_{{э_\u0020 11}} \\left( x_{{АТ_\u0020 э1}} + x_{{Б_\u0020 21}} \\right) }} '
         f'{{x_{{э_\u0020 11}} x_{{АТ_\u0020 э1}} + x_{{Б_\u0020 21}} }}; \\quad'
         f'x_{{К1_\u2211}} = \\dfrac {{ {x_e1[0]:.3f} \\cdot \\left( {x_at_e:.3f} + {x_e2[0]:.3f} \\right)}} '
         f'{{ {x_e1[0]:.3f} + {x_at_e:.3f} + {x_e2[0]:.3f} }} = {x_s[0]:.3f}$'),

     Paragraph('Активное сопротивление', style=st_20_20),
     fml(f'$r_{{Б_\u0020 1}} = \\dfrac {{r_г + r_т}} {{n_1}}; \\quad'
         f'r_{{Б_\u0020 1}} = \\dfrac{{{r_g:.3f} + {r_t[0]:.3f} }} {{{n1_c}}} = {r_b[0]:.3f}$'),
     sp_20,
     fml(f'$r_{{Б_\u0020 2}} = r_г + r_т; \\quad'
         f'r_{{Б_\u0020 2}} = {r_g:.3f} + {r_t[0]:.3f} = {r_b[1]:.3f}$'),
     sp_30,
     fml(f'$r_{{Б_\u0020 3}} = \\dfrac {{r_г + r_{{АТ_\u0020 Н}} }} {{2}}; \\quad'
         f'r_{{Б_\u0020 3}} = \\dfrac {{{r_g:.3f} + {r_at[2]:.3f} }} {{{n_at}}} = {x_b[0, 1]:.3f}$'),
     sp_30,
     fml(f'$r_{{с_\u0020 э}} = \\dfrac {{r_л}} {{n_л}} + r_с; \\quad'
         f'r_{{с_\u0020 э}} = \\dfrac {{{r_ln:.5f} }} {{{n_ln}}} + {r_n}= {r_n_e:.3f}$'),
     sp_30,
     fml(f'$r_{{АТ_\u0020 э}} = \\dfrac {{r_{{АТ_\u0020 В}} }} {{n_{{АТ}} }}; \\quad'
         f'r_{{АТ_\u0020 э}} = \\dfrac {{ {r_at[0]:.3f} }} {{{n_at}}} = {r_at_e:.3f}$'),
     sp_30,
     fml(f'$r_{{э_\u0020 1}} = \\dfrac {{r_{{Б_\u0020 1}} r_{{Б_\u0020 3}} }} '
         f'{{r_{{Б_\u0020 1}} + r_{{Б_\u0020 3}} }}; \\quad'
         f'r_{{АТ_\u0020 э}} = \\dfrac {{ {r_b[0]:.3f} \\cdot {r_b[2]:.3f} }} {{{r_b[0]:.3f} + '
         f'{r_b[2]:.3f} }} = {r_e1:.3f}$'),
     sp_30,
     fml(f'$r_{{э_\u0020 2}} = \\dfrac {{r_{{с_\u0020 э}} r_{{Б_\u0020 2}} }} '
         f'{{r_{{с_\u0020 э}} + r_{{Б_\u0020 2}} }}; \\quad'
         f'r_{{э_\u0020 2}} = \\dfrac {{ {r_b[0]:.3f} \\cdot {r_b[2]:.3f} }} '
         f'{{{r_b[0]:.3f} + {r_b[2]:.3f} }} = {r_e2:.3f}$'),
     sp_30,
     fml(f'$r_{{К1_\u2211}} = \\dfrac {{ r_{{э_\u0020 1}} \\left( r_{{АТ_\u0020 э}} + r_{{Б_\u0020 2}} \\right) }} '
         f'{{r_{{э_\u0020 1}} r_{{АТ_\u0020 э}} + r_{{Б_\u0020 2}} }}; \\quad'
         f'r_{{К1_\u2211}} = \\dfrac {{ {r_e1:.3f} \\cdot \\left( {r_at_e:.3f} + {r_e2:.3f} \\right)}} '
         f'{{ {r_e1:.3f} + {r_at_e:.3f} + {r_e2:.3f} }} = {r_s:.3f}$'),

     ]

doc.build(f, onLaterPages=addPageNumber)
