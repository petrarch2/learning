j = { 'label_a': 1, 'label_b': 2, 'label_c': 3, 'label_d': 4 }
o = j.keys()
print( o )    # dict_keys(['label_a', 'label_b', 'label_c', 'label_d'])　と表示される
p = j.values()
print( p )    # dict_values([1, 2, 3, 4])　と表示される
for q in j.items():
	print( q )
"""
('label_a', 1)
('label_b', 2)
('label_c', 3)
('label_d', 4)
と表示される
"""
