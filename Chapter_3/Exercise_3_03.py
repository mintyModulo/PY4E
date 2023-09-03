# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following tables:
#  Score     Grade
# >= 0.9       A
# >= 0.8       B
# >= 0.7       C
# >= 0.6       D
#  < 0.6       F

score = input("Enter a score between 0.0 and 1.0: ")

try:    
    final_score = float(score)
except:
    print('Bad score')
    quit()

if final_score > 1.0 or final_score < 0.0 :
    print('Bad score')
    quit()
elif final_score >= 0.9:
    print('A')
elif final_score >= 0.8:
    print('B')
elif final_score >= 0.7:
    print('C')
elif final_score >= 0.6:
    print('D')
else:
    print('F')