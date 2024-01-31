def password_level(user_pass):

    check_len = True if len(user_pass)>8 else False
    check_reg_up = True if True in [i.isupper() for i in user_pass] else False
    check_reg_low = True if True in [i.islower() for i in user_pass] else False
    both_reg = (check_reg_up and check_reg_low)
    check_digits = True if True in [i.isdigit() for i in user_pass] else False
    check_dog = not set('@#$%&*().,-_+').isdisjoint(user_pass)
    
    
    # print(f'{check_reg_up=}')
    # print(f'{check_reg_low=}')
    # print(f'{both_reg=}')
    # print(f'{check_digits=}')
    # print(f'{check_dog=}')
    
    
    if not check_len:
        return 'Недопустимый пароль'
    if not both_reg or (check_digits and not both_reg):
        return 'Ненадёжный пароль'
    if (both_reg and not check_digits) or ((check_reg_low or check_reg_up) and check_digits):
        if check_dog:
            return 'Надежный пароль' 
        return "Слабый пароль"
    
        

# psw = input()
psw = '213352135aA@'
a = password_level(psw)
print(a)