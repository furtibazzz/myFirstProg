#inserting a comment line...
def append_twice(list_name,value):
  list_name.append(value)
  list_name.append(value)
  
nums = [1,2,3]
append_twice(nums,7) 
print(nums)  #[1,2,3,7,7]
