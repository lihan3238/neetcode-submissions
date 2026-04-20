class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count1=[0]*9
        count2=[0]*9
        count3=[0]*9
        team=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    count1[int(board[i][j])-1]+=1
                    if count1[int(board[i][j])-1]>1:
                        print("1",i,j,board[i][j])
                        return False
                if board[j][i]!=".":
                    count2[int(board[j][i])-1]+=1
                    if count2[int(board[j][i])-1]>1:
                        print("2",j,i,board[j][i])
                        return False

            for m,n in team:
                # print(i*3%9+1+m,((i*3)//9)*3+1+n,board[i*3%9+1+m][((i*3)//9)*3+1+n])
                if board[i*3%9+1+m][((i*3)//9)*3+1+n]!=".":
                    count3[int(board[i*3%9+1+m][((i*3)//9)*3+1+n])-1]+=1
                    if count3[int(board[i*3%9+1+m][((i*3)//9)*3+1+n])-1]>1:
                        print("3")
                        return False
            count1=[0]*9
            count2=[0]*9
            count3=[0]*9
        return True