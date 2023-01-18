from rich import print

from edgar.form import SecForms


def test_list_forms():
    forms = SecForms.load()
    assert len(forms) > 100


def test_forms_summary():
    forms = SecForms.load()
    summary = forms.summary()
    assert len(summary) == len(forms)
    print()
    print(forms)


def test_forms_get_form():
    forms = SecForms.load()
    form = forms.get_form('10-K')
    assert form
    assert form.form == '10-K'
    print(form)
    form = forms['10-Q']
    print(form)
