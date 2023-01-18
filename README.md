# SkyPro test work

  ### ➜ Task 1
    
  ```
  Привет!
  Директория с templates находиться в корневой папке проекта
  тогда как для обеспечения большей модульности её лучше
  помещать в папку с конкретным приложением, которое 
  использует необходимые templates
  ```

  ```
  Директория staticfiles имеет стандартное название static.
  Лучше придерживаться стандартного нейминга )
  ```

  ```python
  Базовый маршрутизатор содержит много лишних роутов, которые можно было бы 
  вынести в отдельный маршрутизатор приложения.
  И заинклидтть через include('vacancies.urls')

  urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacancies/', include('vacancies.urls'), name='vacancies'),
  ]

  За кастомный обработчик 404 \ 500 - ошибок отдельный респект.
  ```

  ```python
  В settings.py -> INSTALLED_APPS желательно указывать полный
  путь до конфига приложения

  INSTALLED_APPS = [
    'vacancies.apps.VacanciesConfig'
  ]
  ```

  ```python

  Так же при создании модели можно не указывать primary_key
  Так как orm автоматически создаст это поле.

  class SomeModel(models.Model):
    id = models.IntegerField(primary_key=True)
  ```

  ```js
  В целом проект выполнен хорошо, мне нравится подход
  декомпозиции и следование принципу DRY.
  Оценка 5 из 6.
  ```

  ### ➜ Task 2

  1. `git clone`
  2. `poetry install`
  3. `poetry shell`
  5. `cd myapi`
  5. `python manager.py runserver`

  
