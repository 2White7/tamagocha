import json


with open("data.json","r") as f:
      tamplate=json.load(f)

print("Добро пожаловать домой! Что вы хотите сделать, хозяин?\n" + "Посмотреть статус - 1\n"
       + "Покормить - 2\n" + "Отправить в кровать - 3\n"
       + "Навести порядки и покупать - 4\n" + "Отправить на прогулку - 5\n" + "Отправить в БДСМ клуб - 6\n")


def tamagocha():

      do=int(input())

      if do == 1:
            print("Статус\n" + str(tamplate["name"]) + ("\nГолод = " + str(tamplate["eda"])) + ("\nУсталость = " + str(tamplate["tired"])) +
            ("\nУровень загрязненности комнаты = " + str(tamplate["trash"])) + ("\nПотебность в общении = "
            + str(tamplate["socialka"])) + ("\nПотребность в страданиях = " + str(tamplate["bdsm"])))

      elif do == 2:
            tamplate["eda"] = 100
            print("Спасибо было вкусно!\n" + "Голод = " + str(tamplate["eda"]))

      elif do == 3:
            tamplate["tired"] = 100
            print("Я выспалась!\n" + "Усталость = " + str(tamplate["tired"]))

      elif do == 4:
            tamplate["trash"] = 100
            print("Какая чистота!\n" + "Уровень загрязнения = " + str(tamplate["trash"]))

      elif do == 5:
            tamplate["socialka"] = 100
            print("Я так хорошо погуляла!\n" + "Потребность в общении = " + str(tamplate["socialka"]))

      elif do == 6:
            tamplate["bdsm"] = 100
            print("Это было великолепно!\n" + "Потребность в страданиях = " + str(tamplate["bdsm"]))

      elif do == 7:
            return do

      else:
            print("Я не понимаю, повторите еще раз.")

      if tamplate["eda"] == 0:
            print("Ваш персонаж умер от голода")
      elif tamplate["trash"] == 0:
            print("Ваш персонаж умер в грязи от инфекций")
      elif tamplate["bdsm"] == 0:
            print("Ваш персонаж совершил суицид")
      elif tamplate["tired"] == 0:
            print("Ваш персонаж устал до смерти")
      elif tamplate["socialka"] == 0:
            print("Ваш персонаж умер от одиночества")
      return do

end=0
while end!=7:
      end=tamagocha()


with open("data.json","w") as f:
      json.dump(tamplate,f)

