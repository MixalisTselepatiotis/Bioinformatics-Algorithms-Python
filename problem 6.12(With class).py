#                                 AN INTRODUCTION TO
#                             BIOINFORMATICS ALGORITHMS
#                         NEIL C. JONES AND PAVEL A. PEVZNER
################################  Problem 6.12 ######################################
#                                 Problem 6.12                                      #
#  Two players play the following game with two “chromosomes” of length n and m     #
#  nucleotides. At every turn a player can destroy one of the chromosomes and break #
#  another one into two nonempty parts. For example, the first player can destroy a # 
#  chromosome of length n and break another chromosome into two chromosomes of      #
#  length m/3 and m − m/3 . The player left with two single-nucleotide chromosomes  #
#  loses. Who will win? Describe the winning strategy for each n and m.             #  
#                                                                                   #
#####################################################################################


class exercise_12:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        matrix = []
        
    def FillMatrix(self):
        
        matrix = [[0 for x in range(self.m)] for y in range (self.n)]
        matrix[0][0] = "L";

        
        for i in range(1, self.n) :
            if matrix[i - 1][0] == "L" :
                matrix[i][0] = "W"
            else:
                matrix[i][0] = "L"
                
                
        for j in range(1, self.m) :
           if matrix[0][j - 1] == "L" :
               matrix[0][j] = "W"
           else :
               matrix[0][j] = "L"
               
               
        for i in range(1, self.n) :
            for j in range(1, self.m) :
                if matrix[i - 1][j - 1] == "W" and matrix[i - 1][j] == "W" and matrix[i][j - 1] == "W" :
                    matrix[i][j] = "L"
                else : 
                    matrix[i][j] = "W"

                 
        for i in range(0,i+1):         
            print (matrix[i], " ") 
               
   
        if matrix[self.n - 1][self.m - 1] == "L" :
            print("Player 1 loses.")
        else :
            print("Player 1 wins.")
                       
         
            
a = int(input("Give a number:"))        
b = int(input("Give an another:"))

ex1 = exercise_12(a,b)
ex1.FillMatrix()






