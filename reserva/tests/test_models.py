from datetime import date

import pytest
from model_bakery import baker

from reserva.models import Reserva, Petshop

@pytest.fixture
def reserva():
    data = date(2023, 12, 21)
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data=data,
        turno='tarde'
    )
    return reserva

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
    assert str(reserva) == 'Tom: 2023-12-21 - tarde'

@pytest.mark.django_db
def test_qtd_reservas_deve_retornar_reservas():
    petshop = baker.make(Petshop)
    quantidade = 3
    baker.make(
        Reserva,
        quantidade,
        petshop=petshop
    )

    assert petshop.qtd_reservas() == 3