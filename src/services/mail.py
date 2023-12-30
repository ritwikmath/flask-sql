from flask import current_app
from flask_mail import Mail, Message
import importlib
import os

class MailService:
    def __init__(self, recipient, subject) -> None:
        self.mail = Mail(current_app)
        self.msg = Message(sender='ritwikmath@gmail.com',
                           recipients=[recipient],
                           subject=subject)
    
    def format_mail(self, template_name, varables):
        root_path = current_app.instance_path.rsplit('/', maxsplit=1)[0]
        path = os.path.join(root_path, 'src', 'email_templates', f"{template_name}.html")
        with open(path, "r", encoding='utf-8') as template:
            template_content = template.read()
            for v in varables:
                template_content = template_content.replace(v[0], v[1])
            self.msg.html = template_content
        return self
    
    def send_mail(self):
        self.mail.send(self.msg)
