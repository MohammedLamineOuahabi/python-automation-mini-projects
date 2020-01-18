import os
#get infos from windows user variable
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

print(EMAIL_USER)
print(EMAIL_PASS)