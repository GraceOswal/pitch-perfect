import os

from dotenv import load_dotenv as ld

ld()

class Config:
    debug = True
    SECRET_KEY = os.environ.get(SECR)
