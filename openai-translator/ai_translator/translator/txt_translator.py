from typing import Optional
from model import Model
from translator.pdf_parser import PDFParser
from translator.writer import Writer
from utils import LOG

class TXTTranslator:
    def __init__(self, model: Model):
        self.model = model
        self.pdf_parser = PDFParser()
        self.writer = Writer()

    def translate_txt(self, txt: str, target_language: str = '中文'):
        prompt = self.model.make_text_prompt(txt, target_language)
        LOG.debug(prompt)
        translation, status = self.model.make_request(prompt)
        LOG.info(translation)

        return translation
