class patterns:
    def pyramid(self,n):
        for i in range (n):
            for j in range(i):
                print("*",end=" ")
            print()
        for i in range(n):
            for j in range(n-i):
                print("*",end=" ")
            print()
p1=patterns()
p1.pyramid(5)