input_path = 'input4.txt'
output_path = 'output4.txt'

def minNumbCoins(coins, totalAmount):
    dp = [float('inf')] * (totalAmount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, totalAmount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[totalAmount] != float('inf'):
        return dp[totalAmount]
    else:
        return -1



with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    n, x = list(map(int, input_file.readline().split(" ")))
    coins = list(map(int, input_file.readline().split(" ")))
    result = minNumbCoins(coins, x)
    output_file.write(str(result) + "\n")