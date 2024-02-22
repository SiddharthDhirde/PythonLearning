import one

print("top-level in two.py")

one.func()

if __name__ == "__main__":
    print("__name__ in two: ", __name__)
    print("two.py is being run directly")
else:
    print("__name__ in two: ", __name__)
    print("two.py is being imported into another module")
