from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status


class AccountViewTestCase(APITestCase):
    def setUp(self):
        pass

    def test_SendCodeAPIView_phoneformat_error(self):
        url = api_reverse('account:sendcode')
        response = self.client.post(url, {'mobile_phone': '186233788ab'})
        # print(type(response.data))
        # print('test_SendCodeAPIView_phoneformat_error -> {response}'.format(response=response.data))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_SendCodeAPIView_success(self):
    #     url = api_reverse('account:sendcode')
    #     response = self.client.post(url, {'mobile_phone': '18623370060'})
    #     # print(type(response.data))
    #     # print('test_SendCodeAPIView_success -> {response}'.format(response=response.data))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_CodeRegOrLoginAPIView_phoneformat_error(self):
        url = api_reverse('account:code_regorlogin')
        response = self.client.post(url, {'mobile_phone': '1862s370060', 'veri_code': '1314'})
        # print(type(response.data))
        # print('test_CodeRegOrLoginAPIView_phoneformat_error -> {response}'.format(response=response.data))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_CodeRegOrLoginAPIView_vericode_error(self):
        url = api_reverse('account:code_regorlogin')
        response = self.client.post(url, {'mobile_phone': '18623370060', 'veri_code': '1315'})
        # print(type(response.data))
        # print('test_CodeRegOrLoginAPIView_vericode_error -> {response}'.format(response=response.data))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_CodeRegOrLoginAPIView_success(self):
        url = api_reverse('account:sendcode')
        response = self.client.post(url, {'mobile_phone': '18623370060'})
        # print(type(response.data))
        # print('test_SendCodeAPIView_success -> {response}'.format(response=response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url = api_reverse('account:code_regorlogin')
        response = self.client.post(url, {'mobile_phone': '18623370060', 'veri_code': '1314'})
        # print(type(response.data))
        # print('test_CodeRegOrLoginAPIView_success -> {response}'.format(response=response.data))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
