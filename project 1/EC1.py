print("Available movies today:")
print("A)12 Strong:    1)2:30  2)4:40  3)7:50  4)10:50")
print("B)Coco:         1)12:40 2)3:45")
print("C)The Post:     1)12:45 2)3:35  3)7:05  4)9:55")

ask1 = input("Movie choice:   ")



if ask1 == "A" or ask1 == "B" or ask1 == "C":
    ask2 = int(input("Showtime:       "))
    if  ask1 == "A" and ask2 < 5:
        ask3 = int(input("Adult tickets:  "))
        ask4 = int(input("Kid tickets:    "))
        if ask3 + ask4 >30:
            print("Invalid option; please restart app..." )
        else:
            price_for_adult = ask3 * 12.45
            price_for_kid = ask4 * 9.68
            total = price_for_adult + price_for_kid
            print(f"Total cost:     ${total:.2f}")        
    elif ask1 == "B" and ask2 < 3: 
        ask3 = int(input("Adult tickets:  "))
        ask4 = int(input("Kid tickets:    "))
        if ask3 + ask4 >30:
            print("Invalid option; please restart app..." )
        else:
            if ask2 == 1: 
                price_for_adult = ask3 * 11.17
                price_for_kid = ask4 * 8
                total = price_for_adult + price_for_kid
                print(f"Total cost:     ${total:.2f}")
            else:
                price_for_kid = ask4 * 9.68
                price_for_adult = ask3 * 12.45
                total = price_for_adult + price_for_kid
                print(f"Total cost:     ${total:.2f}")
        
    elif ask1 == "C" and ask2 < 5:
        ask3 = int(input("Adult tickets:  "))
        ask4 = int(input("Kid tickets:    "))
        if ask3 + ask4 >30:
            print("Invalid option; please restart app..." )
        else:
            if ask2 == 1 or ask2 == 2: 
                price_for_adult = ask3 * 11.17
                price_for_kid = ask4 * 8 
                total = price_for_adult + price_for_kid
                print(f"${total:.2f}")
            else: 
                price_for_adult = ask3 * 12.45
                price_for_kid = ask4 * 9.68
                total = price_for_adult + price_for_kid
                print(f"Total cost:     ${total:.2f}")
    else:
        print("Invalid option; please restart app..." )

        
else:
    print("Invalid option; please restart app..." )
               
