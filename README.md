# ArchTour

#Основная настройка
Для начала нужно получить доступ на сервере
    для этого нужно купить VDS/VPS, тут процесс зависит от вашего выбора
    но в целом, нужно следовать инструкциям на экране

мы будем показывать процесс установки на ubuntu-server
при покупке VDS/VPS у вас уже будет установленна ОС(операционная система), после чего нам нужно обновить локальные репозитории коммандой
```sudo apt update```
```sudo apt upgrade -y```

так как запуск приложений от root, не является хорошей практикой, нам нужно создавить нового пользователя

#Создание нового пользователя
```sudo useradd newuser```
**вместо newuser подставьте желаемое имя и введите пароль**

после чего следуйте инструкциям, не обязательно добавлять какую либо информацию, кроме пароля
**НО ОБЯЗАТЕЛЬНО подтвердить добавление**
когда высветится строчка о корректности данных, следует ввести
```y```

Далее нужно будет создать папку в которой будет распологаться проект, для начала мы перейдём в нужную нам директорию коммандой
```cd /```
```cd /home/newuser```
**замените newuser на указанное вами имя пользователя**
после чего вам нужно будет склонировать данный репозиторий на сервер, это можно сделать коммандой
```git clone https://github.com/x1roko/ArchTour.git```

после вводим
```sudo apt install apt-transport-https ca-certificates curl software-properties-common```

```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - ```

```sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"```

```sudo apt-update```

```sudo apt-get install docker-ce```

```sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose```

```sudo chmod +x /usr/local/bin/docker-compose```

после чего нужно выйти с текущего пользователя и зайти на нового

```reboot```
**Данная команда перезагрузит компьютер**
после чего указать данные логина для пароля
перейти в папку
```cd /home/newuser/ArchTour```
**Замените newuser на Логин, что указали**

```sudo apt install screen```

```screen```

```docker-compose up```

После конца нажмите запомните Аддрес, что высветится
нажмите
```Ctrl + A```
```D```

на своём устройстве введите в строке браузера
http://ipserver:8000/generate-wordcloud

**Замените ipserver на домен, или ip аддрес своего сервера**
#В случае если вы не знаете, ipсервера, введите комманду
```ip a```


