from fastapi import FastAPI
from routers.text_generator import routes_text_generator


app = FastAPI()
app.include_router(routes_text_generator.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
