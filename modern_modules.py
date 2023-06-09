
import random
def activity(*args,**kwargs):
    print(args)
    print(kwargs)

    min=sum(args)+random.randint(10,20)
    choice=random.choice(list(kwargs.values()))
    print(min)
    print(choice)
    print(f"Your have spent {min} minutes for {choice}")


def order(*args):
    order_num=random.randint(10,60)
    print(f"Order number {order_num}:")
    for item in args:
        print(f"Your order for {item} is placed")
    print("")
    print(" Your Order Number will be called soon")
    print("******Thankyou!******")



def Player( name, state, age):
    print("List of Players")
    print(f"{name}, age {age} is from {state}.")