from flask import Flask, request, render_template, session, redirect, url_for
import hashlib
import json
import time

from model import GLMModel, OpenAIModel
from utils import ArgumentParser, ConfigLoader, LOG
from translator import TXTTranslator, PDFTranslator

app = Flask(__name__)

#命令行获取配置
# argument_parser = ArgumentParser()
# args = argument_parser.parse_arguments()
# config_loader = ConfigLoader(args.config)
# config = config_loader.load_config()
#
# model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
# api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']

#config.yaml获取配置
config_loader = ConfigLoader("config.yaml")
config = config_loader.load_config()

model_name = config['OpenAIModel']['model']
api_key = config['OpenAIModel']['api_key']
model = OpenAIModel(model=model_name, api_key=api_key)

@app.route('/txttranslator',  methods=['POST'])
def txttranslator():
    data = request.json
    text = data["text"]
    target_language = data["target_language"]

    translator = TXTTranslator(model)

    return translator.translate_txt(text, target_language)

@app.route('/pdftranslator',  methods=['POST'])
def pdftranslator():
    data = request.json
    target_language = data["target_language"]

    pdf_file_path = config['common']['book']
    file_format = config['common']['file_format']

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)

    return translator.translate_pdf_txt(pdf_file_path, file_format, target_language)

@app.route('/translator')
def translator():
    return render_template("translator.html")

#app.secret_key = 'any random string'




