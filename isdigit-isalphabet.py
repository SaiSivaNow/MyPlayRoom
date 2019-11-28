
input_str=input()

my_dict={'LETTERS':0,'NUMBERS':0}

for char in input_str:
    if char.isdigit():
        my_dict['NUMBERS']+=1;
    elif char.isalpha():
        my_dict['LETTERS']+=1;


for x,y in my_dict.items():
    print(x,y)
