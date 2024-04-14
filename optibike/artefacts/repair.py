from bike import Bike

class RepairClass:
    @staticmethod
    def repair(bike):
        """
        Sets the bike's needs_repair status to True indicating it needs repairs.
        :param bike: Instance of Bike that needs to be repaired.
        """
        bike.needs_repair(True)

# Example Usage:
bike = Bike()
print(bike)  # Before repair
RepairClass.repair(bike)
print(bike)  # After repair
