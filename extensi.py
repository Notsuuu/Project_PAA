import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value=100, seed=None):
    if seed is not None:
        random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(array):
    seen = set()
    for num in array:
        if num in seen:
            return False
        seen.add(num)
    return True

def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time

def measure_average_time(func, *args, runs=5):
    times = [measure_time(func, *args) for _ in range(runs)]
    return sum(times) / len(times)

def main():
    ns = [100, 150, 200, 250, 300, 350, 400, 500]
    max_value = 250 - 82

    worst_case_times = []
    average_case_times = []

    for n in ns:
        validate_input(n, max_value)
        array = generate_array(n, max_value)
        worst_case_array = [1] * n

        worst_case_time = measure_average_time(is_unique, worst_case_array)
        average_case_time = measure_average_time(is_unique, array)

        worst_case_times.append(worst_case_time)
        average_case_times.append(average_case_time)

        print(f"n = {n}, Worst Case Time = {worst_case_time:.10f}s, Average Case Time = {average_case_time:.10f}s")

    plt.figure(figsize=(10, 6))
    plt.plot(ns, worst_case_times, marker='o', label='Worst Case', color='red', linestyle='--')
    plt.plot(ns, average_case_times, marker='s', label='Average Case', color='blue', linestyle='-.')
    plt.title('Performance Comparison: Worst Case vs Average Case', fontsize=14)
    plt.xlabel('Array Size (n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True)
    plt.show()

def validate_input(n, max_value):
    if n <= 0:
        raise ValueError("Array size (n) must be greater than 0.")
    if max_value <= 0:
        raise ValueError("Maximum value must be greater than 0.")

if __name__ == "__main__":
    main()
