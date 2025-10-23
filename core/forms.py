from django import forms
from .models import PhotoPatient, PDFPatient
from django.contrib.auth.forms import UserCreationForm

class MedicoRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'username' in self.fields:
            self.fields['username'].widget.attrs.update({'placeholder': 'Nome de Usuário Único'})
        if 'email' in self.fields:
            self.fields['email'].widget.attrs.update({'placeholder': 'Seu Email (Opcional)'})


class PhotoPatientForm(forms.ModelForm):
    class Meta:
        model = PhotoPatient
        fields = ['foto', 'descricao']

        widgets = {
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breve descrição da foto'}),
        }
        
        labels = {
            'foto': 'Arquivo de imagem',
            'descricao': 'Descrição',
        }

class PDFPatientForm(forms.ModelForm):
    class Meta:
        model = PDFPatient
        fields = ['pdf_file', 'nome_documento']
        
        widgets = {
            'pdf_file': forms.FileInput(attrs={'class': 'form-control'}),
            'nome_documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Documento (Ex: Raio-X Toráxico)'}),
        }
        labels = {
            'pdf_file': 'Arquivo PDF',
            'nome_documento': 'Título do Documento',
        }

