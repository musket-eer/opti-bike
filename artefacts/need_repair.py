class need_repair:
    def __init__(self):
        self.needs_repair = False
        self.locked = False

    def press_repair_button(self):
        self.needs_repair = True
        self.locked = True

    def unlock(self, admin_password):
        if admin_password == "admin123":
            self.locked = False
        else:
            print("Unauthorized access. Only the admin can unlock the bike.")

# Example usage:
bike = need_repair()
bike.press_repair_button()
print(bike.needs_repair)  # Output: True
print(bike.locked)  # Output: True

bike.unlock("admin123")
print(bike.locked)  # Output: False

bike.unlock("wrong_password")  # Output: Unauthorized access. Only the admin can unlock the bike.
