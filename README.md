# films_api
## API на Flask
### Это миниверсия imdb api.
#### Реализованные эндпойнты:
/films  - получить все фильмы,
/films/uuid   - получить фильм по uuid,
/actors       - получить всех актеров,
/actors/id    - получить актера по id,
/aggregations - получить общие сведения о фильмах: максимальная, средняя оценка, общее количество фильмов.
#### Доступные методы: GET, POST, PUT, DELETE
#### Реализована аутентификация с помощью библиотеки pyJWT.
