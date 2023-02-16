from django.db import models

class MockCloudinaryField(models.Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        return value

    def get_prep_value(self, value):
        return value

    def formfield(self, **kwargs):
        from django.forms.fields import CharField
        defaults = {'form_class': CharField}
        defaults.update(kwargs)
        return super().formfield(**defaults)