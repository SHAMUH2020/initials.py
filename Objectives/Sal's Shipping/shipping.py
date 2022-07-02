def shipping_cost_ground(weight):

# Ground Shipping
  if weight <= 2:
    price_per_pound = 1.5
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound =  4.75

  return 20 + (price_per_pound * weight)

print ("Ground Shipping: $", shipping_cost_ground(4.8))

# Ground Shipping Premium
shipping_cost_ground_premium = 125.00
print("Ground Shipping Premium: $", shipping_cost_ground_premium)

# Drone Shipping

def shipping_cost_drone(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound =  14.25

  return price_per_pound * weight
print ("Drone Shipping: $", shipping_cost_drone (4.8))
