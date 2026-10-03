# .csv --> comma separated value
# .txt --> text file

# ey 'with' er maddhome kono file e ja eccha ta likha possible. er jonno alada file create kora lagbe na [with open] er moddhe j file er name dewa hobe seta ekai create hoye jabe

# ////
# with open('massage.txt', 'w') as file: # w -> write
#     file.write('I love you, python!')

# with open('massage.txt', 'a') as file: # a -> ekta value bar bar jog korbe emn ekta bishoy
#     file.write('I love you, python!')

with open('massage.txt', 'r') as file: # r -> eead kora. oi file e ki ki ache taie read kore dibe
    text = file.read()
    print(text)