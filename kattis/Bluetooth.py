Dict = {"m": 1,"b": 2}

num_dict = {"+1": 0,"+2": 1,"+3": 2,"+4": 3,"+5": 4,"+6": 5,"+7": 6,"+8": 7,
            "1+": 8,"2+": 9,"3+": 10,"4+": 11,"5+": 12,"6+": 13,"7+": 14,"8+": 15,
            "-1": 16,"-2": 17,"-3": 18,"-4": 19,"-5": 20,"-6": 21,"-7": 22,"-8": 23,
            "1-": 24,"2-": 25,"3-": 26,"4-": 27,"5-": 28,"6-": 29,"7-": 30,"8-": 31,}

master_list = [0 for i in range(32)]
 
problems_num = int(input())

for i in range(problems_num):
    tooth_num, problem = input().split()
    master_list[num_dict[tooth_num]] = Dict[problem]

if (2 in master_list[8:16]) == False and (2 in master_list[24:32]) == False and (0 in master_list[8:16]) == True and (0 in master_list[24:32]) == True:
    print(1)
elif (2 in master_list[0:8]) == False and (2 in master_list[16:24]) == False and (0 in master_list[0:8]) == True and (0 in master_list[16:24]) == True:
    print(0)
else:
    print(2)





    


