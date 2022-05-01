# 조건문 기본
# if xxx :   - 여기가 true 이면
#     yyy  - 여기가 실행이 된다.

user_id = input('id?')
user_pwd = input('password?')
'''
if user_pwd =='111111':
    print('hello master')
else:
    print('who are you?')
'''
if user_id == 'egoing':
    if user_pwd =='111111':
        print('hello master')
    else:
        print('who are you?')
else:
    print('who are you?')

# 조건문 중복사용 가능