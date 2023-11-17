from dataclasses import fields
from django.forms  import EmailInput, ModelForm,DateInput, NumberInput, Select, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper

from .models import Dosen, Mahasiswa, Mitra, Pimpinan, Prodi, Role, UnitMBKM, Mentor, Transkip, MahasiswaInbound

class DateInput(DateInput):
    input_type='date'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class GantiPasswordForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['role']

class CreatePimpinanForm(ModelForm):
    class Meta:
        model =  Pimpinan
        fields = '__all__'
        exclude  = ['user']

class EditPimpinanForm(ModelForm):
    class Meta:
        model =  Pimpinan
        fields = '__all__'
        exclude  = ['user','username']

class CreateUnitForm(ModelForm):
    class Meta:
        model = UnitMBKM
        fields = '__all__'
        exclude  = ['user']

class CreateProdiForm(ModelForm):
    class Meta:
        model = Prodi
        fields = '__all__'
        exclude = ['user']

class EditProdiForm(ModelForm):
    class Meta:
        model = Prodi
        fields = ['unit','nama_prodi','jenjang','koordinator_prodi','nip_koordinator_prodi','email','no_hp'] 
        widgets = {
            'nama_prodi': TextInput(attrs={'class':'form-control form-select input-sm', 'data-control':"select2", 'readonly':True, 'required': True}),
            'email': EmailInput(attrs={'class':'form-control input-sm', 'required': False}),
            'no_hp': NumberInput(attrs={'class':'form-control input-sm', 'required': False}),
        }       
class CreateMahasiswaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateMahasiswaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['program_studi'].empty_label = 'Pilih Program Studi'
    class Meta:
        model = Mahasiswa
        fields = ['nim','tgl_lahir','email','program_studi','no_hp']
        exclude = ['user']
        widgets = {
            'nim': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'Nim', 'required': True}),
            'tgl_lahir': DateInput(attrs={'class':'form-control input-sm mb-3'}),
            'email': EmailInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'email@gmail.com','required': True}),
            'no_hp': NumberInput(attrs={'class':'form-control input-sm', 'required': False}),
            'program_studi': Select(attrs={'class':'form-control form-select input-sm mb-3', 'data-control':"select2"})
        }

class EditMahasiswaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditMahasiswaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['program_studi'].empty_label = 'Pilih Program Studi'
    class Meta:
        model = Mahasiswa
        fields = ['nim','email','program_studi','no_hp','total_sks','ipk']
        exclude = ['user']
        widgets = {
            'nim': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'Nim', 'required': True}),
            'email': EmailInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'email@gmail.com','required': True}),
            'no_hp': NumberInput(attrs={'class':'form-control input-sm', 'required': False}),
            'program_studi': Select(attrs={'class':'form-control form-select input-sm mb-3', 'data-control':"select2"}),
            'total_sks': NumberInput(attrs={'class':'form-control input-sm', 'required': True}),
            'ipk': NumberInput(attrs={'class':'form-control input-sm', 'required': True, 'step':'0.01'}),
        }


class CreateMitraForm(ModelForm):
    class Meta:
        model = Mitra
        fields = 'nama_mitra','nama','jabatan','email','jk','no_hp'
        exclude = ['user']
        
class CreateMentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = 'nama','jabatan','email','no_hp'


class CreateDosenForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateDosenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['program_studi'].empty_label = 'Pilih Program Studi'
    class Meta:
        model = Dosen
        fields = ['nidn','tgl_lahir','email','program_studi','no_hp']
        exclude = ['user']
        widgets = {
            'nidn': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'Nidn', 'required': True}),
            'tgl_lahir': DateInput(attrs={'class':'form-control input-sm mb-3'}),
            'email': EmailInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'email@gmail.com','required': True}),
            'no_hp': NumberInput(attrs={'class':'form-control input-sm', 'required': False}),
            'program_studi': Select(attrs={'class':'form-control form-select input-sm mb-3', 'data-control':"select2"}),
        }

# class GantiPasswordForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['user', 'password1','password2']

class UploadTranskipForm(ModelForm):
    class Meta:
        model = Transkip
        fields = '__all__'
        widgets = {
            'transkip': forms.FileInput(attrs={'class':'form-control', 'required': True,}),
        }

class EditProfilMhsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfilMhsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['nip_dpa'].required = False
        self.fields['sertifikat'].required = False
        self.fields['no_rek'].required = False
        self.fields['nama_rek'].required = False
        self.fields['cv'].required = False
        self.fields['sptjm_liga_mbkm'].required = False
    class Meta:
        model = Mahasiswa
        fields = ['email','no_hp','nama_dpa','nip_dpa','nidn_dpa','cv','sertifikat','no_rek','nama_rek','sptjm_liga_mbkm']
        widgets = {
            'no_hp': NumberInput(attrs={'class':'form-control input-sm', 'required': False}),
            'email': EmailInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'email@gmail.com','required': True}),
            'nama_dpa': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'Nama beserta title', 'required': True}),
            'nip_dpa': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'NIP'}),
            'nidn_dpa': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'NIDN'}),
            'cv': forms.URLInput(attrs={'class':'form-control input-sm','placeholder':'Link Drive terbuka akses untuk view','id':'linkInputCV'}),
            'sertifikat': forms.URLInput(attrs={'class':'form-control input-sm','placeholder':'Link Drive terbuka akses untuk view','id':'linkInputSertifikat'}),
            'no_rek': NumberInput(attrs={'class':'form-control input-sm','placeholder':'Nomor Rekening BNI/BSI Pribadi'}),
            'nama_rek': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'Nama Rekening BNI/BSI Pribadi'}),
            'sptjm_liga_mbkm': forms.URLInput(attrs={'class':'form-control input-sm','placeholder':'Link Drive terbuka akses untuk view','id':'linkInputSPTJM'}),
        }

class EditProfilMhsInboundForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfilMhsInboundForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = MahasiswaInbound
        fields = ['nim','nik','tgl_lahir','email','no_hp','ipk','total_sks','no_hp_orang_tua','fakultas_asal','kode_pt_asal','pic_pt_asal','no_hp_pic']
        widgets = {

            'nim': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'Tuliskan NIMmu'}),
            'nik': NumberInput(attrs={'class':'form-control input-sm','placeholder':'Tuliskan NIKmu'}),
            'tgl_lahir': DateInput(attrs={'class':'form-control input-sm mb-3'}),
            'email': EmailInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'email@gmail.com','required': True}),
            'no_hp': NumberInput(attrs={'class':'form-control input-sm'}),
            'ipk': NumberInput(attrs={'class':'form-control input-sm', 'required': True, 'step':'0.01'}),
            'total_sks': NumberInput(attrs={'class':'form-control input-sm'}),
            'fakultas_asal': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'Tuliskan Fakultasmu'}),
            'no_hp_orang_tua': NumberInput(attrs={'class':'form-control input-sm'}),
            'pic_pt_asal': TextInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'Tuliskan Nama Lengkap PIC Asalmu Beserta Gelar '}),
            'kode_pt_asal': NumberInput(attrs={'class':'form-control input-sm'}),
            'no_hp_pic': NumberInput(attrs={'class':'form-control input-sm'}),
           
        }

class EditMhsInboundForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditMhsInboundForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = MahasiswaInbound
        fields = ['dosen']
        widgets = {
           'dosen': Select(attrs={'class':'form-control form-select input-sm mb-3'}),
        }


class EditProfilDsnForm(ModelForm):
    class Meta:
        model = Dosen
        fields = ['email','no_hp']
        widgets = {
            'no_hp': NumberInput(attrs={'class':'form-control input-sm', 'required': False}),
            'email': EmailInput(attrs={'class':'form-control input-sm mb-3', 'placeholder':'email@gmail.com','required': True}),
        }