'''import random
#*args for argumensts
def order(*args):
    order_num=random.randint(10,60)
    print(f"Order number {order_num}:")
    for item in args:
        print(f"Your order for {item} is placed")
    print("")
    print(" Your Order Number will be called soon")
    print("******Thankyou!******")

order("Pizza","Burger","Fries") '''

import random
# *args for arguments(are in tuples) / **kwargs for key=value arguments (arer in Key:value pairs)
def activity(*args,**kwargs):
    print(args)
    print(kwargs)

    min=sum(args)+random.randint(10,20)
    choice=random.choice(list(kwargs.values()))
    print(min)
    print(choice)
    print(f"Your have spent {min} minutes for {choice}")


 
activity(10,20,10, hobby="Gaming", work="Devops", like="Reading", sport="Football")
