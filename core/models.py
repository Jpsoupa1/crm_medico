from django.db import models

# Modelo User padrao do DJango para vincular paciente -> Médico

from django.contrib.auth.models import User
from django.urls import reverse


class Patient(models.Model):

    medico = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pacientes',
        verbose_name='Médico Responsável'
    )

    nome_completo = models.CharField(max_length=200, verbose_name='Nome Completo')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)


    historico_medico = models.TextField(verbose_name='Histórico Médico', blank=True, null=True)
    alergias = models.TextField(verbose_name='Alergias', blank=True, null=True)

    data_registro = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        # Adicionar uma restricao para garantir que o medico possa listar/filtrar
        ordering = ['nome_completo']

    def __str__(self):
        """Representacao em string do objeto Paciente."""
        return self.nome_completo
    
    def get_absolute_url(self):
        """
        Define o URL padrao para redirecionar apos a criacao de um paciente.
        Vamos usar a rota de detalhes do paciente.
        """
        return reverse('detalhe_paciente', kwargs={'pk': self.pk})

class PhotoPatient(models.Model):

    paciente = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='fotos',
        verbose_name='paciente'
    )

    foto = models.ImageField(upload_to='pacientes/fotos/', verbose_name='Foto')
    descricao = models.CharField(max_length=255, blank=True, verbose_name='Descrição')
    data_upload = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Foto do Paciente'
        verbose_name_plural = 'Fotos do Paciente'
    
    def __str__(self):

        return f"Foto de  {self.paciente.nome_completo} ({self.pk})"
    

class PDFPatient(models.Model):
    paciente = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='pdfs',
        verbose_name='Paciente'
    )

    pdf_file = models.FileField(upload_to='pacientes/pdfs/', verbose_name='Arquivo PDF')
    nome_documento = models.CharField(max_length=255, verbose_name='Nome do Documento')
    data_upload = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Documento PDF'
        verbose_name_plural = "Documentos PDFs"
    
    def __str__(self):
        
        return f"PDF: {self.nome_documento} para {self.paciente.nome_completo}"
    