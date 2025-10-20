import timeit
from nanograz.example import square

# Global variable scope timing
start = timeit.default_timer()
for i in range(10000000):
    square(i)
end = timeit.default_timer()
print(f"Global: {end - start} seconds")


# Local variable scope timing
def main():
    for i in range(10000000):
        square(i)


if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print(f"Local: {end - start} seconds")
