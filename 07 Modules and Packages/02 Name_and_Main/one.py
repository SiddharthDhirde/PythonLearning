def func():
    print("func() ran in one.py")

print("top-level print inside of one.py")

if __name__ == "__main__":
    print("__name__ in one: ", __name__)
    print("one.py is being run directly")
else:
    print("__name__ in one: ", __name__)
    print("one.py is being imported into another module")
