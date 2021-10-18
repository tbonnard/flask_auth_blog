from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField
from wtforms.fields.html5 import EmailField
import email_validator


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


##WTForm
class CreateUserForm(FlaskForm):
    name = StringField("Your name", validators=[DataRequired()])
    email = EmailField('Enter your email', validators=[DataRequired(), Email()])
    password = PasswordField('Your password', validators=[DataRequired()])
    submit = SubmitField('Sign me up!')


class LoginUserForm(FlaskForm):
    email = EmailField('Enter your email', validators=[DataRequired(), Email()])
    password = PasswordField('Your password', validators=[DataRequired()])
    submit = SubmitField('Login!')


class CommentForm(FlaskForm):
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField('Add comment')
