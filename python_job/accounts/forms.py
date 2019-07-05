from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


GENDER_CHOICES = (
    ('male', 'Nam'),
    ('female', 'Nữ'))


class EmployeeRegistrationForm(UserCreationForm):
    # gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENDER_CHOICES)

    def __init__(self, *args, **kwargs):
        super(EmployeeRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        # self.fields['gender'].widget = forms.CheckboxInput()

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['hotline'].widget.attrs.update(
            {
                'placeholder': 'Enter Hotline',
            }
        )

        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','hotline', 'password1', 'password2', 'gender',]

        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'gender': {
                'required': 'Gender is required'
            }
        }

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "Freelance"
        if commit:
            user.save()
        return user


class EmployerRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(EmployerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Company Name"
        self.fields['last_name'].label = "Company Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Company Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Company Address',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['hotline'].widget.attrs.update(
            {
                'placeholder': 'Enter Số Điện Thoại',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'hotline','email', 'password1', 'password2',]

        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            }
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "NhaTuyenDung"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user

# freelance update

exp_choice = (
    ('Mới đi làm  ( Dưới 2 năm kinh nghiệm) ', 'Mới đi làm  (Dưới 2 năm kinh nghiệm) '),
    ('Đã có kinh nghiệm ( 2-5 năm kinh nghiệm)', 'Đã có kinh nghiệm (2-5 năm kinh nghiệm)'),
    ('Chuyên gia ( Trên 5 năm kinh nghiệm)', 'Chuyên gia(Trên 5 năm kinh nghiệm)'))

class ProfileUpdateBasic(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateBasic, self).__init__(*args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

        # self.fields['gender'].widget = forms.CheckboxInput()

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['hotline'].widget.attrs.update(
            {
                'placeholder': 'Enter Hotline',
            }
        )


    #year_exp = forms.ChoiceField(widget=forms.Select, choices=exp_choice)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','hotline', 'gender',]
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'gender': {
                'required': 'Gender is required'
            }
        }

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = super(ProfileUpdateBasic, self).save(commit=False)
       # user.role = "Freelance"
        if commit:
            user.save()
        return user



class ProfileUpdateCV(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         super(ProfileUpdateCV, self).__init__(*args, **kwargs)
         self.fields['year_exp'].label = "Trình Độ"

     year_exp = forms.ChoiceField(widget=forms.Select, choices=exp_choice)

     class Meta:
         model = User
         fields = ['hinh', 'sologan','nganh_nghes', 'description','skill','thanh_phos','year_exp', ]

     def save(self, commit=True):
         user = super(ProfileUpdateCV, self).save(commit=False)
         #user.role = "Freelance"
         if commit:
             user.save()
         return user


