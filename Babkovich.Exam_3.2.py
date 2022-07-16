# 2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково слева-направо и справа-налево.
# Иначе – False.
def func(text):
    print(text == text[::-1])
    
text = func
text(input("Enter text: "))