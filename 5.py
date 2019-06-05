
str = '193a'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()
