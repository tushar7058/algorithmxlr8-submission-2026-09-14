def main():
    w = int(input())
    solve(w)



def solve(weight):
    if weight>2 and weight %2 ==0:
        print("YES")
    else:
        print("NO")
 
if __name__ == "__main__":
    main()
