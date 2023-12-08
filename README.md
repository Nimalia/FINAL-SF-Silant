Привет, меня зовут **Алина** 👋

Завершаю учебу на курсе ![logo_sf](imgforreadme/logo_sf.png) 

**Fullstack разработчик на Python**
 

Блок **ДИПЛОМНАЯ РАБОТА**
# ![logo_silant](static/icons/favicon.ico) Силант



[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=F7091B&random=false&width=435&lines=%D0%94%D0%B8%D0%BF%D0%BB%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0.+%D0%A1%D0%B8%D0%BB%D0%B0%D0%BD%D1%82.)](https://git.io/typing-svg)
___



**Задание:**

![task](imgforreadme/task1.png)
![task](imgforreadme/task2.png)
![task](imgforreadme/task3.png)
![task](imgforreadme/task4.png)

**Проект:**

![drf logo](https://s3.amazonaws.com/media-p.slid.es/uploads/708405/images/4005243/django_rest_500x500.png)



### **Быстрый старт:**
**Для запуска проекта необходимо:**

1. Клонировать репозиторий 

    ➡️  [Github repository](https://github.com/Nimalia/FINAL-SF-Silant.git)

2. Установить виртуальное окружение
    ```bash 
    python3 -m venv venv
    ```

    ```bash 
    source ./venv/bin/activate
    ```
3. Установить `requirements.txt`
    ```bash 
    pip install -r requirements.txt
    ```
4. Переходим в директорию (если необходимо):
    ```bash 
    cd *имя директории* 
    ```
5. Создать пользователя
    ```bash 
    python3 manage.py createsuperuser
    ```
6. Запустить сервер
    ```bash 
    python3 manage.py runserver
    ```

7. Запускаем [Силант](127.0.0.1:8000/search/) 
 
    ⚠️ порт 8000
 
### **Роли:**

Клиент: Trudnikov 

Пароль: Client2023
___

Менеджер: manager1

Пароль: manager
___

Сервисная компания: FNS

Пароль: Client2023
____

### **Структура приложения:**

1. Вход неавторизованного пользователя:
![doc_pic](imgforreadme/unauthorized.png)

Пользователь видит только список техники
и может совершить поиск:
![doc_pic](imgforreadme/search.png)

2. Зарегистрировать пользователя может только Администратор. 
Администратору доступен весь функционал приложения: 
![doc_pic](imgforreadme/admin.png)

3. Сделаны отдельные группы с правами:
- группа для менеджеров Силант, которым выданы определенные права
![doc_pic](imgforreadme/manager.png)  

- группа клиентов Силант, которым выданы определенные права
![doc_pic](imgforreadme/client.png)  

- группа для сервисных компаний Силант, которым выданы определенные права
![doc_pic](imgforreadme/servorg.png)  

4. Детализация по каждой технике:
![doc_pic](imgforreadme/detail.png) 

5. Создание Новой техники/Нового тех.обслуживания/Новой рекламации (в зависимости от роли):
![doc_pic](imgforreadme/newdata.png)

6. Страница авторизации:
![doc_pic](imgforreadme/login.png)  

7. Страница выход:
![doc_pic](imgforreadme/logout.png) 

8. Модальные окна:
![doc_pic](imgforreadme/modal.png) 

9. Адаптивность верстки:
![doc_pic](imgforreadme/adapt.png) 

![doc_pic](imgforreadme/adaptend.png) 

**🛠️Технические нюансы🔩**

1. Импорт данных из Exel в SQL производиться с помощью 
```bash
Django import/expot
```
так как поля в моделях 
```bash
= ForeignKey
```
то необходимо использовать [widget](https://django-import-export.readthedocs.io/en/latest/advanced_usage.html#importing-model-relations)


2. Для иконок [онлайн конвертор](https://convertio.co/ru/png-svg/)

3. Сортировка через ```ordering``` во ```views.py```

4. Пагинация через ```views.py``` + ```шаблон html``` + ```css```
![doc_pic](imgforreadme/pagination.png)



----
```` Спасибо за уделенное время! 🙏 ````

___

![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Nimalia&theme=solarized_dark)


![](https://komarev.com/ghpvc/?username=Nimalia)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=anuraghazra)](https://github.com/anuraghazra/github-readme-stats)