from pydantic import BaseModel
from fastapi import APIRouter, Request, Response
from fastapi.encoders import jsonable_encoder
from .render_image import GenerateImage, GetImage

router = APIRouter()

#Note for Adam; I dont know if it is a good practice, but I think encapsulate the response and the request coulb be worth it.
class RequestPostText(BaseModel):
    user_id : int
    text : str

class ResponsePostText(BaseModel):
    user_id: int 
    image_id: int



#Note for Adam, In the future we have to implement a Oauth method and/or cookies for the user identification
@router.post("/text")
async def text_generator_POST(request: RequestPostText) ->ResponsePostText:
    #Vamos a tener que hacer un error handling guapo, me da pereza ponerme ahora asi que lo cheeke Diosito
    response = ResponsePostText
    response.user_id = request.user_id

    pipeline = GenerateImage(user_id = request.user_id, text= request.text)
    pipeline.generate_image()
    response.image_id = pipeline.image_id()
    return response


@router.get("/image/{id}")
async def text_generator_GET(id : int, request: Request) :

    pipeline = GetImage(id)
    return Response(content=pipeline.image(), media_type="image/png")




    