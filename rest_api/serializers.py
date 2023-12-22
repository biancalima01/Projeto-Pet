from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)
import datetime
from reserva.models import Petshop, Reserva


class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )

    class Meta:
        model = Petshop
        fields = '__all__'


class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        return self.serializer(value, context=self.context).data


class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'


class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetShopRelatedFieldCustomSerializer(
        queryset= Petshop.objects.all(),
        read_only=False
    )

    def validate_data(self, value):
        hoje = datetime.date.today()
        if value < hoje:
            raise ValidationError('Não é possível realizar um agendamento para o passado!')
        return value

    class Meta:
        model = Reserva
        fields = '__all__'
