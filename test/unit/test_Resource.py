import pytest
from app.models import inventory

#------------------------------Test Fixtures-----------------------------
@pytest.fixture
def resource_values():
    return {
        'name': 'Parrot',
        'manufacturer': 'Pirates A-Hoy',
        'total': 100,
        'allocated': 50
    }


@pytest.fixture
def Hdd_values():
    return {
        'name': 'MyHdd',
        'manufacturer': 'WD',
        'total': 500,
        'allocated': 230,
        'capacity': 1000,
        'size': 400,
        'rpm': 200
    }

@pytest.fixture
def resource(resource_values):
    return inventory.Resource(**resource_values)
#------------------------------------Test Initialization-----------------------------------------

def test_valid_initialization(resource, resource_values):
    assert resource.name == resource_values['name']
    assert resource.manufacturer ==  resource_values['manufacturer']
    assert resource.total == resource_values['total']
    assert resource.allocated == resource_values['allocated']
#-----------------------------------Test Resource.claim()----------------------------
@pytest.mark.parametrize('total,allocated,n_claimed',[(10,3,8), (4,3,-10)] )
def test_claim_value_error( resource, total, allocated, n_claimed):
    resource._total = total
    resource._allocated = allocated
    with pytest.raises(ValueError):
        resource.claim(n_claimed)

def test_claim_type_error(resource):
    n_claimed = 1.5
    with pytest.raises(TypeError):
        resource.claim(n_claimed)
#-----------------------------------Test Resource.freeup()----------------------------
@pytest.mark.parametrize('total,allocated,n_freed',[(10,3,5), (10,3,-10)] )
def test_free_up_value_error(resource, total, allocated, n_freed):
    resource._total = total
    resource._allocated = allocated
    print(resource)
    with pytest.raises(ValueError):
        resource.freeup(n_freed)

def test_free_up_type_error(resource):
    n_freed = 1.2
    with pytest.raises(TypeError):
        resource.freeup(n_freed)
#-----------------------------------Test Resource.died()----------------------------
@pytest.mark.parametrize('total,allocated,n_died',[(10,3,5), (10,3,-10),(10,3,50)] )
def test_died_value_error(resource, total, allocated, n_died):
    resource._total = total
    resource._allocated = allocated
    print(resource)
    with pytest.raises(ValueError):
        resource.freeup(n_died)

def test_died_type_error(resource):
    n_died = 1.2
    with pytest.raises(TypeError):
        resource.freeup(n_died)
#---------------------------------Test Resource.purchased()-------------------------
@pytest.mark.parametrize('total,allocated,n_purchased', [(10,3,-5)])
def test_purchased_value_error(resource, total, allocated, n_purchased):
    resource._total = total
    resource._allocated = allocated
    print(resource)
    with pytest.raises(ValueError):
        resource.freeup(n_purchased)

def test_purchased_type_error(resource):
    n_purchased= 1.2
    with pytest.raises(TypeError):
        resource.freeup(n_purchased)
#--------------------------------------Test Resouce funcs------------------------------
def test_resource_funcs (resource):
    total = resource.total
    allocated = resource.allocated
    n_claimed = 7
    n_freed = 13
    n_died = 8
    n_purchased = 25
    total = total - n_died + n_purchased
    allocated = allocated + n_claimed - n_freed - n_died

    resource.claim(n_claimed)
    resource.freeup(n_freed)
    resource.died(n_died)
    resource.purchased(n_purchased)

    assert resource.total == total
    assert resource.allocated == allocated







