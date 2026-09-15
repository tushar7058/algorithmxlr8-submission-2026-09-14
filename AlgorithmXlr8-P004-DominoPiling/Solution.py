def main():
    n, m = map(int, input().split())

    # 1. Brute force approach 

    # board = [[False]*m for _ in range(n)]
    # count = 0

    # for i in range(n):
    #     for j in range(m):
    #         if board[i][j]:
    #             continue
    #             # try to place a domino to the right , otherwise try to downword
    #         if j+1 < m and not board[i][j+1]:
    #             board[i][j] =  board[i][j+1] = True
    #             count +=1
    #         elif i +1 < n and not board[i+1][j]:
    #             board[i][j] = board[i+1][j] = True
    #             count +=1
    # print(count)


    # 2 . optimized approach
    print((n*m)//2)


if __name__ == "__main__":
    main()

