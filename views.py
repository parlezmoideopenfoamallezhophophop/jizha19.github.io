from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    images = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg',  'image6.jpg']
    return render_template("home.html",images=images)
