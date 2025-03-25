from django.shortcuts import render
from .forms import PESELForm

def pesel_validator_view(request):
    result = None
    birthdate = None
    gender = None

    if request.method == "POST":
        form = PESELForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['pesel']
            birthdate, gender = form.get_birthdate_and_gender(pesel)
            result = "PESEL jest poprawny!"
        else:
            result = "PESEL jest niepoprawny."
    else:
        form = PESELForm()

    return render(request, 'validator/index.html', {
        'form': form,
        'result': result,
        'birthdate': birthdate,
        'gender': gender,
    })
