from rest_framework import status
from rest_framework.test import APIClient
import pytest
@pytest.mark.django_db
class TestCreateCollection:
    def test_anonomyous_user_response_401(self):
        client=APIClient()
        response=client.post('/store/collections',{'title':'a'})
        assert response.status_code==status.HTTP_401_UNAUTHORIZED
         