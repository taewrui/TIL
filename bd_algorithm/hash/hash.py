def custom_hash(a):
    return hash(a) % 10000

print(custom_hash("dfdff"))
print(custom_hash("dfdff"))