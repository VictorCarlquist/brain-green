from django.urls import reverse
from rest_framework import status
from .models import Producer, Farm, AreaFarm
from .views import DashboardData, ProducerList, ProducerDetail, FarmList, FarmDetail, AreaList, AreaDetail
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

class ProducerTests(APITestCase):

    def setUp(self) -> None:
        User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        return super().setUp()


    def test_add_producer(self):
        """
        Ensure we can create a new account object.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('producer-list')
        view = ProducerList.as_view()

        data = {
            "name": "Victor",
            "cpf_cnpj": "33206107083"
        }

        # Make an authenticated request
        request = factory.post(url, data=data, format='json')
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producer.objects.count(), 1)
        self.assertEqual(Producer.objects.get().name, 'Victor')

    def test_get_producer(self):
        """
        Ensure we can get a producer object.
        """
        producer = Producer.objects.create(name="Victor", cpf_cnpj="33206107083")

        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('producer-detail', args=[producer.pk])
        view = ProducerDetail.as_view()

        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request, pk=producer.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'Victor')
        self.assertEqual(response.data.get('cpf_cnpj'), '33206107083')

    def test_update_producer(self):
        """
        Ensure we can update a producer object.
        """
        producer = Producer.objects.create(name="Victor", cpf_cnpj="33206107083")

        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('producer-detail', args=[producer.pk])
        view = ProducerDetail.as_view()

        data = {
            "name": "Carla",
            "cpf_cnpj": "33206107083"
        }

        # Make an authenticated request
        request = factory.put(url, data=data, format='json')
        force_authenticate(request, user=user)
        response = view(request, pk=producer.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'Carla')
        self.assertEqual(response.data.get('cpf_cnpj'), '33206107083')

    def test_delete_producer(self):
        """
        Ensure we can delete a producer object.
        """
        producer = Producer.objects.create(name="Victor", cpf_cnpj="33206107083")

        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('producer-detail', args=[producer.pk])
        view = ProducerDetail.as_view()

        # Make an authenticated request
        request = factory.delete(url)
        force_authenticate(request, user=user)
        response = view(request, pk=producer.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Producer.objects.count(), 0)

    def test_list_producer(self):
        """
        Ensure we can list all producer objects.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('producer-list')
        view = ProducerList.as_view()
        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Producer.objects.count())


class FarmTests(APITestCase):

    def setUp(self) -> None:
        User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        Producer.objects.create(name="Victor", cpf_cnpj="33206107083")
        return super().setUp()

    def test_add_farm(self):
        """
        Ensure we can create a new farm object.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('farm')
        view = FarmList.as_view()

        data = {
            "farm_name": "Fazenda",
            "producer_id": 1,
            "total_area_hectares": 100,
            "city": "São Paulo",
            "state": "SP"
        }

        # Make an authenticated request
        request = factory.post(url, data=data, format='json')
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Farm.objects.count(), 1)
        self.assertEqual(Farm.objects.get().farm_name, 'Fazenda')
        self.assertEqual(Farm.objects.get().producer_id, 1)
        self.assertEqual(Farm.objects.get().total_area_hectares, 100)
        self.assertEqual(Farm.objects.get().city, 'São Paulo')
        self.assertEqual(Farm.objects.get().state, 'SP')

    def test_get_farm(self):
        """
        Ensure we can get a farm object.
        """
        farm = Farm.objects.create(farm_name="Fazenda", producer_id=1, total_area_hectares=100, city="São Paulo", state="SP")

        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('farm-detail', args=[farm.pk])
        view = FarmDetail.as_view()

        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request, pk=farm.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('farm_name'), 'Fazenda')
        self.assertEqual(response.data.get('producer_id'), 1)
        self.assertEqual(response.data.get('total_area_hectares'), 100)
        self.assertEqual(response.data.get('city'), 'São Paulo')
        self.assertEqual(response.data.get('state'), 'SP')

    def test_update_farm(self):
        """
        Ensure we can update a farm object.
        """
        farm = Farm.objects.create(farm_name="Fazenda", producer_id=1, total_area_hectares=100, city="São Paulo", state="SP")

        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('farm-detail', args=[farm.pk])
        view = FarmDetail.as_view()

        data = {
            "farm_name": "Minha farm",
            "producer_id": 1,
            "total_area_hectares": 200,
            "city": "Rio de Janeiro",
            "state": "RJ"
        }

        # Make an authenticated request
        request = factory.put(url, data=data, format='json')
        force_authenticate(request, user=user)
        response = view(request, pk=farm.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('farm_name'), 'Minha farm')
        self.assertEqual(response.data.get('producer_id'), 1)
        self.assertEqual(response.data.get('total_area_hectares'), 200)
        self.assertEqual(response.data.get('city'), 'Rio de Janeiro')
        self.assertEqual(response.data.get('state'), 'RJ')

    def test_delete_farm(self):
        """
        Ensure we can delete a farm
        """
        farm = Farm.objects.create(farm_name="Fazenda", producer_id=1, total_area_hectares=100, city="São Paulo", state="SP")

        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('farm-detail', args=[farm.pk])
        view = FarmDetail.as_view()

        # Make an authenticated request
        request = factory.delete(url)
        force_authenticate(request, user=user)
        response = view(request, pk=farm.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Farm.objects.count(), 0)

    def test_list_farm(self):
        """
        Ensure we can list all farm objects.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('farm-list',args=[1])
        view = FarmList.as_view()
        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request, pk_producer=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), AreaFarm.objects.count())


class AreaFarmTest(APITestCase):

    def setUp(self) -> None:
        User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        Producer.objects.create(name="Victor", cpf_cnpj="33206107083")
        Farm.objects.create(farm_name="Fazenda", producer_id=1, total_area_hectares=100, city="São Paulo", state="SP")
        return super().setUp()

    def test_add_area(self):
        """
        Ensure we can create a new area object.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('area')
        view = AreaList.as_view()

        data = {
            "farm_id": 1,
            "area_type": "AR",
            "area_hectares": 50,
            "crops": "SO"
        }

        # Make an authenticated request
        request = factory.post(url, data=data, format='json')
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AreaFarm.objects.count(), 1)
        self.assertEqual(AreaFarm.objects.get().area_hectares, 50)

    def test_add_area_bigger_than_farm(self):
        """
        Ensure we can create a new area object.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('area')
        view = AreaList.as_view()

        data = {
            "farm_id": 1,
            "area_type": "AR",
            "area_hectares": 60,
            "crops": "SO"
        }

        # Make an authenticated request
        request = factory.post(url, data=data, format='json')
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AreaFarm.objects.count(), 1)
        self.assertEqual(AreaFarm.objects.get().area_hectares, 60)
        try:
            request = factory.post(url, data=data, format='json')
            force_authenticate(request, user=user)
            response = view(request)
        except Exception as e:
            self.assertEqual(str(e), "Sum area 120.0 bigger than total farm area 100.0")

    def test_get_area(self):
        """
        Ensure we can get a area object.
        """
        area = AreaFarm.objects.create(farm_id=1, area_type="AR", area_hectares=50, crops="SO")
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('area-detail', args=[area.pk])
        view = AreaDetail.as_view()

        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request, pk=area.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('farm_id'), 1)
        self.assertEqual(response.data.get('area_type'), 'AR')
        self.assertEqual(response.data.get('area_hectares'), 50)
        self.assertEqual(response.data.get('crops'), 'SO')

    def test_update_area(self):
        """
        Ensure we can update an area object.
        """
        area = AreaFarm.objects.create(farm_id=1, area_type="AR", area_hectares=50, crops="SO")
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('area-detail', args=[area.pk])
        view = AreaDetail.as_view()
        data = {
            "farm_id": 1,
            "area_type": "GR",
            "area_hectares": 75,
            "crops": "CO"
        }
        # Make an authenticated request
        request = factory.put(url, data=data, format='json')
        force_authenticate(request, user=user)
        response = view(request, pk=area.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('area_type'), 'GR')
        self.assertEqual(response.data.get('area_hectares'), 75)
        self.assertEqual(response.data.get('crops'), 'CO')


    def test_update_area_bigger_than_farm(self):
        """
        Ensure we can update an area object.
        """
        area = AreaFarm.objects.create(farm_id=1, area_type="AR", area_hectares=50, crops="SO")
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('area-detail', args=[area.pk])
        view = AreaDetail.as_view()
        data = {
            "farm_id": 1,
            "area_type": "GR",
            "area_hectares": 120,
            "crops": "CO"
        }
        # Make an authenticated request
        try:
            request = factory.put(url, data=data, format='json')
            force_authenticate(request, user=user)
            response = view(request, pk=area.pk)
        except Exception as e:
            self.assertEqual(str(e), "Sum area 120.0 bigger than total farm area 100.0")


    def test_delete_area(self):
        """
        Ensure we can delete an area object.
        """
        area = AreaFarm.objects.create(farm_id=1, area_type="AR", area_hectares=50, crops="SO")
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('area-detail', args=[area.pk])
        view = AreaDetail.as_view()

        # Make an authenticated request
        request = factory.delete(url)
        force_authenticate(request, user=user)
        response = view(request, pk=area.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AreaFarm.objects.count(), 0)

    def test_list_area(self):
        """
        Ensure we can list all farm objects.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('area-list', args=[1])
        view = AreaList.as_view()
        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request, pk_farm=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), AreaFarm.objects.count())


class DashboardTest(APITestCase):

    def setUp(self) -> None:
        User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        Producer.objects.create(name="Victor", cpf_cnpj="33206107083")
        Farm.objects.create(farm_name="Fazenda", producer_id=1, total_area_hectares=100, city="São Paulo", state="SP")
        Farm.objects.create(farm_name="Fazenda2", producer_id=1, total_area_hectares=30, city="São Paulo", state="PR")
        Farm.objects.create(farm_name="Fazenda3", producer_id=1, total_area_hectares=60, city="São Paulo", state="PR")
        AreaFarm.objects.create(farm_id=1, area_type="AR", area_hectares=50, crops="SO")
        AreaFarm.objects.create(farm_id=1, area_type="AR", area_hectares=20, crops="SO")

        return super().setUp()

    def test_total_farm(self):
        """
        Ensure we can list all farm objects.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('get_total_farm')
        view = DashboardData.as_view({'get': 'get_total_farm'})
        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, Farm.objects.count())

    def test_total_area(self):
        """
        Ensure we can get the total area of all farms.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('get_total_area')
        view = DashboardData.as_view({'get': 'get_total_area'})
        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 190)

    def test_total_by_state(self):
        """
        Ensure we can get the total area by state.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('get_total_state')
        view = DashboardData.as_view({'get': 'get_total_by_state'})
        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data),  [{'state': 'PR', 'total': 90.0}, {'state': 'SP', 'total': 100.0}])

    def test_total_by_crop(self):
        """
        Ensure we can get the total area by crop.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('get_total_crop')
        view = DashboardData.as_view({'get': 'get_total_by_crop'})
        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data), [{'areafarm__crops': 'SO', 'total': 70.0}])

    def test_total_by_type(self):
        """
        Ensure we can get the total area by type.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='john')
        url = reverse('get_total_type')
        view = DashboardData.as_view({'get': 'get_total_by_type'})
        # Make an authenticated request
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data), [{'areafarm__area_type': 'AR', 'total': 70.0}])