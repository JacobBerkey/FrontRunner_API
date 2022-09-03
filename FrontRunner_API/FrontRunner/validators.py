from django.core.exceptions import ValidationError

def validate_domainonly_email(value):
    if not "FrontRunner.com"  in value:
        raise ValidationError("Email has to end with FrontRunner.com")
    return value