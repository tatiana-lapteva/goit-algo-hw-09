
import timeit
from collections import Counter


def find_coins_greedy(n: int, coins: list) -> dict:
    """ Функція жадібного алгоритму """

    """
    Ця функція повинна приймати суму, яку потрібно видати покупцеві, і повертати словник 
    із кількістю монет кожного номіналу, що використовуються для формування цієї суми. 
    Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен 
    бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.
    """
    res = []
    coins.sort(reverse=True)
    for coin in coins:
        while n >= coin:
            n -= coin
            res.append(coin)
    return dict(Counter(res))


def find_min_coins(n: int, coins: list) -> dict:
    """
    Функція динамічного програмування. 
    Ця функція також повинна приймати суму для видачі решти, але використовувати метод 
    динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для 
    формування цієї суми. Функція повинна повертати словник із номіналами монет та їх 
    кількістю для досягнення заданої суми найефективнішим способом. Наприклад, для суми 
    113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}
    """

    if n == 0:
        return 0
    
    result = {}
    #coins.sort(reverse=True)
    
    mem = [float('inf')] * (n + 1)
    mem[0] = 0     

    coin_used = [0] * (n + 1)

    for coin in coins:
        for i in range(coin, n + 1):
            if mem[i - coin] + 1 < mem[i]:
                mem[i] = mem[i - coin] + 1
                coin_used[i] = coin

    while n > 0:
        coin = coin_used[n]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        n -= coin

    return result



def measure_time(function, n: int, coins: list):
    start = timeit.default_timer()
    result = function(n, coins)
    
    return result, timeit.default_timer() - start



if __name__ == "__main__":

    coins = [50, 25, 10, 5, 2, 1]

    greedy_result, greedy_time = measure_time(find_coins_greedy, 113, coins)       
    print(f"Результат жадібного алгоритму для суми 113: {greedy_result}")
    print(f"Час виконання жадібного алгоритму: {greedy_time:.5f}")

    dynamic_result, dynamic_time = measure_time(find_min_coins, 113, coins)
    print(f"Результат динамічного програмування для суми 113: {dynamic_result}")
    print(f"Час виконання динамічного програмування: {dynamic_time:.5f}")

    greedy_result, greedy_time = measure_time(find_coins_greedy, 9999, coins)       
    print(f"Результат жадібного алгоритму для суми 9999: {greedy_result}")
    print(f"Час виконання жадібного алгоритму: {greedy_time:.5f}")

    dynamic_result, dynamic_time = measure_time(find_min_coins, 9999, coins)
    print(f"Результат динамічного програмування для суми 9999: {dynamic_result}")
    print(f"Час виконання динамічного програмування: {dynamic_time:.5f}")