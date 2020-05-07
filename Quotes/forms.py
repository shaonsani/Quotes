from django import forms
from .models import Quotes

class QuotesForm(forms.ModelForm):
    quotes =forms.CharField( widget=forms.Textarea )
    class Meta:
        model= Quotes
        fields = ('__all__')

        labels={
            'q_code':'Q.Code',
            'author_name':'Author',
            'catagory':'Type',
        }

    def __init__(self,*arg,**kwargs):
        super(QuotesForm,self).__init__(*arg,**kwargs)
        self.fields['catagory'].empty_label='Select'
