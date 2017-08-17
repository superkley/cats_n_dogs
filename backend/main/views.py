import base64
from io import BytesIO
from flask import Blueprint, jsonify, render_template, request

from backend.main.ai import predict_breed

cats_n_dogs = Blueprint('cats_n_dogs', __name__, static_folder='../static')


@cats_n_dogs.route('/cats_n_dogs')
def main():
    return render_template('index.html')


@cats_n_dogs.route('/')
def index():
    return render_template('index.html')


@cats_n_dogs.route('/process_img', methods=['POST'])
def process_img():
    data = request.get_json()
    img_src = data['imgSrc']
    b64str = img_src.partition(',')[2]
    binary_jpeg = base64.b64decode(b64str)
    img_file = BytesIO(binary_jpeg)
    return jsonify({'breed': predict_breed(img_file)})
