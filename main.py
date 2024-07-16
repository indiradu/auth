from fastapi import FastAPI, Body, Depends
from app.model import UserSchema, UserloginSchema, PostSchema
from app.auth.handler import signJWT
from app.auth.bearer import Bearer

app= FastAPI()
  
users=[]
posts=[
    {
        "title":"cats",
        "description":'all bfeoojl'
    }
]

@app.get('/')
def root():
    return{'message':"Hello world"}

def verify_user(data: UserloginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.get("/posts")
def get_post():
    return posts



@app.post("/posts", dependencies=[Depends(Bearer())])
def create_post(post: PostSchema = Body(...)):
    posts.append(post)
    return post

@app.get("/user")
def get_user():
    return users
         

@app.post('/user/sign_up')
def create_user(user: UserSchema=Body(...)):
    users.append(user)
    return signJWT(user.email)

@app.post('/user/signin')
def login_user(user:UserloginSchema=Body(...)):
    if verify_user(user):
        return signJWT(user.email)
    return{'error':'Invalid credentials'}



