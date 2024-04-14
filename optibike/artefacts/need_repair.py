class BikeRepair:
    needs_repair = False
    locked = False

    @classmethod
    def press_repair_button(cls):
        cls.needs_repair = True
        cls.locked = True

    @classmethod
    def unlock(cls, admin_password):
        if admin_password == "admin123":
            cls.locked = False
        else:
            print("Unauthorized access. Only the admin can unlock the bike.")






#__________________________________IGNORE_________________________________________________________________________________________________
# Example usage:
BikeRepair.press_repair_button()
print(BikeRepair.needs_repair)  # Output: True
print(BikeRepair.locked)        # Output: True

BikeRepair.unlock("admin123")
print(BikeRepair.locked)        # Output: False

BikeRepair.unlock("wrong_password")  # Output: Unauthorized access. Only the admin can unlock the bike.

