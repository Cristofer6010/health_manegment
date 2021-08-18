print ("Enter Your Name : ")
name = input()
print ("What You Want Check (1 for Diet) and (2 for Exrcise) : ")
a = int(input())
def healthManegment(name,a):
        return
        if (name == "Harry" and a == 1 ):
                with open("harry_diet.txt") as f:
                        print (f.read())
        elif (name == "Harry" and a == 2  ):
                with open("harry_exrcice.txt") as g:
                        print (g.read())
        elif (name == "Hammad" and a == 1  ):
                with open("hammad_diet.txt") as h:
                        print (h.read())
        elif (name == "Hammad" and a == 2  ):
                with open("hammad_exrcice.txt") as i:
                        print (i.read())
        elif (name == "Rohan" and a == 1  ):
                with open("rohan_diet.txt") as j:
                        print (j.read())
        elif (name == "Rohan" and a == 2  ):
                with open("rohan_exrcice.txt") as k:
                        print (k.read())
        xyz = healthManegment(name,a)
        print (xyz)
