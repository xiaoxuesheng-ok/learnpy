# 定义变量，车。
# 赋值，100.
cars = 100

#  定义变量，车的空间。
#  赋值，4.0
space_in_a_car = 4.0

# 定义司机变量
#    赋值，30 .
drivers = 30

# 定义乘客变量
#  赋值，90
passengers = 90

#  定义，没有行驶的车。
cars_not_driven = cars - drivers

#  定义, 行驶的车
cars_driven  = drivers

#  定义 , 今天满载量 =   行驶的车* 车空间
carpool_capacity = cars_driven *  space_in_a_car

#  平均每辆车,每辆车做多少人。
average_passengers_per_cas = passengers / cars_driven


#  这些车  可用
print("There are",cars,"cars available.")

# 这些司机，可用。
print("there are only",drivers,"drivers available.")

# 这些车今天空了
print("there will be",cars_not_driven,"empty cars today.")

# 今天满载可以拉这些人
print("we can transport",carpool_capacity,"people today.")

#  今天有这些乘客需要拉。
print("we have ", passengers,"to carpool today")

#  每辆车上需要放这些人。
print("we need to put about",average_passengers_per_cas,"in each car ")
