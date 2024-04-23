import validate_docbr

from rest_framework import serializers


class ProducerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cpf_cnpj = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=100)

    def validate_cpf_cnpj(self, value):
        """
        Check that the blog post is about Django.
        """
        cpf = validate_docbr.CPF()
        if cpf.validate(value):
            return value

        cnpj = validate_docbr.CNPJ()
        if cnpj.validate(value):
            return value

        raise serializers.ValidationError("CPF/CNPJ inválido!")


class FarmSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    #producer = ProducerSerializer(read_only=True)
    producer_id = serializers.IntegerField()
    farm_name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    total_area_hectares = serializers.FloatField()


class AreaFarmSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    farm = FarmSerializer(read_only=True)
    farm_id = serializers.IntegerField()
    area_type = serializers.CharField(max_length=2)
    area_hectares = serializers.FloatField()
    crops = serializers.CharField(max_length=2)
