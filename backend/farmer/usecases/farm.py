from ..entities.entity_base import EntityBaseInterface
from ..serializers import FarmSerializer, AreaFarmSerializer


class FarmUseCase:
    def __init__(self, repository: EntityBaseInterface) -> None:
        self.repository = repository

    def add(self, data: FarmSerializer):
        self.repository.add(data.data)

    def get(self, pk: int) -> FarmSerializer:
        data = self.repository.get(pk)
        return FarmSerializer(data)

    def update(self, pk: int, data: FarmSerializer):
        self.repository.update(pk, data.data)

    def delete(self, pk: int):
        self.repository.delete(pk)

    def list(self, filters: dict = {}) -> FarmSerializer:
        data = self.repository.listItems(filters)
        return FarmSerializer(data, many=True)

    def total_farm(self):
        return self.repository.count()

    def total_area(self):
        return self.repository.total_area()

    def total_by_state(self):
        return self.repository.total_by_state()

    def total_by_crop(self):
        return self.repository.total_by_crop()

    def total_by_type(self):
        return self.repository.total_by_type()


class AreaUseCase:
    def __init__(self, repository: EntityBaseInterface, farm_repository: EntityBaseInterface) -> None:
        self.repository = repository
        self.farm_repository = farm_repository

    def check_area(self, data: AreaFarmSerializer, pk_update=None):
        pk = data.data["farm_id"]
        currently_area = self.farm_repository.sum_area(pk)

        farm = self.farm_repository.get(pk)
        total_area = farm.total_area_hectares
        discount_update_area = 0
        if pk_update:
            area = self.repository.get(pk_update)
            discount_update_area = area.area_hectares

        new_area = (currently_area + data.data["area_hectares"]) - discount_update_area
        if total_area < new_area:
            raise Exception(f"Sum area {new_area} bigger than total farm area {total_area}")

    def add(self, data: AreaFarmSerializer):
        self.check_area(data)
        self.repository.add(data.data)

    def get(self, pk: int) -> AreaFarmSerializer:
        data = self.repository.get(pk)
        return AreaFarmSerializer(data)

    def update(self, pk: int, data: AreaFarmSerializer):
        self.check_area(data, pk)
        self.repository.update(pk, data.data)

    def delete(self, pk: int):
        self.repository.delete(pk)

    def list(self, filters: dict = {}) -> AreaFarmSerializer:
        data = self.repository.listItems(filters)
        return AreaFarmSerializer(data, many=True)

