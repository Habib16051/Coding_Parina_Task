from .models import SearchInput
from .forms import KhojSearchForm
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

#####################################################################################################


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('khoj_search')

    def form_valid(self, form):
        user = form.save()
        # Log the user in.
        login(self.request, user)
        return super().form_valid(form)

############################################################################################


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('khoj_search')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

###########################################################################################


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

###########################################################################################


class KhojSearchView(LoginRequiredMixin, FormView):
    template_name = 'khoj_search.html'
    form_class = KhojSearchForm
    login_url = 'login'

    def form_valid(self, form):
        input_values = form.cleaned_data['input_values']
        search_value = form.cleaned_data['search_value']

        input_list = [int(x.strip()) for x in input_values.split(',')]
        input_list.sort(reverse=True)

        search_result = search_value in input_list

        SearchInput.objects.create(
            user=self.request.user,
            input_values=input_values,
            search_value=search_value
        )

        context = self.get_context_data()
        context['search_result'] = search_result
        return self.render_to_response(context)

###############################################################################
