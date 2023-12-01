from web import flaskserver

def flaskTest():
    flaskserver.app.run(port=2020, host="127.0.0.1", debug=True)

if __name__ == "__main__":
    # argument_parser = ArgumentParser()
    # args = argument_parser.parse_arguments()
    # config_loader = ConfigLoader(args.config)
    #
    # config = config_loader.load_config()
    #
    # model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
    # api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
    # target_language = args.target_language if args.target_language else "中文"
    #
    # model = OpenAIModel(model=model_name, api_key=api_key)
    #
    # pdf_file_path = args.book if args.book else config['common']['book']
    # file_format = args.file_format if args.file_format else config['common']['file_format']
    #
    # # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    # translator = PDFTranslator(model)
    # translator.translate_pdf(pdf_file_path, file_format, target_language)

    flaskTest()
