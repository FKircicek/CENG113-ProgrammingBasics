#Fatih Kırçiçek 260201016

eq1_left_positives = []
eq1_left_negatives = []
eq1_right_positives = []
eq1_right_negatives = []
eq1 = input("Enter the first equation: \n")
eq2 = input("Enter the second equation: \n")
a = eq1.split("=")
eq1_left = a[0]
eq1_right = a[1]
b = eq1_left.split("+")
for i in b:
    c = list(i.split("-"))
    eq1_left_positives.append(c[0])
    for j in range(1,len(c)):
        eq1_left_negatives.append(c[j])
if eq1_left_positives[0] == "":
    eq1_left_positives.remove("")       
d = eq1_right.split("+")
for i in d:
    e = list(i.split("-"))
    eq1_right_positives.append(e[0])
    for j in range(1,len(e)):
        eq1_right_negatives.append(e[j])
if eq1_right_positives[0] == "":
    eq1_right_positives.remove("")

eq2_left_positives = []
eq2_left_negatives = []
eq2_right_positives = []
eq2_right_negatives = []

a = eq2.split("=")
eq2_left = a[0]
eq2_right = a[1]
b = eq2_left.split("+")
for i in b:
    c = list(i.split("-"))
    eq2_left_positives.append(c[0])
    for j in range(1,len(c)):
        eq2_left_negatives.append(c[j])
if eq2_left_positives[0] == "":
    eq2_left_positives.remove("")       
d = eq2_right.split("+")
for i in d:
    e = list(i.split("-"))
    eq2_right_positives.append(e[0])
    for j in range(1,len(e)):
        eq2_right_negatives.append(e[j])
if eq2_right_positives[0] == "":
    eq2_right_positives.remove("")

x_terms1 = []
y_terms1 = []
coefficients1 = []
for i in eq1_left_positives:
    if i.endswith("x"):
        x_terms1.append(i)
    elif i.endswith("y"):
        y_terms1.append(i)
    else:
        coefficients1.append(i)
for i in eq1_left_negatives:
    i = "-" + i
    if i.endswith("x"):
        x_terms1.append(i)
    elif i.endswith("y"):
        y_terms1.append(i)
    else:
        coefficients1.append(i)
for i in eq1_right_positives:
    i = "-" + i
    if i.endswith("x"):
        x_terms1.append(i)
    elif i.endswith("y"):
        y_terms1.append(i)
    else:
        coefficients1.append(i)
for i in eq1_right_negatives:
    if i.endswith("x"):
        x_terms1.append(i)
    elif i.endswith("y"):
        y_terms1.append(i)
    else:
        coefficients1.append(i)
x_terms2 = []
y_terms2 = []
coefficients2 = []
for i in eq2_left_positives:
    if i.endswith("x"):
        x_terms2.append(i)
    elif i.endswith("y"):
        y_terms2.append(i)
    else:
        coefficients2.append(i)
for i in eq2_left_negatives:
    i = "-" + i
    if i.endswith("x"):
        x_terms2.append(i)
    elif i.endswith("y"):
        y_terms2.append(i)
    else:
        coefficients2.append(i)
for i in eq2_right_positives:
    i = "-" + i
    if i.endswith("x"):
        x_terms2.append(i)
    elif i.endswith("y"):
        y_terms2.append(i)
    else:
        coefficients2.append(i)
for i in eq2_right_negatives:
    if i.endswith("x"):
        x_terms2.append(i)
    elif i.endswith("y"):
        y_terms2.append(i)
    else:
        coefficients2.append(i)
sum_of_x1 = 0
sum_of_y1 = 0
sum_of_coefficients1 = 0
       
for i in x_terms1:
    i = i.replace("x","")
    i = int(i)
    sum_of_x1 += i
print(sum_of_x1)
for i in y_terms1:
    i = i.replace("y","")
    i = int(i)
    sum_of_y1 += i    
print(sum_of_y1)    
for i in coefficients1:
    i = int(i)    
    sum_of_coefficients1 += i    

print("Equations in the simplified form:")
if sum_of_y1 >= 0:
    print(str(sum_of_x1) + "x","+ " + str(sum_of_y1) + "y =",-1*sum_of_coefficients1)
else:    
    print(str(sum_of_x1) + "x",str(sum_of_y1) + " y =",-1*sum_of_coefficients1)
    
sum_of_x2 = 0
sum_of_y2 = 0
sum_of_coefficients2 = 0

for i in x_terms2:
    i = i.replace("x","")
    i = int(i)
    sum_of_x2 += i
for i in y_terms2:
    i = i.replace("y","")
    i = int(i)
    sum_of_y2 += i        
for i in coefficients2:
    i = int(i)    
    sum_of_coefficients2 += i    

if sum_of_y2 >= 0:
    print(str(sum_of_x2) + "x","+ " + str(sum_of_y2) + "y =",-1*sum_of_coefficients2)
else:    
    print(str(sum_of_x2) + "x","- " + str(-1*sum_of_y2) + "y =",-1*sum_of_coefficients2)    
x11 = -1*sum_of_x1
y11 = sum_of_y1
co11 = sum_of_coefficients1
co22 = sum_of_coefficients2
x1 = sum_of_x1*sum_of_x2
y1 = sum_of_y1*sum_of_x2
co1 = sum_of_coefficients1*sum_of_x2
x2 = sum_of_x2*x11
y2 = sum_of_y2*x11
co2 = sum_of_coefficients2*x11
y = y1+y2
co = co1+co2
co = co/y  
x = (co22-(sum_of_y2*co))/sum_of_x2
print("Solution:\n","x =",int(-x),"\n y =",int(-co) )