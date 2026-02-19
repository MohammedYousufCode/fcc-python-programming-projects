#** start of main.py **

def verify_card_number(card_number):
    cleaned_card_number=card_number.replace("-","").replace(" ","")
    check_digit=int(cleaned_card_number[-1])
    without_last=cleaned_card_number[:-1]
    sum_of_digits=0
    for i, digit in enumerate(reversed(without_last)):
        n = int(digit)
        if i % 2 == 0:   # double every second digit
            n *= 2
            if n > 9:
                n -= 9
        sum_of_digits += n

    sum_of_digits+=check_digit
    if sum_of_digits%10==0:
        return "VALID!"
    else:
        return "INVALID!"
verify_card_number('4111-1111-1111-1111')      

        

#* end of main.py **

