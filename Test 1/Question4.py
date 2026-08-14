

wall_area = float(input("Enter an  area of one wall: "))
interior_cost_per_unit = float(input("Enter the interior painting cost per unit area: "))
exterior_cost_per_unit = float(input("Enter the exterior painting cost per unit area: "))
 
interior_cost = (wall_area * interior_cost_per_unit)
exterior_cost = (wall_area * exterior_cost_per_unit)
total_cost = (interior_cost + exterior_cost)
 
print("Interior Painting Cost =", interior_cost)
print("Exterior Painting Cost =", exterior_cost)
print("Total Painting Cost =", total_cost)