from random import randint


first_number = randint(1, 9)
secand_number = randint(1, 9)


print(f'How much is {first_number} * {secand_number} ?')
user_answer = int(input('Enter your answer: '))


def get_correct_number(a, b):
    return  a * b    
correct_number = get_correct_number(first_number, secand_number)



if correct_number is user_answer:
    print('Correct.' )
else:
    print(f'Wrong. Correct answer is {correct_number}')

