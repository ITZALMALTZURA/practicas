#programa que mande una imagen
from erina import Handler
class EjenploImagen(Handler):
	def handler(self):
 	 	if salf.type =="text":
			if self.raw_imput.eq("envia la imagen"):
				img="./_data/EjemploImagen/ejemplo.jpg"
				self.response.image("imagen de ejemplo,img")
				return TRUE
			#imagen'1''2''3'
			if self.command.eq("imagen"):
				n = self.args.get(0)
				if not n:
					self.response.text("necesita un paramet$")
					return True
			   if not (n == "1" or  n =="2"):
                                        self.response.text("solo tengo una imagen 1$")
					return True

				img = "./_data/EjemploImagen/ejemplo.jpg"%n
				self.response.image(n, img)
					return True






INIT.PY

from ._image_filter import ImageFilter
from ._basic_talk import BasicTalk 
from ._random_meme import RandomMeme
from ._notify_
