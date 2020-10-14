def palindrome(st):
    st = st.replace(' ', '').lower()
    return 'Палиндром' if st == st[::-1] else 'Не палиндром'


print(palindrome('12321'))
print(palindrome('Палиндром'))
