from flask import request, render_template, Blueprint, url_for, flash
from flask_cors import CORS
from helpers import get_index_page_data
import os

from models import (
    db,
    Title,
    Description,
    Photo,
    Post,
    PublishTime,
)
web_page = Blueprint('web', __name__, template_folder='templates')

@web_page.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        data  = get_index_page_data()
        print(data)
        return render_template(template_name_or_list='index.html', data=data)
    
@web_page.route('/post', methods={'GET'})
def post():
    if request.method == 'GET':
        data = get_post_data