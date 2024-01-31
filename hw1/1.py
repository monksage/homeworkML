k = int(input())
nums = []
for i in range(k):
    nums.append(int(input()))
nums.sort(reverse=True)
print('Reverse sorted nums')
for num in nums:
    print(num)