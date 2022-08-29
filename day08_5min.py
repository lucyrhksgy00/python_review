"""
    1. 유저로부터 전화번호를 받는다.
    2. 전화번호가 숫자와 '-'로만 구성이 되어 있는지 체크
    3. 정상이면 숫자가 10자리 또는 11자리인지 체크
    4. 정상이면 10자리면 XXX, XXX, XXXX return
               11자리면 XXX, XXXX, XXXX return
    5. 비정상이면 999, 9999, 9999 return
"""
def checkPhoneNumber(str):
    nstring = ''

    # 1. 숫자와 '-'만으로 구성되어 있는지 체크
    for c in str:
        if c in "0123456789-":
            if c == '-':
                pass
            else:
                nstring += c
        else:
            return 999, 9999, 9999

    # 2. 숫자가 10자리 또는 11자리인지 체크
    if len(nstring) == 10:
        return nstring[0:3], nstring[3:6], nstring[6:]
    elif len(nstring) == 11:
        return nstring[0:3], nstring[3:7], nstring[7:]
    else:
        return 999, 9999, 9999

a, b, c = checkPhoneNumber("011-345-2561")
print(a, b, c)

a, b, c = checkPhoneNumber("010-2214-2561")
print(a, b, c)

a, b, c = checkPhoneNumber("PPP")
print(a, b, c)