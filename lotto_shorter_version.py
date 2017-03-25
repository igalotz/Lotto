import random

    
def lotto():
    pull = list(range(1,50))
    #print("Pull: ",pull)
    result = []
    for i in range(0,6):
        number = random.choice(pull)
        pull.remove(number)
        result.append(number)
    return sorted(result)

def check_coupon(number, coupon):
    return True if number in coupon else False

coupon = []
number = 0 

while len(coupon) < 6:
    x = input("Wybierz liczbę[1-49]: ")
    try:
        number = int(x)
    except:
        print ("to nie jest liczba")
        
    if (number < 1 or number > 49) or ( number in coupon):
        print("Zła liczba")
    else:
        coupon.append(number)
        print("Wybrałeś: ", sorted(coupon))
    

coupon.sort()
score = lotto()

print("Wybrałeś liczby:", coupon)
print("Wylosowano liczby:", score)

hits = 0
for number in coupon:
    if check_coupon(number, score):
        hits += 1

if hits > 2:        
    print("Trafiłes", hits, "liczb")
else:
    print("Nic nie wygrałeś")


















