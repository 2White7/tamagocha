import json
import datetime


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

now = datetime.datetime.today()

time = tamplate["time"]
tamplate["time"] = str(now)

time1 = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
c = str(now - time1)
diff = datetime.datetime.strptime(c, "%H:%M:%S.%f")
if diff.hour > 0:
    tamagocha1.eda = tamagocha1.eda - (10 * diff.hour)
    tamagocha1.bdsm = tamagocha1.bdsm - (10 * diff.hour)
    tamagocha1.trash = tamagocha1.trash - (10 * diff.hour)
    tamagocha1.tired = tamagocha1.tired - (10 * diff.hour)
    tamagocha1.socialka = tamagocha1.socialka - (10 * diff.hour)

end=0
while end!=7:
      end=tamagocha1.interface()

tamplate["eda"] = tamagocha1.eda
tamplate["socialka"] = tamagocha1.socialka
tamplate["bdsm"] = tamagocha1.bdsm
tamplate["trash"] = tamagocha1.trash
tamplate["tired"] = tamagocha1.tired

with open("data.json", "w") as f:
    json.dump(tamplate, f)