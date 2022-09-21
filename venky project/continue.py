#continue
#statement skip cheastundi
#example DON'T PRINT 3 DIVISIBLES FROM 1 TO 100
for i in range(1,101):
    if i%3==0:
        continue
    print(i)
    

#dont print 3 and 5 divisibles
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)

