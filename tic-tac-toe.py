def suma(a , b, c):
   return a + b + c

def printboard(xstate,zstate):
 zero = 'X' if xstate[0] else ('O' if zstate[0] else " ")
 one = 'X' if xstate[1] else ('O' if zstate[1] else " ")
 two = 'X' if xstate[2] else ('O' if zstate[2] else " ")
 three = 'X' if xstate[3] else ('O' if zstate[3] else " ")
 four = 'X' if xstate[4] else ('O' if zstate[4] else " ")
 five = 'X' if xstate[5] else ('O' if zstate[5] else " ")
 six = 'X' if xstate[6] else ('O' if zstate[6] else " ")
 seven = 'X' if xstate[7] else ('O' if zstate[7] else " ")
 eight = 'X' if xstate[8] else ('O' if zstate[8] else " ")
 nine = 'X' if xstate[9] else ('O' if zstate[9] else " ")

 print("+-----------+")
 print(f"| {one} | {two} | {three} |")
 print("+-----------+")
 print(f"| {four} | {five} | {six} |")
 print("+-----------+")
 print(f"| {seven} | {eight} | {nine} |")
 print("+-----------+")

 
def checkwin(xstate,zstate):
   wins = [[1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7]]
   for win in wins:
    if(suma(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
        print("X wins")
        return 1
    if(suma(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3):
        print("O wins")
        return 0
   return -1
if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    turn = 1 # 1 for x and 0 for o
    print("welcome to tic tac toe")
    print("X's chance")

    while(True):
       printboard(xstate,zstate)
       if(turn == 1):
          print("x's chance")
          value = int(input("please enter value: "))
          xstate[value] = 1
       else:
         print("O's chance")
         value = int(input("please enter value: "))
         zstate[value] = 1
       
       cwin = checkwin(xstate,zstate)
       if(cwin!= -1):
          printboard(xstate,zstate)
          print("game over")
          break
       turn = 1- turn 
 