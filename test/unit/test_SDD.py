from app.models import inventory
import pytest

#-----------------------------------Test CPU---------------------------------------
@pytest.fixture
def sdd_values():
    return {
        'name': 'Mysdd',
        'manufacturer': 'WD',
        'total': 40,
        'allocated': 25,
        'capacity': 500,
        'interface' : 'My Interface'
    }

@pytest.fixture
def sdd(sdd_values):
    return inventory.Sdd(**sdd_values)

def test_sdd_initialization(sdd, sdd_values):
    assert sdd.name == sdd_values['name']
    assert sdd.manufacturer == sdd_values['manufacturer']
    assert sdd.total == sdd_values['total']
    assert sdd.allocated == sdd_values['allocated']
    assert sdd.capacity == sdd_values['capacity']
    assert sdd.interface == sdd_values['interface']


def test_sdd_init_value_error_negative_total(sdd_values):
    sdd_values['total'] = -10
    with pytest.raises(ValueError):
        my_sdd = inventory.Sdd(**sdd_values)

def test_sdd_init_value_error_negative_allocated(sdd_values):
    sdd_values['allocated'] = -10
    with pytest.raises(ValueError):
        my_sdd = inventory.Sdd(**sdd_values)

def test_sdd_init_value_error_negative_capacity(sdd_values):
    sdd_values['capacity'] = -10
    with pytest.raises(ValueError):
        my_sdd = inventory.Sdd(**sdd_values)


@pytest.mark.parametrize('total,allocated,n_claimed',[(10,3,8), (4,3,-10)] )
def test_claim_value_error(sdd, total, allocated, n_claimed):
    sdd._total = total
    sdd._allocated = allocated
    with pytest.raises(ValueError):
        sdd.claim(n_claimed)

def test_claim_type_error(sdd):
    n_claimed = 1.5
    with pytest.raises(TypeError):
        sdd.claim(sdd)

#-----------------------------------Test Sdd.freeup()----------------------------
@pytest.mark.parametrize('total,allocated,n_freed',[(10,3,5), (10,3,-10)] )
def test_free_up_value_error(sdd, total, allocated, n_freed):
    sdd._total = total
    sdd._allocated = allocated
    print(sdd)
    with pytest.raises(ValueError):
        sdd.freeup(n_freed)

def test_free_up_type_error(sdd):
    n_freed = 1.2
    with pytest.raises(TypeError):
        sdd.freeup(n_freed)

#-----------------------------------Test Sdd.died()----------------------------
@pytest.mark.parametrize('total,allocated,n_died',[(10,3,5), (10,3,-10),(10,3,50)] )
def test_died_value_error(sdd, total, allocated, n_died):
    sdd._total = total
    sdd._allocated = allocated
    with pytest.raises(ValueError):
        sdd.freeup(n_died)

def test_died_type_error(sdd):
    n_died = 1.2
    with pytest.raises(TypeError):
        sdd.freeup(n_died)
#---------------------------------Test Sdd.purchased()-------------------------
@pytest.mark.parametrize('total,allocated,n_purchased', [(10,3,-5)])
def test_purchased_value_error(sdd, total, allocated, n_purchased):
    sdd._total = total
    sdd._allocated = allocated
    with pytest.raises(ValueError):
        sdd.freeup(n_purchased)

def test_purchased_type_error(sdd):
    n_purchased= 1.2
    with pytest.raises(TypeError):
        sdd.freeup(n_purchased)

