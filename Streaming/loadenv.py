import os, dotenv

if os.path.exists(os.path.abspath(os.path.join(__file__, "..", ".env"))):
    dotenv.load_dotenv()
    os.system(os.environ['MAKEMIGRATIONS'])
    os.system(os.environ['MIGRATE'])