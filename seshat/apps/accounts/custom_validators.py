# custom_validators.py (or validators.py within your app)

from django.core.exceptions import ValidationError
import re

def validate_email_with_dots(value):
    """
    Custom validator to reject email addresses with more than four dots in their domain part.
    """
    # Split the email address into local and domain parts
    local_part, domain_part = value.split('@')

    # Check if the domain part has more than four dots
    if local_part.count('.') > 4:
        raise ValidationError("Email address contains too many dots in the domain part.")

    # You can add more checks if needed

