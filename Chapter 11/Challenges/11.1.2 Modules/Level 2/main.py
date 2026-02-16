import si_conversion
import cube_shape

side_in_m = int(input())

surface_area_m2 = cube_shape.surface_area(side_in_m)
side_in_cm = si_conversion.m_to_cm(side_in_m)
surface_area_cm2 = cube_shape.surface_area(side_in_cm)

print(f'Cube surface area is {surface_area_m2} m^2 or {surface_area_cm2} cm^2.')