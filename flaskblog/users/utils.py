import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics' , picture_fn)
	# Shrink the image to thumbnail
	output_size = (125,125)
	icon_image = Image.open(form_picture)
	icon_image.thumbnail(output_size)
	icon_image.save(picture_path)
	return picture_fn

def remove_picture():
	old_picture_path = os.path.join(current_app.root_path, 'static/profile_pics' , current_user.image_file)
	if os.path.isfile(old_picture_path) and current_user.image_file != 'default.jpg':
		os.remove(old_picture_path)

def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request',
				 sender='noreply@demo.com',
				 recipients=[user.email])
	msg.body = f'''To reset your password, enter the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you didnt not make the Request Ignor it'''
	mail.send(msg)