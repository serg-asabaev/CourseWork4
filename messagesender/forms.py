from django.forms import ModelForm
from django.core.exceptions import ValidationError
from datetime import datetime

from .models import Sending


class SendingForm(ModelForm):

    class Meta:
        model = Sending
        fields = ('start_time', 'end_time', 'message', 'recipients')

    def __init__(self, *args, **kwargs):
        super(SendingForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите дату и время начала рассылки'})
        self.fields['end_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите дату и время окончания рассылки'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберите сообщение рассылки'})
        self.fields['recipients'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберите получателей рассылки'})

    def clean(self):
        cleaned_data = super().clean()

        start_time = cleaned_data.get('start_time')
        start_time2 = datetime(start_time.year, start_time.month, start_time.day, start_time.hour, start_time.minute,
                               start_time.second)
        end_time = cleaned_data.get('end_time')
        end_time2 = datetime(end_time.year, end_time.month, end_time.day, end_time.hour, end_time.minute,
                                                        end_time.second)

        now_time = datetime.now()

        if start_time2 < now_time:
            raise ValidationError('Дата начала рассылки не может быть в прошлом!')

        if end_time2 < start_time2:
            raise ValidationError('Дата окончания рассылки должна быть после даты начала рассылки!')

class SendingSendForm:
    class Meta:
        model = Sending

