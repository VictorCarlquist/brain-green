from ..serializers import ProducerSerializer
from .entity_base import EntityBaseInterface
from ..models import Producer, Farm, AreaFarm
from django.db.models import Sum, Count

class ORMBase(EntityBaseInterface):

    def listItems(self, filter: list):
        q_filter = {}
        for f in filter:
            k = self.MAP_FILTER.get(f.get('filter'))
            if k:
                q_filter[self.MAP_FILTER[f.get('filter')]] = f.get('value')
        if q_filter:
            return self.model.objects.filter(**q_filter)

        return self.model.objects.all()

    def add(self, data: dict):
        return self.model.objects.create(**data)

    def get(self, pk: int):
        return self.model.objects.filter(pk=pk).first()

    def update(self, pk: int, data: dict):
        return self.model.objects.filter(pk=pk).update(**data)

    def delete(self, pk: int):
        return self.model.objects.filter(pk=pk).delete()


class ProducerEntity(ORMBase):
    MAP_FILTER = {
        "id": "id",
        "name": "name_istartswith",
        "cpf_cnpj": "cpf_cnpj",
    }

    def __init__(self):
        self.model = Producer


class FarmEntity(ORMBase):
    MAP_FILTER = {
        "id": "id",
        "producer": "producer_id",
        "farm_name": "farm_name_istartswith",
        "city": "city_istartswith",
        "state": "state_istartswith",
        "total_area_hectares": "total_area_hectares",
    }

    def __init__(self):
        self.model = Farm

    def sum_area(self, pk: int) -> float:
        return self.model.objects.filter(pk=pk).aggregate(total=Sum("areafarm__area_hectares", default=0))['total']

    def count(self):
        return self.model.objects.count()

    def total_area(self) -> float:
        return self.model.objects.aggregate(total=Sum("total_area_hectares", default=0))['total']


    def total_by_state(self) -> float:
        return (
            self.model.objects.values("state")
            .annotate(total=Sum("total_area_hectares"))
            .order_by("state")
        )

    def total_by_crop(self):
        return (
            self.model.objects
            .filter(areafarm__isnull=False)
            .values("areafarm__crops")
            .annotate(total=Sum("areafarm__area_hectares"))
        )

    def total_by_type(self):
        return (
            self.model.objects
            .filter(areafarm__isnull=False)
            .values("areafarm__area_type")
            .annotate(total=Sum("areafarm__area_hectares"))
        )

class AreaFarmEntity(ORMBase):
    MAP_FILTER = {
        "id": "id",
        "farm": "farm_id",
        "area_type": "area_type",
        "area_hectares": "area_hectares",
        "crops": "crops",
    }

    def __init__(self):
        self.model = AreaFarm
