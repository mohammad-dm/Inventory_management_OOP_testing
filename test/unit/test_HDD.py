from app.models import inventory
import pytest

#-----------------------------------Test CPU---------------------------------------
@pytest.fixture
def hdd_values():
    return {
        'name': 'MyHDD',
        'manufacturer': 'WD',
        'total': 40,
        'allocated': 25,
        'capacity': 500,
        'size': 20,
        'rpm': 85
    }

@pytest.fixture
def hdd(hdd_values):
    return inventory.Hdd(**hdd_values)

def test_hdd_initialization(hdd, hdd_values):
    assert hdd.name == hdd_values['name']
    assert hdd.manufacturer == hdd_values['manufacturer']
    assert hdd.total == hdd_values['total']
    assert hdd.allocated == hdd_values['allocated']
    assert hdd.capacity == hdd_values['capacity']
    assert hdd.size == hdd_values['size']
    assert hdd.rpm == hdd_values['rpm']


def test_hdd_init_value_error_negative_total(hdd_values):
    hdd_values['total'] = -10
    with pytest.raises(ValueError):
        my_hdd = inventory.Hdd(**hdd_values)

def test_hdd_init_value_error_negative_allocated(hdd_values):
    hdd_values['allocated'] = -10
    with pytest.raises(ValueError):
        my_hdd = inventory.Hdd(**hdd_values)

def test_hdd_init_value_error_negative_capacity(hdd_values):
    hdd_values['capacity'] = -10
    with pytest.raises(ValueError):
        my_hdd = inventory.Hdd(**hdd_values)

def test_hdd_init_value_error_negative_size(hdd_values):
    hdd_values['size'] = -10
    with pytest.raises(ValueError):
        my_hdd = inventory.Hdd(**hdd_values)

def test_hdd_init_value_error_negative_rpm(hdd_values):
    hdd_values['rpm'] = -10
    with pytest.raises(ValueError):
        my_hdd = inventory.Hdd(**hdd_values)

@pytest.mark.parametrize('total,allocated,n_claimed',[(10,3,8), (4,3,-10)] )
def test_claim_value_error(hdd, total, allocated, n_claimed):
    hdd._total = total
    hdd._allocated = allocated
    with pytest.raises(ValueError):
        hdd.claim(n_claimed)

def test_claim_type_error(hdd):
    n_claimed = 1.5
    with pytest.raises(TypeError):
        hdd.claim(hdd)

#-----------------------------------Test Hdd.freeup()----------------------------
@pytest.mark.parametrize('total,allocated,n_freed',[(10,3,5), (10,3,-10)] )
def test_free_up_value_error(hdd, total, allocated, n_freed):
    hdd._total = total
    hdd._allocated = allocated
    print(hdd)
    with pytest.raises(ValueError):
        hdd.freeup(n_freed)

def test_free_up_type_error(hdd):
    n_freed = 1.2
    with pytest.raises(TypeError):
        hdd.freeup(n_freed)

#-----------------------------------Test Hdd.died()----------------------------
@pytest.mark.parametrize('total,allocated,n_died',[(10,3,5), (10,3,-10),(10,3,50)] )
def test_died_value_error(hdd, total, allocated, n_died):
    hdd._total = total
    hdd._allocated = allocated
    with pytest.raises(ValueError):
        hdd.freeup(n_died)

def test_died_type_error(hdd):
    n_died = 1.2
    with pytest.raises(TypeError):
        hdd.freeup(n_died)
#---------------------------------Test Hdd.purchased()-------------------------
@pytest.mark.parametrize('total,allocated,n_purchased', [(10,3,-5)])
def test_purchased_value_error(hdd, total, allocated, n_purchased):
    hdd._total = total
    hdd._allocated = allocated
    with pytest.raises(ValueError):
        hdd.freeup(n_purchased)

def test_purchased_type_error(hdd):
    n_purchased= 1.2
    with pytest.raises(TypeError):
        hdd.freeup(n_purchased)

