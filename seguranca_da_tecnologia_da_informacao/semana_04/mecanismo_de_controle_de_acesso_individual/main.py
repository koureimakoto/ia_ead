#!/usr/bin/env python3

import re
import auth

new_user = auth.User()

new_user.create_new_user("urei@gmail.com", "#$Talles1234")
print(new_user.check_passwd("Oii$AOPALS"))