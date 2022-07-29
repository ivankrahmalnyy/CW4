from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режисеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тарантино'),
})

movie: Model = api.model('Фильмы', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Чтиво'),
    'description': fields.String(required=True, max_length=100, example='Владелец ранчо пытается сохранить землю ....'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=UKei_d0cbP4'),
    'year': fields.Integer(required=True, example=2018),
    'rating': fields.Float(required=True, example=8.6),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example=1),
    'password': fields.String(required=True, max_length=100, example='test'),
    'name': fields.String(required=True, max_length=100, example='John'),
    'surname': fields.String(required=True, max_length=100, example='Taylor'),
    'genre': fields.Nested(genre),
})

