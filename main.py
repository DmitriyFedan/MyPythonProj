from tkinter import *
from tkinter import messagebox
from datetime import datetime
from random import randint

# ====создание и настройки даты и времени =====
class Alarms:
    user_HH = 0
    user_MM = 0
    user_mess = "NULL"

    def __init__(self, HH, MM, mess="Будильник"):
        self.user_HH = HH
        self.user_MM = MM
        self.user_mess = mess


class Clock:
    # ====   ==========
    now = datetime.now()
    day_month = now.strftime("%d.%m.%y")
    hh_mm_ss = now.strftime("%H:%M:%S")

    alarms_dict = {}  # словарь будильников
    alarm_num = 0  # номер будильника для формирования списка
    alarm_on = True
    user_HH = 0
    user_MM = 0
    user_mess = "NULL"

    def alarm_ring(self):
        if self.alarm_on == True:
            for i in self.alarms_dict:
                if self.now.hour >= int(self.alarms_dict[i].user_HH) and \
                        self.now.minute >= int(self.alarms_dict[i].user_MM):
                    messagebox.showinfo("Будильник", "Будильник сработал " + self.alarms_dict[i].user_mess)
                    if i in self.alarms_dict:
                        del self.alarms_dict[i]
                        self.alarms_list_refresh()
                        self.alarm_ring()
                        break

    def date_refresh(self):
        self.now = datetime.now()
        self.day_month = self.now.strftime("%d.%m.%y")
        self.hh_mm_ss = self.now.strftime("%H:%M:%S")
        date_label["text"] = self.day_month
        time_label["text"] = self.hh_mm_ss
        alarm_label["text"] = str(self.user_HH) + ":" + str(self.user_MM)

    # this function reading user time from (entry`s   ent h & ent m)
    # and remember in class
    def read_time(self):

        try:
            self.user_HH = ent_H.get()
            self.user_MM = ent_M.get()
            self.user_mess = ent_mess.get()
            if 0 <= int(self.user_HH) <= 24 and 0 <= int(self.user_MM) <= 59:
                messagebox.showinfo("OK", "Время установлено")
                self.alarm_on = True
                self.alarm_create(self.user_HH, self.user_MM, self.user_mess)

            else:
                messagebox.showinfo("Ошибка", "Введите корректное время")
                self.entry_s_clear()
        except ValueError:
            messagebox.showinfo("Ошибка", "Введите время")
            self.entry_s_clear()

    def alarm_create(self, hh, mm, mess):
        next_name = "alarmNumber {}".format(self.alarm_num)
        self.alarm_num += 1
        if mess != "":
            self.alarms_dict[next_name] = self.alarms_dict.get(next_name, Alarms(hh, mm, mess))
            self.alarms_list_refresh()
        else:
            self.alarms_dict[next_name] = self.alarms_dict.get(next_name, Alarms(hh, mm))
            self.alarms_list_refresh()

    def alarms_list_refresh(self):
        alarms_listbox.delete(0, alarms_listbox.size())

        for i in self.alarms_dict:
            alarm_text = self.alarms_dict[i].user_HH + ":" + \
                         self.alarms_dict[i].user_MM + "  " + \
                         self.alarms_dict[i].user_mess
            alarms_listbox.insert(END, alarm_text)
        self.alarms_dict.sort()

    def entry_s_clear(self):
        ent_M.delete(0, 50)
        ent_H.delete(0, 50)
        ent_mess.delete(0, 50)
        a = Canvas.createimage()


# ====== настраиваемые параметры =======
width_but = 8  # ширина кнопок старт и стоп
height_but = 1  # высота кнопок старт и стоп
font_but = "Times_new_roman 8 bold"  # шрифт 1

x1coord = 10  # первая координата по х для привязки  виджетов
y1coord = 5  # первая координата по y для привязки виджетов

x2coord = 120
y2coord = 5

alarma = Clock()

# ====== Оформаление =======
wind_1 = Tk()
wind_1.geometry("300x400")
wind_1.resizable(False, False)

# =====Кнопка старта будильника =====
btn_start = Button(wind_1,
                   text="Старт",
                   width=width_but,
                   height=height_but,
                   font=font_but,
                   anchor="c",
                   activebackground="green",
                   command=alarma.read_time)

# ====== Кнопка остановка будильника =====
btn_stop = Button(wind_1,
                  text=" Стоп",
                  width=width_but,
                  height=height_but,
                  font=font_but,
                  anchor="c",
                  activebackground="red")

# ======= лэйблы =========

# дата
datetext_label = Label(wind_1, text="Сегодня", anchor="c", font="Arial 8 bold")
date_label = Label(wind_1, text="Сейчас обновлю", anchor="c", font="Arial 12 bold")

# ========= время =================
timetext_label = Label(wind_1, text="Текущее время", anchor="c", font="Arial 8 bold")
time_label = Label(wind_1, text="Сейчас обновлю", anchor="c", font="Arial 12 bold")

# ========надпись над полем ввода =======
entry_label = Label(wind_1, text="Введите время", anchor="c", font="Arial 7 bold")
# ===установленный будильник
alarm_label = Label(wind_1,
                    text=str(alarma.user_HH) + ":" + str(alarma.user_MM),
                    font=font_but)
alarm_label.place(x=200, y=200)

# ====== ввод данных =====
ent_H = Entry(wind_1, width=2, font="Arial 15 bold")  # поле ввода часов
ent_M = Entry(wind_1, width=2, font="Arial 15 bold")  # минут
ent_mess = Entry(wind_1, width=10, font="Arial 8 bold")

# =======
alarms_listbox = Listbox()

# =======================================================
# ===== =====позиционирование виджетов========================
datetext_label.place(x=x1coord, y=y1coord)  # надпись (Сегодня)
date_label.place(x=x1coord, y=y1coord + 20)  # надпись  отображающая дату
timetext_label.place(x=x1coord, y=y1coord + 40)  # надпись (текущее время)
time_label.place(x=x1coord, y=y1coord + 60)  # надпись отображающая время
entry_label.place(x=x1coord - 5, y=y1coord + 80)  # надпись (Введите время)
ent_H.place(x=x1coord, y=y1coord + 100)  # поле ввода час
ent_M.place(x=x1coord + 40, y=y1coord + 100)  # поле ввода минуты
ent_mess.place(x=x1coord, y=y1coord + 145)  # поле ввода сообщения
btn_start.place(x=x1coord, y=y1coord + 170)  # кнопка старт
btn_stop.place(x=x1coord, y=y1coord + 200)  # кнопка стоп
alarms_listbox.place(x=x2coord, y=y2coord)


# ==========================================================
# ===========================================================
def main():
    alarma.date_refresh()
    alarma.alarm_ring()
    wind_1.after(1000, main)


main()
wind_1.mainloop()
