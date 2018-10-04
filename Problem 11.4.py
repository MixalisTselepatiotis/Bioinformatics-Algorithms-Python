#                                        AN INTRODUCTION TO
#                                     BIOINFORMATICS ALGORITHMS
#                                NEIL C. JONES AND PAVEL A. PEVZNER
#########################################  Problem 11.4 #############################################
#                                                                                                   #
#                                          Problem 11.4                                             #
#    Figure 11.7 shows an HMM with two states a and b. When in the a state, it is more              #
#    likely to emit purines (A and G). When in the b state, it is more likely to emit pyrimidines   #
#    (C and T). Decode the most likely sequence of states (a/b) for sequence GGCT.                  #
#    Use log-scores, rather than straight probability scores.                                       #
#                                                                                                   #
#####################################################################################################                                           

#According to the 11.2 "The Fair Bet Casino and HiddenMarkovModels" Page -> 390

from random import randint

print("******************START****************") 
print(" ")
print("***************************************")
print("INSERT ONLY SEQUENCE IN FORM OF A/G/C/T")
print("***************************************")

c = [1,1,1,1,0,1,1,1,1,1]       
str = input("Enter the desired sequence:")

c_s = 'a'
t_pos = 0;
i = 0;  
error = 0;

print("The probable route is:")

while True:

   if i==0:             
      if str[0]=='A' or str[0]=='G':    
         t_pos += 0.4*0.5;
      elif str[0]=='T' or str[0]=='C':
         t_pos += 0.1*0.5;
      else:
         print("\n" *100)
         print("*************ERROR************")
         print("INVALID SEQUENCE FORM !")
         error = 1
         break                            
      i += 1    
      print(c_s)
   r = randint(0,9)
                  
   if c_s == 'a':
      if c[r] == 0:                   
         c_s = 'b'
      else: 
         c_s = 'a'   
   elif c_s == 'b':
      if c[r] == 0:
         c_s = 'a'
      else:
         c_s = 'b'                        
                                                                          
                                            
   if c[r] == 0:
      if c_s == 'b':
         print(c_s)
         if str[i]=='T' or str[i]=='C':
            t_pos *= 0.3*0.1
            i += 1   
         elif str[i]=='A' or str[i]=='G':
            t_pos *= 0.2*0.1
            i += 1                    
         else:
            print("\n" *100)
            print("*************ERROR************")
            print("INVALID SEQUENCE FORM !")
            error = 1
            break
      else:
         print(c_s)
         if str[i]=='T' or str[i]=='C':
            t_pos *= 0.1*0.1
            i += 1                        
         elif str[i]=='A' or str[i]=='G':
            t_pos *= 0.4*0.1
            i += 1                                           
         else:
            print("\n" *100)
            print("*************ERROR************")
            print("INVALID SEQUENCE FORM !")
            error = 1
            break         
         
   else:
      if c_s == 'a':
         print(c_s) 
         if str[i]=='A' or str[i]=='G':
            t_pos *= 0.4*0.9
            i += 1            
         elif str[i]=='T' or str[i]=='C':
            t_pos *= 0.1*0.9
            i += 1                        
         else:
            print("\n" *100)
            print("*************ERROR************")
            print("INVALID SEQUENCE FORM !")
            error = 1
            break
      else:
         print(c_s)
         if str[i]=='A' or str[i]=='G':
            t_pos *= 0.2*0.9
            i += 1                    
         elif str[i]=='T' or str[i]=='C':
            t_pos *= 0.3*0.9
            i += 1                        
         else:
            print("\n" *100)
            print("*************ERROR************")
            print("INVALID SEQUENCE FORM !")
            error = 1
            break

   if i == len(str):
      break

   
if error == 0: 
    print("The posibility of the route is: ", t_pos, " %") 

                
           
                
        
        


                                            
