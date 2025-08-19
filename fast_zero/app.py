from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import MessageSchema, UserPublicSchema, UserSchema

app = FastAPI()

users = []


@app.get('/', status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {'message': 'Hello World!'}


@app.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserSchema):
    print(user)
    return {"name": user.name, "email":user.email}
