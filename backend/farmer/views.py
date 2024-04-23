import json
from rest_framework.response import Response
from .entities.orm import ProducerEntity, FarmEntity, AreaFarmEntity
from .serializers import ProducerSerializer, FarmSerializer, AreaFarmSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .usecases.producer import ProducerUseCase
from .usecases.farm import FarmUseCase, AreaUseCase


class ProducerList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        repo = ProducerEntity()
        serializer = ProducerUseCase(repo).list()
        return Response(serializer.data)

    def get(self, request):
        repo = ProducerEntity()
        serializer = ProducerUseCase(repo).list()
        return Response(serializer.data)

    def post(self, request):

        serializer = ProducerSerializer(data=request.data)
        if serializer.is_valid():
            repo = ProducerEntity()
            ProducerUseCase(repo).add(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProducerDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        repo = ProducerEntity()
        serializer = ProducerUseCase(repo).get(pk)
        return Response(serializer.data)


    def put(self, request, pk):
        serializer = ProducerSerializer(data=request.data)
        if serializer.is_valid():
            repo = ProducerEntity()
            ProducerUseCase(repo).update(pk, serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        repo = ProducerEntity()
        ProducerUseCase(repo).delete(pk)
        return Response(status=status.HTTP_200_OK)



class FarmList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk_producer):
        repo = FarmEntity()
        print(pk_producer)
        serializer = FarmUseCase(repo).list([{'filter': 'producer', 'value': pk_producer}])
        return Response(serializer.data)

    def post(self, request):

        serializer = FarmSerializer(data=request.data)
        if serializer.is_valid():
            repo = FarmEntity()
            FarmUseCase(repo).add(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FarmDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        repo = FarmEntity()
        serializer = FarmUseCase(repo).get(pk)
        return Response(serializer.data)


    def put(self, request, pk):
        serializer = FarmSerializer(data=request.data)
        if serializer.is_valid():
            repo = FarmEntity()
            FarmUseCase(repo).update(pk, serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        repo = FarmEntity()
        FarmUseCase(repo).delete(pk)
        return Response(status=status.HTTP_200_OK)

class AreaList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk_farm):
        serializer = AreaUseCase(AreaFarmEntity(), FarmEntity()).list([{'filter': 'farm', 'value': pk_farm}])
        return Response(serializer.data)

    def post(self, request):

        serializer = AreaFarmSerializer(data=request.data)
        if serializer.is_valid():
            AreaUseCase(AreaFarmEntity(), FarmEntity()).add(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AreaDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        serializer = AreaUseCase(AreaFarmEntity(), FarmEntity()).get(pk)
        return Response(serializer.data)


    def put(self, request, pk):
        serializer = AreaFarmSerializer(data=request.data)
        if serializer.is_valid():
            AreaUseCase(AreaFarmEntity(), FarmEntity()).update(pk, serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        AreaUseCase(AreaFarmEntity(), FarmEntity()).delete(pk)
        return Response(status=status.HTTP_200_OK)


class DashboardData(ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_total_farm(self, request):
        repo = FarmEntity()
        total = FarmUseCase(repo).total_farm()
        return Response(total, status=status.HTTP_200_OK)

    def get_total_area(self, request):
        repo = FarmEntity()
        total = FarmUseCase(repo).total_area()
        return Response(total, status=status.HTTP_200_OK)

    def get_total_by_state(self, request):
        repo = FarmEntity()
        total = FarmUseCase(repo).total_by_state()
        return Response(total, status=status.HTTP_200_OK)

    def get_total_by_crop(self, request):
        repo = FarmEntity()
        total = FarmUseCase(repo).total_by_crop()
        return Response(total, status=status.HTTP_200_OK)

    def get_total_by_type(self, request):
        repo = FarmEntity()
        total = FarmUseCase(repo).total_by_type()
        return Response(total, status=status.HTTP_200_OK)

