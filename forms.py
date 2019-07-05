from flask_wtf import FlaskForm
from wtforms import TextField,  SubmitField
from wtforms import validators

class ContactForm(FlaskForm):
   subscriptionid = TextField("Subscription ID",[validators.Required("Please enter your Azure Subscription ID.")])
   clientid = TextField("Client ID",[validators.Required("Please enter your Azure Client ID.")])
   secret = TextField("App Secret",[validators.Required("Please enter your Azure app secret key.")])
   tenant = TextField("Tenant ID",[validators.Required("Please enter your Azure Tenant ID.")])
   submit = SubmitField("Login")
