import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"تابع {func.__name__} در {end-start:.4f} ثانیه اجرا شد")
        return result
    return wrapper

@timer
def compute_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(compute_sum(1000000))
