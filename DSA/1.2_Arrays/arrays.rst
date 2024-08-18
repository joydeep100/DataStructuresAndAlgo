Ammo

- Sorting
- HashMap
- 2 Pointers

say n = [1,2,1,1] then valid pairs of 1 are (1,1), (1,1) & (1,1)
Valid Pairs = Try (n*(n-1))/2 for a given char frequency n

- When checking for pointers not going out of bounds first keep 
the check and then then other condition

.. Example
```
while (i < len(name) and name[i] == typed[k]):
    .. instead of 
while (name[i] == typed[k] and i < len(name)):
```