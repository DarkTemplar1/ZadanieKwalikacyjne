from django import forms
import datetime

class PESELForm(forms.Form):
    pesel = forms.CharField(label="Numer PESEL", max_length=11, min_length=11, required=True)

    def clean_pesel(self):
        pesel = self.cleaned_data['pesel']
        if not pesel.isdigit():
            raise forms.ValidationError("PESEL może zawierać tylko cyfry.")

        if not self.is_valid_pesel(pesel):
            raise forms.ValidationError("Niepoprawny numer PESEL.")

        return pesel

    def is_valid_pesel(self, pesel):
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        checksum = sum(int(pesel[i]) * weights[i] for i in range(10)) % 10
        control_digit = (10 - checksum) % 10
        return control_digit == int(pesel[10])

    def get_birthdate_and_gender(self, pesel):
        year = int(pesel[:2])
        month = int(pesel[2:4])
        day = int(pesel[4:6])

        if month > 80:
            year += 1800
            month -= 80
        elif month > 60:
            year += 2200
            month -= 60
        elif month > 40:
            year += 2100
            month -= 40
        elif month > 20:
            year += 2000
            month -= 20
        else:
            year += 1900

        gender = "Kobieta" if int(pesel[9]) % 2 == 0 else "Mężczyzna"
        return datetime.date(year, month, day), gender
