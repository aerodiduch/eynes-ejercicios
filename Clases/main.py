import math

class Circulo:
    def __init__(self, radius: int) -> None:
        '''Instanciate a Circulo object

        Args:
            radius (int): Radius of the circulo

        Raises:
            ValueError: Raised if radius is equal or less than 0.
        '''
        self.radius = radius
        self.value_error = 'Radius must be greater than 0'
        if self.radius <= 0:
            raise ValueError(self.value_error)
    
    def __str__(self) -> str:
        return f'Your circulo object has a radius of {self.radius}'
    
    def __mul__(self, value):
        if value <= 0:
            raise ValueError(self.value_error)
        return self.radius * value
    
    def change_radius(self, new_radius: int):
        '''Setter for a new radius

        Args:
            new_radius (int): New radius value. Must be > 0

        Raises:
            ValueError: Raises if new radius value is equal or less than 0.
        '''
        if new_radius <= 0:
            raise ValueError(self.value_error)
        else:
            self.radius = new_radius
    
    def area(self):
        '''Calculates the area of the circle with the given radius

        Returns:
            int: area of the circulo
        '''
        return math.pi*(self.radius**2)
    
    def perimeter(self):
        '''Calculates perimeter of the circle with the given radius

        Returns:
            int: perimeter of the circulo
        '''
        return 2*math.pi*self.radius


if __name__ == '__main__':
    circulo = Circulo(23)
    print(circulo)
    print(circulo.area())
    print(circulo.perimeter())
    circulo.change_radius(10)
    print(circulo)
    print(circulo.area())
    print(circulo.perimeter())
