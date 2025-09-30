import matplotlib.pyplot as plt

def sieve_of_eratosthenes(limit):
    """Find all primes up to limit using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    return [num for num, prime in enumerate(is_prime) if prime]

def count_primes_by_thousands(primes, max_val):
    """Count primes in each 1000-number range."""
    ranges = list(range(0, max_val + 1, 1000))
    counts = [0] * (len(ranges) - 1)
    
    for prime in primes:
        bucket = prime // 1000
        if bucket < len(counts):
            counts[bucket] += 1
    
    return ranges[:-1], counts

# Generate primes and count them
primes = sieve_of_eratosthenes(100000)
range_starts, counts = count_primes_by_thousands(primes, 100000)

# Define 10 colors to cycle through
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Plot and save
plt.figure(figsize=(10, 6))
bar_colors = [colors[i % 10] for i in range(len(range_starts))]
plt.bar(range_starts, counts, width=800, align='edge', edgecolor='black', color=bar_colors)
plt.xlabel('Range Start')
plt.ylabel('Number of Primes')
plt.title('Prime Distribution by Thousands (1-100000)')
plt.xticks(range(0, 100001, 10000))
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('prime_distribution.png', dpi=300)
print("Figure saved as 'prime_distribution.png'")