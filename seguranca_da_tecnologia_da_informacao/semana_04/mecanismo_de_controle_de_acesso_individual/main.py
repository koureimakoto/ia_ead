#!/usr/bin/env python3

import re
import auth

new_user = auth.User()

print("rst: ", re.findall(r'[\w\.-]+@[\w\.-]+\.[\w]+', 'koureimakoto@gmail.com') )

rslt = new_user.create_new_user("koureimakoto@gmail.com", "12345678")
print(rslt)

new_user.get_sign_user("koureimakoto@gmail.com", "12345678")
print("User: ", new_user)