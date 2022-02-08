"""
Manages inventory of different types of computer harsware specs consists of :
CPU, HDD, SDD
"""
from app.utils import validators

class Resource:
    """
    Class for claiming, killing, freeing, purchasing of a resource.
    """

    def __init__(self, name, manufacturer, total, allocated):
        """
        Args:
            name (str): Name of the Device
            manufacturer (str): Name of the manufacturing comp (NVIDIA, Samsung, etc)
            total (int): Initial number of available hardware in the inventory.
            allocated (int):Initial number of allocated hardware in the inventory.
        Returns:
            A resource Object.
        """
        self._name = name
        self._manufacture = manufacturer
        self._total = total
        self._allocated = allocated

        validators.validate_integer(
        arg_name= 'total', arg_value=total, min_value=0,
        custom_min_message=f'Cannot have negative number of {name}!')

        validators.validate_integer(
            arg_name='allocated', arg_value=allocated, min_value=0, max_value=self._total,
            custom_min_message=f'Cannot allocate negative number of {name}!',
            custom_max_message=f'Cannot allocate more than total!')

    def __str__(self):
        return f'Resource name: {self.name}' \
               f'Resource manufacturer: {self.manufacturer}' \
               f'Resource total: {self.total}' \
               f'Resource allocated: {self.allocated}'

    def claim(self, n_claimed):
        """
        Claim n number of resources to add to the allocated ones.
        If operation possible, adds n to allocated resources
        Args:
            n_claimed: number of claimed resources
        """

        #Checking n is acceptable
        validators.validate_integer(
            arg_name='n_calimed', arg_value=n_claimed, min_value=0,
            custom_min_message=f'Cannot claim negative number of {self._name}!')

        #Checking if allocation is possible
        validators.validate_integer(
            arg_name='allocated', arg_value=self._allocated + n_claimed,
            max_value=self._total,
            custom_max_message=f'Cannot allocate more than total!')

        self._allocated = self._allocated + n_claimed

    def freeup(self, n_freed):
        """
        Removes n_freed number of resources from the allocated.
        Args:
            n_freed: number of resources to be free
        """
        # Checking if n is acceptable
        validators.validate_integer(
            arg_name='n_freed', arg_value=n_freed, min_value=0,
            custom_min_message=f'Cannot free up negative number of {self._name}!')

        # Checking if freeing up is possible
        validators.validate_integer(
            arg_name='allocated', arg_value=self._allocated - n_freed,
            min_value=0,
            custom_min_message=f'Can not free up more than the allocated number')

        self._allocated = self._allocated - n_freed


    def died(self, n_died):
        """
        Can kill n_died number of specs. Will be removed from
        the total and the allocated.
        Args:
            n_died: number of dead specs
        """
        # Checking if n_died is acceptable
        validators.validate_integer(
            arg_name='n_died', arg_value=n_died, min_value=0,
            custom_min_message=f'Cannot kill negative number of {self._name}!')

        #Checking if killing is possible
        validators.validate_integer(
            arg_name='n_died', arg_value=self._allocated - n_died, min_value=0,
            custom_min_message=f'Cannot kill {self._name}s more than what is allocated!')

        self._allocated = self._allocated - n_died
        self._total = self._total - n_died

    def purchased(self, n_purchased):
        """
        Buys n_purchased number of specs. Adds n_purchased to the total.
        Args:
            n_purchased: Number of purchased specs.
        """
        # Checking if n_died is acceptable
        validators.validate_integer(
            arg_name='n_died', arg_value=n_purchased, min_value=0,
            custom_min_message=f'Cannot buy negative number of {self._name}!')

        self._total = self._total + n_purchased

    @property
    def name (self):
        return self._name

    @property
    def total (self):
        return self._total

    @property
    def manufacturer (self):
        return self._manufacture

    @property
    def allocated (self):
        return self._allocated

class Cpu (Resource):
    """
    Cpu is a Resource with the ability to store the number of cores,
    sucket types and power
    """
    def __init__(self, name, manufacturer, total, allocated,
                 cores, socket, power_watts):
        """
        Args:
            name (str):
            manufacturer (str):
            total:
            allocated:
            cores (int): NUmber of cores
            socket (str): Type of the socket
            power_watts (int): Power in watts
        """

        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

        validators.validate_integer(
            arg_name='cores', arg_value=cores, min_value=0,
            custom_min_message=f'Cannot have negative number of cores!')

        validators.validate_integer(
            arg_name='power_watts', arg_value=power_watts, min_value=0,
            custom_min_message=f'Cannot have negative number of power watts!')

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts

class Storage (Resource):
    """
    Inherits from storage and has capacity attribute.
    """

    def __init__(self, name, manufacturer, total, allocated, capacity):
        """
        Args:
            name (str): Name of the Device
            manufacturer (str): Name of the manufacturing comp (NVIDIA, Samsung, etc)
            total (int): Initial number of available hardware in the inventory.
            allocated (int):Initial number of allocated hardware in the inventory.
            capacity (int): Capacity of the storage
        """
        super().__init__(name, manufacturer, total, allocated)
        self._capacity = capacity

        validators.validate_integer(
            arg_name='capacity', arg_value=capacity, min_value=0,
            custom_min_message=f'Cannot have a negative number for capacity!')

    @property
    def capacity(self):
        return self._capacity

class Hdd (Storage):
    """
    Adds size and rpm to Storage class.
    """
    def __init__(self, name, manufacturer, total, allocated, capacity, size, rpm):
        """
        Args:
            name (str): Name of the Device
            manufacturer (str): Name of the manufacturing comp (NVIDIA, Samsung, etc)
            total (int): Initial number of available hardware in the inventory.
            allocated (int):Initial number of allocated hardware in the inventory.
            capacity (int): Capacity of the storage
            size (int): Size of HDD
            rpm (int): Round/minute

        Returns:

        """
        super().__init__(name, manufacturer, total, allocated, capacity)
        self._size = size
        self._rpm = rpm

        validators.validate_integer(
            arg_name='size', arg_value=size, min_value=0,
            custom_min_message=f'Cannot have a negative number for size!')

        validators.validate_integer(
            arg_name='rpm', arg_value=rpm, min_value=0,
            custom_min_message=f'Cannot have a negative number for rpm!')

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm


class Sdd(Storage):
    """
    Adds interface to the Storage class.
    """

    def __init__(self, name, manufacturer, total, allocated, capacity, interface):
        super().__init__(name, manufacturer, total, allocated, capacity)
        self._interface = interface

    @property
    def interface(self):
        return self._interface





