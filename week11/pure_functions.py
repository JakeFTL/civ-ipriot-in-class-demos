
# %%
def some_func(a): # parameter
    b = 42
    print(b, "inside")

b = 100
some_func(42)
print(b, "outside")

# %%
def greet():
    print("Hello, World!")
greet()

# %%
def greet():
    return "Hello, World!"

print(greet())

# %%
import my_first_module as jake_math

print(jake_math.multiply(3, 2))