from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class TopicForm(FlaskForm):
    wiki_topic = StringField(
        'Enter Wikipedia topic',
        validators=[
            InputRequired(message="Please submit a topic"),
        ])
    # remember_me = BooleanField('Remember Me')
    submit = SubmitField('Search Topic')


# class URLForm(FlaskForm):
#     submit_url = SubmitField("Submit Link")
class LinkSearchForm(FlaskForm):
    linksearch = StringField(
        "Search links for",
        validators=[
            InputRequired(message="Please submit a topic"),
        ])
    submit_linksearch = SubmitField("Submit query")
