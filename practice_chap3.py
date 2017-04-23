def sphere_volume():
  import math
  print("this program will produce the volume and surface area of a sphere based off its radius")
  r = eval(input("Please enter the spheres radius: "))
  pi = math.pi
  # volume calc
  v = round((4 / 3) * pi * (r ** 3), 2)
  # area calc
  a = round((4 * pi * (r ** 2)), 2)
  print("The volume of the give sphere with radius", r, "is", v)
  print("The surface area of the give sphere with radius", r, "is", a)

sphere_volume()