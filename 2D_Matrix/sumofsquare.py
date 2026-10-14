def SumofSquare(num: int, sum: int) -> str:
    if sum > num * 9:
        return -1
    count_9 = sum // 9
    remainder = sum % 9
    if remainder > 0:
        count_0 = num - count_9 - 1
    else:
        count_0 = num - count_9
    final_string = "9" * count_9
    if remainder > 0:
        final_string += str(remainder)
    final_string += "0" * count_0
    return final_string


"""Step1: We will first check if the sum is greater than num*9 if yes than return -1
Step2: Now we will find out how many complete 9 can be used to maximise the output
Step3: we will find out the remainder which can be used to fill the remaining digits after using 9's
Step4: Now we will find out how many 0's can be used to fill the remaining digits
Step5: Now we will create the final string by adding 9's, remainder and 0's in that order and return the final string"""


print(SumofSquare(num=2, sum=17))
