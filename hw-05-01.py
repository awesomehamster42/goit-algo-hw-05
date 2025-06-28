def caching_fibonacci():
    cache = {}    # Створюємо словник для кешування обчисленних значень

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]    # Значення з кешу, яке вже обчислили
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)    # Рекурсивне обчислення і кешування
        return cache[n]
    
    return fibonacci