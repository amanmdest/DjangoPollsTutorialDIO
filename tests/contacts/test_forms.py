from contacts.forms import NameForm


def test_name_form_sucess():
    data = {"your_name": "Robin"}
    form = NameForm(data=data)

    result = form.is_valid()

    assert form.data == {'your_name': 'Robin'}
    assert result == True


def test_name_form_max_length():
    data = {"your_name": "Robin" * 50}
    form = NameForm(data=data)

    assert form.is_valid() is False
    assert form.errors == {
        'your_name': ['Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 250).']
    }


def test_name_form_fail():
    data = {}
    form = NameForm(data=data)

    result = form.is_valid()

    assert result == False