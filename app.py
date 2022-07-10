
import psutil
import sys

memory = psutil.virtual_memory()
print("Sebelum memory dipakai ..........")
print("Total memory                 :",memory.total, "bytes",round(memory.total/2**30,2),"GB")
print("Total memory Used            :",memory.used, "bytes",round(memory.used/2**30,2),"GB")
print("Total memory Free            :",memory.free, "bytes",round(memory.free/2**30,2),"GB")
print("Total memory Percent Used    :",memory.percent,"%")
print("========================================================")

a = {}

for i in range(1024*1024) : 
    a[i]=i

str1 = "one"
str2 = "two"
str3 = "three"
int1 = 1
int2 = 11
int3 =11111
float1 = 89.9
float2 = 1000.2
float3 = 129999.89


print("Memory Size Of 'str1' variable = ",sys.getsizeof(str1),"bytes")
print("Memory Size Of 'str2' variable = ",sys.getsizeof(str2),"bytes")
print("Memory Size Of 'str3' variable = ",sys.getsizeof(str3),"bytes")
print("Memory Size Of 'int1' variable = ",sys.getsizeof(int1),"bytes")
print("Memory Size Of 'int2' variable = ",sys.getsizeof(int2),"bytes")
print("Memory Size Of 'int3' variable = ",sys.getsizeof(int3),"bytes")
print("Memory Size Of 'float1' variable = ",sys.getsizeof(float1),"bytes")
print("Memory Size Of 'float2' variable = ",sys.getsizeof(float2),"bytes")
print("Memory Size Of 'float3' variable = ",sys.getsizeof(float3),"bytes")
print("Memory Size Of 'a' variable = ",sys.getsizeof(a),"bytes", round(sys.getsizeof(a)/2**20,2),"MB")
print("========================================================")

print("Setelah memory dipakai ..........")
print("Total memory                 :",memory.total, "bytes",round(memory.total/2**30,2),"GB")
print("Total memory Used            :",memory.used, "bytes",round(memory.used/2**30,2),"GB")
print("Total memory Free            :",memory.free, "bytes",round(memory.free/2**30,2),"GB")
print("Total memory Percent Used    :",memory.percent,"%")

print("========================================================")
