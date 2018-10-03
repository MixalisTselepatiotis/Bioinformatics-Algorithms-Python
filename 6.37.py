#                                        AN INTRODUCTION TO
#                                     BIOINFORMATICS ALGORITHMS
#                                NEIL C. JONES AND PAVEL A. PEVZNER
#########################################  Problem 6.37 #############################################
#                                          Problem 6.37                                             #
#  Devise an efficient algorithm for the chimeric alignment problem.                                #
#  A virus infects a bacterium, and modifies a replication process in the bacterium by inserting    #
#  at every A, a polyA of length 1 to 5.                                                            #
#  at every C, a polyC of length 1 to 10.                                                           #
#  at every G, a polyG of arbitrary length >= 1.                                                    # 
#  at every T, a polyT of arbitrary length >= 1.                                                    #
#  No gaps or other insertions are allowed in the virally modified DNA. For example, the sequence   #
#  AAATAAAGGGGCCCCCTTTTTTTCC is an infected version of ATAGCTC.                                     #  
#                                                                                                   #
#####################################################################################################

print("************* HELP **************") 
print(" ")
print("   A INFECTED VERSION OF DNA")
print("   AAATAAAGGGGCCCCCTTTTTTTCC")
print(" ")
print("************* START *************")
print(" ")
print(" ")

str = input("ENTER A INFECTED VERSION OF DNA :")
    
print("THE NON INFECTED VERSION OF DNA IS :")
            
countA = 0
countC = 0
countG = 0
countT = 0
    
for i in range(0, len(str)):

    
    if str[i] != 'A' and str[i] != 'C' and str[i] != 'G' and str[i] != 'T':
       print("\n" * 100)
       print("INVALID DNA FROM !")
       break
    

    if str[i] == 'A':		   
       countA += 1
       if countA > 5:
          print(" ")
          print("\n" * 100)
          print("INVALID DNA FROM !")
          print("At every A, a poly-A of length 1 to 5!")
          print(" ")   	  
          break
    
       if countA > 0 and countA <=1:
          print("A")
          countC = 0
          countG = 0
          countT = 0
          

    if str[i] == 'C':		  
       countC += 1
       if countC > 10: 	        
          print(" ")
          print("\n" * 100)
          print("INVALID DNA FORM !")
          print("At every C, a poly-C of length 1 to 10!")
          print(" ")
          break
        
       if countC > 0 and countC <= 1:
          print("C")
          countA = 0
          countG = 0
          countT = 0
          

    if str[i] == 'G':		  
       countG += 1
       if countG > 0 and countG <= 1 :
          print("G")
          countA = 0  
          countC = 0
          countT = 0    


    if str[i] == 'T':
       countT += 1;
       if countT > 0 and countT <= 1:
          print("T")
          countA = 0 
          countC = 0
          countG = 0 
		  
     
		     
	   
		 

        
   
