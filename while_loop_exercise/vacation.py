needed_money = float(input())
money_on_hand = float(input())
spending_counter = 0
total_days_counter = 0
spending_to_many_days = False

while money_on_hand < needed_money:
    action = input()
    current_sum = float(input())
    total_days_counter += 1
    if action == "spend":
        spending_counter += 1
        if spending_counter == 5:
            spending_to_many_days = True
            break
        money_on_hand -= current_sum
        if money_on_hand < 0:
            money_on_hand = 0
    else:
        money_on_hand += current_sum
        spending_counter = 0

if spending_to_many_days:
    print("You can't save the money.")
    print(f"{total_days_counter}")
else:
    print(f"You saved the money for {total_days_counter} days.")
