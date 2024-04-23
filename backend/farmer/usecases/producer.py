from typing import List

from ..entities.entity_base import EntityBaseInterface
from ..serializers import ProducerSerializer


class ProducerUseCase:
    def __init__(self, repository: EntityBaseInterface) -> None:
        self.repository = repository

    def add(self, data: ProducerSerializer):
        self.repository.add(data.data)

    def get(self, pk: int) -> ProducerSerializer:
        data = self.repository.get(pk)
        return ProducerSerializer(data)

    def update(self, pk: int, data: ProducerSerializer):
        self.repository.update(pk, data.data)

    def delete(self, pk: int):
        self.repository.delete(pk)

    def list(self, filters: dict = {}) -> ProducerSerializer:
        data = self.repository.listItems(filters)
        return ProducerSerializer(data, many=True)


