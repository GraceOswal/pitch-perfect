from flask import Blueprint

main = Blueprint('main', __name__)
from . views import *

from app import views
from app import error
