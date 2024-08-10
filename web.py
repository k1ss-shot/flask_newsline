from flask import request, render_template, Blueprint, url_for, flash
from flask_cors import CORS
from helpers import get_index_page_data, get_post_data
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
        return render_template('index.html', data=data)

@web_page.route('/post/<int:post_id>', endpoint='post_detail')
def post_detail(post_id):
    data = get_post_data(post_id=post_id)
    print(data)
    return render_template('post.html', data=data)

