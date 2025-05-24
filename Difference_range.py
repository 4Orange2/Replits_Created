test_case = int(input("number that you want to test? "))
time_beatrice = 60*2/test_case
time_hieu = 8
dr = time_beatrice - time_hieu
print((dr*(60-dr) + (((dr - 1)*dr)/2))/(60*60))
