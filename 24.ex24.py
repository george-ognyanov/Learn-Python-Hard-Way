print('lets pratcise everything.')
print('you\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t the lovely world
with logic so firmly planted
cannot discern \n the need of love
nor comprehend passion from intuition
and requires and explanation
\n\t where there is none.
"""

print('----------')
print(poem)
print('----------')


five = 10-2+3-6
print(f'this shoud be five: {five}')

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print('with a starting point of: {}'.format(start_point))
#its just like with an f"" string
print(f'wed have {beans} beans, {jars} jars and {crates} crates.')

start_point = start_point / 10

print('we can also do that this way:')
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print('wed have {} beans, {} jars and {} crates'.format(*formula))