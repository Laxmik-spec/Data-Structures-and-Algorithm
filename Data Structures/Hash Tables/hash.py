# Hash Implementation

def hash_function(key,m):
    return key % m

m = 10
print("Hash Table Size:", m)
hash_table = [[] for _ in range(m)]
print("Hash Table:", hash_table)
print("Inserting values into the hash table:")
for i in range(1, m+1):
    index = hash_function(i, m)
    hash_table[index].append(i)
    print(f"Inserted {i} at index {index}: {hash_table}")
print("Final Hash Table:", hash_table)