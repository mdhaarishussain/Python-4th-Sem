import random
import math
import statistics

def generate_random_numbers(n):
    random_numbers = [random.randint(1, 1000) for _ in range(n)]
    return random_numbers

def logarithmic_transformation(data):
    transformed_data = [math.log(x) for x in data]
    return transformed_data

def calculate_statistics(data):
    min_val = min(data)
    max_val = max(data)
    mean_val = sum(data) / len(data)
    median_val = statistics.median(data)
    mode_val = statistics.mode(data)
    std_dev = statistics.stdev(data)
    return min_val, max_val, mean_val, median_val, mode_val, std_dev

def main():
    n = int(input("Enter the number of random numbers to generate: "))
    random_numbers = generate_random_numbers(n)

    # Apply logarithmic transformation
    transformed_numbers = logarithmic_transformation(random_numbers)

    # Calculate statistics before transformation
    print("Statistics before transformation:")
    before_min, before_max, before_mean, before_median, _, before_std_dev = calculate_statistics(random_numbers)
    print(f"Minimum: {before_min}")
    print(f"Maximum: {before_max}")
    print(f"Mean: {before_mean}")
    print(f"Median: {before_median}")
    # Mode calculation is removed as it is not applicable for continuous data
    print(f"Standard Deviation: {before_std_dev}")

    # Calculate statistics after transformation
    print("\nStatistics after transformation:")
    after_min, after_max, after_mean, after_median, _, after_std_dev = calculate_statistics(transformed_numbers)
    print(f"Minimum: {after_min}")
    print(f"Maximum: {after_max}")
    print(f"Mean: {after_mean}")
    print(f"Median: {after_median}")
    # Mode calculation is removed as it is not applicable for continuous data
    print(f"Standard Deviation: {after_std_dev}")

if __name__ == "__main__":
    main()
