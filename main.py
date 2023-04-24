import json
from datetime import datetime
import re

with open("data.json", "r") as f:
    tamplate = json.load(f)

class tamagocha():
    def __init__(self, name, eda, socialka, bdsm, trash, tired):
        self.name = name
        self.eda = eda
        self.socialka = socialka
        self.bdsm = bdsm
        self.trash = trash
        self.tired = tired


    def interface(self):
        do = int(input())

        if do == 1:
            print("Статус\n" + str(self.name) +
                ("\nГолод = " + str(self.eda)) +
                ("\nУсталость = " + str(self.tired)) +
                ("\nУровень загрязненности комнаты = " + str(self.trash)) +
                ("\nПотебность в общении = "+ str(self.socialka)) +
                ("\nПотребность в страданиях = " + str(self.bdsm)))

        elif do == 2:
            self.eda = 100
            print("Спасибо было вкусно!\n" + "Голод = " + str(self.eda))

        elif do == 3:
            self.tired = 100
            print("Я выспалась!\n" + "Усталость = " + str(self.tired))

        elif do == 4:
            self.trash = 100
            print("Какая чистота!\n" + "Уровень загрязнения = " + str(self.trash))

        elif do == 5:
            self.socialka = 100
            print("Я так хорошо погуляла!\n" + "Потребность в общении = " + str(self.socialka))

        elif do == 6:
            self.bdsm = 100
            print("Это было великолепно!\n" + "Потребность в страданиях = " + str(self.bdsm))

        elif do == 7:
            return do

        else:
            print("Я не понимаю, повторите еще раз.")

        if self.eda <= 0:
            print("Ваш персонаж умер от голода")
        elif self.trash <= 0:
            print("Ваш персонаж умер в грязи от инфекций")
        elif self.bdsm <= 0:
            print("Ваш персонаж совершил суицид")
        elif self.tired <= 0:
            print("Ваш персонаж устал до смерти")
        elif self.socialka <= 0:
            print("Ваш персонаж умер от одиночества")
        return do



print("Добро пожаловать домой! Что вы хотите сделать, хозяин?\n" + "Посмотреть статус - 1\n"
       + "Покормить - 2\n" + "Отправить в кровать - 3\n"
       + "Навести порядки и покупать - 4\n" + "Отправить на прогулку - 5\n" + "Отправить в БДСМ клуб - 6\n")

tamagocha1 = tamagocha(tamplate["name"], tamplate["eda"],
                       tamplate["socialka"], tamplate["bdsm"],
                       tamplate["trash"],tamplate["tired"])

now = datetime.now()
time = tamplate["time"]
c = re.split(":| |-", time)
y = int(c[0])
m = int(c[1])
d = int(c[2])
h = int(c[3])
min = int(c[4])
s = int(c[5])
time1 = datetime(y, m, d, h, min, s)
data = now - time1
tamagocha1.eda = tamagocha1.eda - data.seconds//60//15
tamagocha1.socialka = tamagocha1.socialka - data.seconds//60//20
tamagocha1.bdsm = tamagocha1.bdsm - data.seconds//60//60
tamagocha1.tired = tamagocha1.tired - data.seconds//60//15
tamagocha1.trash = tamagocha1.trash - data.seconds//60//25
end=0
while end!=7:
      end=tamagocha1.interface()

tamplate["eda"] = tamagocha1.eda
tamplate["socialka"] = tamagocha1.socialka
tamplate["bdsm"] = tamagocha1.bdsm
tamplate["trash"] = tamagocha1.trash
tamplate["tired"] = tamagocha1.tired
tamplate["time"] = str(datetime.today().replace(microsecond=0))
with open("data.json", "w") as f:
    json.dump(tamplate, f)