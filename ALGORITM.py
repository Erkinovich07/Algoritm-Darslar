
" Algaretim mavzusi "
# 1_Malumotlar tuzulmasi va algaretimlar nima uchun kerek
# 2_Fanni dolzarbligi
# 3_Ma'lumotlar tuzulmasiga misollar
# 4_Algaretimlar

"""<<< MALUMOTLAR TUZULMASI VA ALGARETIMLAR DASTURLASHNI NEGIZI! >>>"""
# _____________________________________________________________________________________________________________________

"""DASTUR VA ALGARETIM NIMA"""
# Dastur (muammo) qanchalik murkkab bo'lmasin,biz uni bir bir nechta sodda  muammolarga bo'lib olamiz
# va har bir muammoga qadama-qadam yechim taklif qilamiz.bu Algaretim diyiladi    
# algaretim = bu qadama-qadam muammoni yechimi
# bitta muammoga bir nechta yechim bo'lishi mumkun

"""Ma'lumotlar"""
# malumotlar kampyuter xotirasida saqlanuvchi matn, rasm, vedio, audio, dasturlar, jadvallar va boshqa axborot

"""ma'lumotlar tuzulmasi"""
# ma'lumotlar tuzulmasi ma'lumotlardan samarali foydalanish uchun tartibga solishni o'ziga xos usuli. 
 
# ___________________________________________________________________________________________________________________

"""FANNI DOLZARBLIGI"""
# Bitta muammoga bir nechta yechim bo'lishi mumkun
# Mavjud ma'lumotlar tuzulmasi va algaretimlardan xabardor bo'lish eng samarali yechimnni topishda yordam beradi
# Samaradorlik algaretimning TEZLIGI va qancha XOTIRA egallshi bilan o'lchanadi (time and complexity)
# KATTA LOYIHALARDA BEVOSITA KOD YOZISH JARAYONI 20-30% XOLOS
# AKSAR VAQT KAMPANYA RESURSLARINI (SERVERLAR, HISOBLASH QUVVATI, VA BOSHQALARNI) TEJASH UCHUN ENG OPTIMAL ALGARETIMLARNI LOYIHALASHTIRISHGA SARFLANADI
# SHuning uchun katta kompanyalar ishga olishda aynan algaretimlar va ma'lumotlar tuzulmasini qanchalik bilishingiz tekshiradi
# Dasturlash tili va turli frenworklari ikkilamchi
# Tasavvur qiling siz ustida ishlayotgan dasturning millonlab foydalanuvchilari bor (bank,online qidiruv,ijtimoiy tarmoq,rasmlar uchun bulut xizmati,yangi super o'yin,elektron kutubxona va hokazo)  
# Ma'lumotlar xar soniyada yangilanib turadi
# Siz har bir mijoz haqida minglab ma'lumotlarni saqlab borishingiz va kerak bo'lgan ma'lumotlarni bir zumda topib berishingiz kerak
# ____________________________________________________________________________________________________________________________________________________________________________________________________

"""MALUMOTLAR TUZULMASI"""
# |_A_|_B_|_A_|_C_|_E_|_B_|_D_|_E_| = Array (ro'yxat)



# |_0_|_5_|_4_|_3_|_0_|_5_|_3_|_5_|
# |_7_|_1_|_3_|_3_|_4_|_4_|_2_|_1_|
# |_5_|_8_|_4_|_2_|_9_|_5_|_3_|_5_| = 2-3-N o'lchamli ro'yxat
# |_2_|_5_|_4_|_3_|_4_|_8_|_3_|_1_|

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#   --|_3_|   Linked list (bog'langan ro'yxat)                      Stacks                  Queues 
#   |                                                                 | ^                      | 
#   |_ |_5_|_A_|--|_8_|_E_|--|_4_|_E_|                                v |                      v
#                                    |                                                         
#                                    |                              0 |_0_|                0 |_5_|
#                                |_0_|                              1 |_7_|                1 |_1_|
#                                                                   2 |_5_|                2 |_8_|       <--------------------- (birinchi kirgan ma'lumot birinchi bo'lib chiqib ketadi)
# (telda rasmlar otqizish va yana usha rasmga qaytish)              3 |_2_|                3 |_5_|
#                                                                   4 |_5_|                4 |_5_|
#                                                                   5 |_2_|                5 |_2_|
#                                                                       
#                                                                       ^               
#                                                                       |
#                                                                       |
#                                                                       |
#                                                                       |
#                                                                       |
#                                                                       |    
#                                    birinchi kirgan ma'lumot ikkinchi bo'lib chiqib keladi)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# GRAPH (Grflar) turli hil tugunlar bo'ladi u tugunlar bir biriga bo'glangan bo'ladi bu tugunlarni viloyatlarga qiyoslasak ham bo'ladi va (xaritani misol qilib keltirsak bo'ladi toshkentdan samarqandga yaqin yolni topsh)
# SHajara (Tree) misol uyda yoshi katta bobongiz buvingiz ota onagiz akagiz va ohirida siz borsiz 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# HASH JADVALLAR                                                                
#   kalit       qiymat
# |_anvar_|----|_python_|
# |_olim_|-----|_html/css_|
# |_hasan_|----|_java_|

# Heap (buham shajara ga o'xshash bo'ladi,farqi qiymatlar o'sish va kamayish tartibida saqlanga bo'ladi)

# ----------------------------------------------------------------------------------------------------------

"""ALGARETIMLAR"""
# Akasar muammolar ma'lumotlarni tartiblashga va qidirishga borib taqaladi
# Biz o'rganadigan aksar algaretimlar ham aynan TARTIBLASH ga va QIDIRISHGA (Sorting and Searching) algoritimlar haqida bo'ladi

#  soarting                        searching        

# bubble sort                      recursion
# Selection sort                   linear search
# Merge sort                       binary search
# Quick sort                       jump search
# Heap sort
# bucket sort