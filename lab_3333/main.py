__author__ = 'Work'
import BaseClient
import getUser
import getFriends
import datetime


def create_args(args):
    return "&".join("%s=%s" % (key, value) for key,value in args.items())

def check_bdatt(obj):#получаем на вход словарь
    return ("bdate" in obj.keys()) and (len(obj["bdate"].split('.')) == 3)

if __name__ == "__main__":
    name=input("Введите ID пользователя ")
    try:
        vk_name=getUser.GetUser('users.get?user_ids=' + name)#создаем объект класса getUser через конструктор с параметром method = "получить пользователей(id=id пользователя)"
        name=vk_name.get_dict_data()#получаем список пользователей в виде словаря
        names=name['response'][0]#так как пользователь с одним ID один единственный, а поле response представляет собой массив,выбираем первый элемент массива
        if (name is None) or ('uid' not in names):
            raise Exception
    except Exception:
        print ('Пользователь с данным ID не найден')
        exit()

     #Выведем имя и фамилию пользователя

    print('Имя пользователя VK: ', names['first_name'] ,
          ' ' , names['last_name'])

    now=datetime.date.today()

    old_arr = {}#словарь для количества #

    args = {
        "user_id":names['uid'],
        "fields":"bdate",
        "v":"5.57"
    }
    try:
        vk=getFriends.GetFriends('friends.get?' + create_args(args))#создаем объект класса getUser через конструктор с параметром method = "получить список друзей пользователя(
        # (преобразованный к параметру get запроса словарь, содержащий id пользователя,поля,которые необходимо вернуть, и версию вк)"
        friends = vk.get_dict_data()["response"]["items"]#получаем массив словарей, каждый из которых содержит возраст друга
    except Exception:
        print('Не удалось получить друзей пользователя')
        exit()

    for x in friends:
        if check_bdatt(x):
            bdate_arr = x["bdate"].split('.')
            bdate = datetime.date(int(bdate_arr[2]),int(bdate_arr[1]),int(bdate_arr[0]))
        diff = int((now - bdate).days/365)
        if diff not in old_arr.keys():
            old_arr[diff]=0
        old_arr[diff]=old_arr[diff]+1

    new_arr=[]

    for key in sorted(old_arr):
        print(str(key) + ' ' + '#'.join('' for i in range(old_arr[key] + 1)))
        new_arr.append(key)

import matplotlib.pyplot as plt

plt.hist(
    new_arr,
    25
)

plt.show()
