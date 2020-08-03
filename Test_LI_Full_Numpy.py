# import pandas as pd
import os
import re
import math
import time
import numpy as np

start = time.time()

#get data from csv file
fileLIBase_np = np.genfromtxt(os.getcwd() +"\\LI Base full.csv" , usecols=np.arange(0,398), delimiter=",", names=True)
fileLITest_np = np.genfromtxt(os.getcwd() + "\\LI Test full.csv", usecols=np.arange(0,398), delimiter=",", names=True)

sum_diff = 0
col_title = []
total_cnt_list = []
diff_cnt_list = []
up_cnt_list = []
down_cnt_list = []
diff_pct_list = []
up_pct_list = []
down_pct_list = []
matched_list = []
mean_Base_list = []
mean_Test_list = []
standard_dv_list_Base = []
standard_dv_list_Test = []
change_standard_dv = 0
change_standard_dv_list = []
character_str_count_list_Base = []
character_str_count_list_Test = []
blank_list_Base = []
blank_list_Test = []

#get column title
for title in fileLIBase_np.dtype.names:
    col_title.append(title)

# use for loop through whole columns. len(fileLIBase_np.dtype.names)to get number of columns
######################################################################################################################
for col in range(len((fileLIBase_np.dtype.names))):
    # get all rows for each column.
    colBase = fileLIBase_np[fileLIBase_np.dtype.names[col]]
    colTest = fileLITest_np[fileLITest_np.dtype.names[col]]
    count = 0
    diff = 0
    up_count = 0
    down_count = 0
    matched = 0
    sum_totalBase = 0.0
    sum_totalTest = 0.0
    standard_dv_Base = 0
    row_BaseValue = []
    square_BaseValue = []
    item = []
    character_str_count_Base = 0
    character_str_count_Test = 0
    blank_Base = 0
    blank_Test = 0

    #len(colBase) get number of rows.
    # use for loop to get each row.
    for row in range(len(colBase)):
        if (type(colBase[row]) != str and not math.isnan(colBase[row])):
            sum_totalBase += colBase[row]
        if (type(colTest[row]) != str and not math.isnan(colTest[row])):
            sum_totalTest += colTest[row]

        if(type(colBase[row]) != str and math.isnan(colBase[row])):
            blank_Base += 1
        if (colBase[row] == "" and colBase[row] == ""):
            blank_Base += 1
        if (type(colTest[row]) != str and math.isnan(colTest[row])):
            blank_Test += 1
        if (colTest[row] == "" and colTest[row] == ""):
            blank_Test += 1

        if (type(colBase[row]) == str):
            get_char_Base = re.split(',|;', colBase[row])
            character_str_count_Base += len(get_char_Base)

        if (type(colTest[row]) == str):
            get_char_Test = re.split(',|;', colTest[row])
            character_str_count_Test += len(get_char_Test)

        if (colBase[row] == colTest[row]):
            matched += 1
        elif (colBase[row] != "" and colTest[row] == ""):
             diff += 1
        elif (colBase[row] == "" and colTest[row] != ""):
            diff += 1
        else:
            if (colBase[row] != colTest[row]):
                diff += 1

            if(type(colBase[row]) == type(colTest[row])):
                if (colBase[row] > colTest[row]):
                    up_count += 1
                elif (colBase[row] < colTest[row]):
                    down_count += 1

        sum_diff += diff
        count += 1

        # if (count >= 10):
        #     break
    # end for (row)
    ######################################################################################################################

    diff_pct = (100 * diff / count)
    up_pct = (100 * up_count / count)
    down_pct = (100 * down_count / count)


    #check file Base. if type of first row is string, then mean_Base and standard_dv_base is empty.
    if (type(colBase[0]) == str):
        mean_Base = ""
        standard_dv_Base = ""
    # if typpe of colbase is int or float then calculate mean each column.
    else:
        mean_Base = sum_totalBase/count
        sum_dev = 0
        for i in range(count):
            value = colBase[i]
            if(type(value) != str and not math.isnan(value)):
                sum_dev += (value - mean_Base) ** 2
        standard_dv_Base = math.sqrt(sum_dev / count)

    #check file Test.
    if (type(colTest[0]) == str):
        mean_Test = ""
        standard_dv_Test = ""
    else:
        mean_Test = sum_totalTest / count
        sum_dev = 0
        for i in range(count):
            value = colTest[i]
            if (type(value) != str and not math.isnan(value)):
                sum_dev += (value - mean_Base) ** 2
        standard_dv_Test = math.sqrt(sum_dev / count)

    if (standard_dv_Base == "" or standard_dv_Test == ""):
        change_standard_dv = ""
    else:
        change_standard_dv = standard_dv_Base - standard_dv_Test

    total_cnt_list.append(count)
    diff_cnt_list.append(diff)
    up_cnt_list.append(up_count)
    down_cnt_list.append(down_count)
    diff_pct_list.append(diff_pct)
    up_pct_list.append(up_pct)
    down_pct_list.append(down_pct)
    matched_list.append(matched)
    mean_Base_list.append(mean_Base)
    mean_Test_list.append(mean_Test)
    standard_dv_list_Base.append(standard_dv_Base)
    standard_dv_list_Test.append(standard_dv_Test)
    change_standard_dv_list.append(change_standard_dv)
    character_str_count_list_Base.append(character_str_count_Base)
    character_str_count_list_Test.append(character_str_count_Test)
    blank_list_Base.append(blank_Base)
    blank_list_Test.append(blank_Test)
# end for(col)
######################################################################################################################

row_title = ['Field','Total_cnt','Diff_cnt','Diff_pct', 'Up_cnt',
             'Up_pct','Down_cnt','Down_pct','Matched','Mean_Base',
             'Mean_Test','Standard_dev_Base','Standard_dev_Test','Change_standard_dev','Char_str_count_Base',
             'Char_str_count_Test',  'Blank_Base', 'Blank_Test']
results = [col_title ,total_cnt_list, diff_cnt_list, diff_pct_list,
           up_cnt_list, up_pct_list, down_cnt_list, down_pct_list,
           matched_list, mean_Base_list, mean_Test_list,
           standard_dv_list_Base, standard_dv_list_Test,
           change_standard_dv_list,
           character_str_count_list_Base,
           character_str_count_list_Test,
           blank_list_Base,
           blank_list_Test]
results = np.c_[row_title, results]
results = results.transpose()
# print(results)
write_np = np.savetxt('expprt_LI_numpy.csv', results, delimiter=',', fmt="%s")

print(time.time() - start)
# it takes 197 seconds