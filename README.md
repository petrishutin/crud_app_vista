Простое CRUD приложение.

Основная функция создавать, просматривать, редактировать и удалять заметки. Приложение написано на flask
При запуске приложения будет автоматически добавлены сгенерированные записи.

Для работы неоходимо:
    - Linux дистрибутив, с админскими правами (Задание выполнялось на Ubuntu 20.04LTS)
    - системный интерпретатор python3 (Выполнялось с Python3.8)
    - локальный сервер MySql или MariaDB (Выполнялость на MariaDB)

База данных:
1. Под админскими правами надо создать базу данных и юзера с правами на эту базу:`CREATE DATABASE notes`
2. Создать юзера:`CREATE USER 'myuser'@'%' IDENTIFIED BY '123456';`
3. Пердоставить права:`GRANT CREATE,SELECT,UPDATE,INSERT,DELETE ON notes.* TO 'myuser'@'%';`
   (Настройки пользователя и базы данных можно поменять в файле app/config.py или передать в качестве переменных окружения)

Для развертывания приложения в качестве сервиса:
1. Создать пользователя `sudo adduser myuser` и повысить пользователя до суперюзер `sudo adduser myuser sudo` 
2. Зайти в систему под созданным юзером
3. Создать нужную директорию и скопировать папку с приложение `mkdir -p /home/myuser/crud_app_vista/ && cp -r app /home/myuser/crud_app_vista/` Или просто склонировать репозиторий находясь в домашней директории пользователя `https://github.com/petrishutin/crud_app_vista.git`
4. Создать виртуальное окружение `python3 -m venv /home/myuser/crud_app/app/venv` 
5. Активировать виртуальное окружени `source /home/myuser/crud_app/app/venv/bin/activate`
6. Установать зависмости (с работающим витуальным окружением) `pip install -r /home/myuser/crud_app/app/requirements.txt`
7. Скоприровать файл crud_app.service в системную директорию (Необходимо обладать правати администратора) `sudo cp crud_app.service /etc/systemd/system/crud_app.service`
8. Запустить сервис `sudo systemctl start crud_app.service` и активировать  `sudo systemctl enable crud_app.service`
9. Перезапустить сервисы `sudo systemctl daemon-reload`

Приложение будет доступно по адресу http://localhost:5000/