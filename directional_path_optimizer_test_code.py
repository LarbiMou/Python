# This file has test cases to verify that the dirReduc function is correct
from directional_path_optimizer import dirReduc

plan =  ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print("\nfor the plan ", plan)
print("the reduced list is:", dirReduc(plan))

plan =  ["NORTH", "SOUTH", "EAST", "WEST"]
print("\nfor the plan ", plan)
print("the reduced list is:", dirReduc(plan))

plan =  ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
print("\nfor the plan ", plan)
print("the reduced list is:", dirReduc(plan))

plan =  ["NORTH", "WEST", "SOUTH", "EAST"]
print("\nfor the plan ", plan)
print("the reduced list is:", dirReduc(plan))

plan =  ["NORTH"]
print("\nfor the plan ", plan)
print("the reduced list is:", dirReduc(plan))

plan =  []
print("\nfor the plan ", plan)
print("the reduced list is:", dirReduc(plan))

