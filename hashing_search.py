import os
os.system('cls')

hash_table = [None] * 20
# Fungsi
def hash_function(value):
    # return len(value) %10
    return  10% len(value)

def hash_coll(value):
    return 15% len(value)

def insertt(hash_table,value):
    hash_key = hash_function(value)
    if hash_table[hash_key] is None:
        hash_table[hash_key] = value
    else:
        hash_key = hash_coll(value)
        hash_table[hash_key] = value

# Menambahkan data
# def insert(hash_table, value):
#     hash_key = hash_function(value)
#     hash_table[hash_key] = value

# Mencari Data
def search(hash_table,value):
    result = hash_function(value)
    if hash_table[result] == value:
        return result
    else:
        result = hash_coll(value)
        return result
    
    # return hash_table[hash_function(value)]

insertt(hash_table,'Perindo')
insertt(hash_table,'GERINDRA')
insertt(hash_table,'PSI')
insertt(hash_table,'PDI')
insertt(hash_table,'Golkar')
print(hash_table)
print (hash_function('PDI'))
print (hash_coll('PDI'))

partai = 'Golkar'
print(search(hash_table,partai))

# partai = 'Golkar'
# print(search(hash_table,partai),'Berada Di Index Ke-', hash_function(partai))