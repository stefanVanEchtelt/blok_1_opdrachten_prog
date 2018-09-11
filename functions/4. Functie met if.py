def new_password(oldpassword, newpassword):
    return oldpassword != newpassword and len(newpassword) >= 6 and newpassword.isalpha() == False

print(new_password('stefan123', 'stefan123'))
print(new_password('stefan123', 'stefa'))
print(new_password('stefan123', 'stefan'))
print(new_password('stefan123', 'stefan12345'))
