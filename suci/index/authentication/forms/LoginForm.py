from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["maxlength"] = "10"
        self.fields["username"].widget.attrs["autocomplete"] = "off"
        self.fields["username"].widget.attrs[
            "placeholder"
        ] = "Introduce tu cédula de identidad"
        self.fields["password"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["placeholder"] = "************"
