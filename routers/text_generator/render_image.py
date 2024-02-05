#Here should be the part to connect with the models

from PIL import Image


class GenerateImage():
     #kwargs will be hyperparameters in the future
     def __init__(self, text: str, user_id: int,  **kwargs) -> None:
          self.__text = text
          self.__user_id = user_id
          self.__image_id = None
          self.__image = None

     def image_id(self) -> int:
          return self.__image_id
     
          #In the future, this function has to be connected with db and assign an image id
     def __assign_image_id(self) -> int:
          return 42
     
     def generate_image(self) -> None:
          self.__image_id = self.__assign_image_id()
          self.__render_image()
          return

     #this function is expected to have  conection with the models
     def __render_image(self) ->None:
          pass


class GetImage():
     def __init__(self, image_id: int, **kwargs) ->None:
          self.__image_id = image_id

     def image(self) -> bytes:
          img  = Image.open('routers/text_generator/test/gibli_image.png')
          return img.tobytes("xbm", "rgb")