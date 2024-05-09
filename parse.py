from fastapi import FastAPI, Request

api = FastAPI()

@api.post("/")
async def notificacionesUser(request : Request):
    data = await request.json()
    print(data)
    return {}