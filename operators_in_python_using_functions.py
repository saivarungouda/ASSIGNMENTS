# 1. write a python program to calculate interst for the give principle amount i=ptr/100
def simple_interest():
    p=int(input("enter principle amount:"))
    t=int(input("enter time duraction:"))
    r=int(input("enter rate of interst:"))

    simple_intrest=p*t*r/100
    print("simple intrest:",simple_intrest)

# 2. write a python program to compute area and perimeter for a rectraingle
def area_and_perimeter():
    l=int(input("enter the length of the rectriangle:"))
    w=int(input("enter the wedth of the rectriangle:"))
    area=l*w
    print("area of the rectriangle of length",l,"and wiedth",w,"is:",area)
    perimeter=2*(l+w)
    print("perimeter of the rectriangle of length",l,"and wiedth",w,"is:",perimeter)

# 3. write a python program to convert celsius to fahrenheit
def temp_conversion():
    celsius=float(input("enter the temp in celsius:"))
    fehrenheit=(9/5)*celsius+32
    print(celsius,"degrees celsius is equal to",fehrenheit,"fehrenheit")

# 4. write a python program to compute spead using s=ut+1/2at^2 using functions

def compute_speed():
    u=float(input("enter the intial velocity:"))
    t=int(input("enter the time taken to cover the distance:"))
    a=float(input("enter the rate of accelaration:"))
    s=u*t+(1/2)*a*t**2
    print("speed",s)

# 5. write a python program to calculate BMI (body mass index) using functions concept
#formula BMI=weight in kgs/(height in meters)2

def BMI():
    weight=float(input("enter the weight:"))
    height=float(input("enter the height:"))
    bmi=weight/height*2
    print("Body Mass Index(BMI) is:",bmi)