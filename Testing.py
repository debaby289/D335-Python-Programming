import math

def find_base_area(rad):
    area = math.pi * math.pow(rad,rad)
    return area

def find_volume(rad,height):
    volume = find_base_area(rad) * height * (1/3)
    return volume

cone_radius = float(input())
cone_height = float(input())

print(f'Cone radius: {cone_radius}')
print(f'Cone height: {cone_height}')
print(f'Base area: {find_base_area(cone_radius):.1f}')
print(f'Volume: {find_volume(cone_radius, cone_height):.1f}')