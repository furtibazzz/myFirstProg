#inserting a comment line...
def append_twice(list_name,value):
  list_name.append(value)
  list_name.append(value)
  
nums = [1,2,3]
append_twice(nums,7) 
print(nums)  #[1,2,3,7,7]

#the second and Bad Way that not returns as expected!!
def append_twice_bad(a_list,val):
  a_list = a_list + [val ,val]
  print(a_list)
nums = [1,2,3]
append_twice_bad(nums,7)
print(nums) #[1,2,3]
