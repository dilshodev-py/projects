"""Register View"""
"""
class CustomRegisterView(FormView):
    form_class = RegisterForm
    template_name = 'apps/auth/register.html'
    def form_valid(self, form):
        first_name = form.data.get('first_name')
        phone_number = form.data.get('phone_number')
        password = form.data.get('password')
        User.objects.get_or_create(first_name=first_name ,phone_number=phone_number , password=password)
        return redirect('login')
"""
d = {
}
print(d.get(None))