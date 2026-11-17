username = "hussein"
failed_attempts = 4

if failed_attempts > 5 and username == "admin":
    print("ALERT:possible attack on the admin account")
elif failed_attempts > 3:
    print("too many attempts: lock the account")
else:
    print("login attempts are normal")