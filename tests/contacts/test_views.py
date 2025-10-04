from http import HTTPStatus

from django.contrib.auth.models import User, Permission
from django.urls import reverse

import pytest


def test_contacts_create_without_authenticated_user(client):
    # '/accounts/login/?next=/contacts/create/'
    url = f'{reverse("accounts:login")}?next={reverse("contacts:create")}'
    
    response = client.get("/contacts/create/")
        
    assert response.status_code == HTTPStatus.FOUND
    # assert reverse('accounts:login') in response.url
    assert response.url == url


@pytest.mark.django_db
def test_contacts_create_success(client, django_user_model):    
    data = {
        'subject': 'abobrinha', 
        'message': 'wake up donnie', 
        'sender': 'darko@timetravel.com',
        'cc_myself': True,
    }

    username = "vulfpeck"
    password = "newguru"
    permission = Permission.objects.get(codename="add_contact")
    user = django_user_model.objects.create_user(username=username, password=password)
    user.user_permissions.add(permission)

    client.force_login(user)

    response = client.post("/contacts/create/", data)
    
    # breakpoint()
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse("contacts:thanks", args=(data["subject"], ))

    

def test_contacts_thanks(client):
    name = "Hikaru"

    response = client.get(f"/contacts/thanks/{name}")

    assert response.status_code == HTTPStatus.OK
    assert f"Congratulations {name}!" in response.content.decode()

