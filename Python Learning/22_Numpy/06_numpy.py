import numpy as np
# Data type in Numpy Arrays

# List of Data Type:-
# 1. Bool_
# 2. int_
# 3. intc
# 4. intp
# 5. int8
# 6. int16
# 7. int32
# 8. int64
# 9. uint8
# 10. uint16
# 11. uint32
# 12. uint64
# 13. float_
# 14. float16
# 15. float32
# 17. float64
# 18. complex64
# 19. complex128

var = np.array([1, 2, 3, 4])
print("Data Type : ", var.dtype)


var = np.array([1.0, 2.0, 3.0, 4.0])
print("Data Type : ", var.dtype)


var = np.array(["1", "2", "3", "4"])
print("Data Type : ", var.dtype)

var = np.array(["1", "2", "3", "4", 1, 2, 3, 4])
print("Data Type : ", var.dtype)

# For change Data type You want a use this short cute
# 1 i = Integer
# 2 b = Boolean
# 3 u = unsigned Integer
# 4 f = Float
# 5 c = Complex Float
# 6 m = timedelta
# 7 M = datetime
# 8 O = Object
# 9 S = String
# 10 U = Unicode String
# 11 V = The fixed Chunk Of memory for Other types (void)

x = np.array([1,2,3,4],dtype=np.int8)
print("Data Type : ",x.dtype)

x = np.array([1,2,3,4],dtype="f")
print(x)
print("Data Type : ", x.dtype)

# my question is why not use int8

# astype Function:-

x = np.array([1,2,3,4])
type_changer = x.astype('S')
print(type_changer)
