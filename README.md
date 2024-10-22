1. Клонируйте репозиторий

Если вы еще не клонировали репозиторий, сделайте это:


```git clone <ваш репозиторий>
cd <папка вашего репозитория>
```
2. Создайте файл .env


    Создайте файл .env в корне проекта со следующим содержимым:

```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB_USER=user_db
POSTGRES_DB_ORDER=order_db
```
3. Соберите и запустите контейнеры

* В корне проекта выполните команду:

```
docker-compose up --build
```
    
    Docker Compose соберет образы и запустит все сервисы, указанные в docker-compose.yml.

* Примечания:

    Убедитесь, что порты 5432 и 5433 на вашей машине свободны перед запуском контейнеров с базами данных.

Если вам нужно пересобрать образы без использования кэша, используйте команду:

```
docker-compose build --no-cache
```
* Остановка контейнеров

Для остановки и удаления всех запущенных контейнеров выполните команду:

```
docker-compose down
```
* Проверка работы сервисов.
Ваши микросервисы будут доступны на следующих портах:
```
user-service: localhost:50051
order-service: localhost:50052
```
**Дополнительные команды.**

* Чтобы следить за логами всех сервисов в режиме реального времени:


```
docker-compose logs -f
```

* Для перезапуска сервисов после изменений в коде:

```
docker-compose up --build
```
