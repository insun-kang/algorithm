
def maxSubArray(nums):
    ans=[0]*len(nums)
    
    ans[0]=nums[0]
    
    for i in range(1, len(nums)):
        ans[i]=max(0, ans[i-1])+nums[i]
    print(ans)
    return max(ans)
    


def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -2, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()