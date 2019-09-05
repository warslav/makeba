from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class PersonalAreaView(DetailView):
    model = CustomUser
    template_name = 'home.html'


class ChangeUserView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home', kwargs={'pk': model.pk}, )
    template_name = 'change.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy("home", args=(self.object.pk,))
