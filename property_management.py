class PropertyManagement:
    def __init__(self, property_name):
        self.property_name = property_name
        self.available_units = {}  # Dictionary to store available units

    def list_available_units(self):
        """
        List available units in the property.
        """
        print(f"Available units at {self.property_name}:")
        if self.available_units:
            for unit, details in self.available_units.items():
                print(f"Unit {unit}: {details}")
        else:
            print("No units currently available.")

    def add_unit(self, unit_number, details):
        """
        Add a new unit to the property.

        Args:
        - unit_number (str): Unit number or identifier.
        - details (str): Description or details of the unit.
        """
        if unit_number not in self.available_units:
            self.available_units[unit_number] = details
            print(f"Unit {unit_number} added successfully.")
        else:
            print(f"Unit {unit_number} already exists.")

    def remove_unit(self, unit_number):
        """
        Remove a unit from the property.

        Args:
        - unit_number (str): Unit number or identifier.
        """
        if unit_number in self.available_units:
            del self.available_units[unit_number]
            print(f"Unit {unit_number} removed successfully.")
        else:
            print(f"Unit {unit_number} does not exist.")

    def handle_maintenance_request(self, unit_number, issue_description):
        """
        Handle a maintenance request for a specific unit.

        Args:
        - unit_number (str): Unit number or identifier.
        - issue_description (str): Description of the maintenance issue.
        """
        print(f"Maintenance request for Unit {unit_number} received:")
        print(issue_description)
        print("Maintenance team dispatched.")
        # Additional logic for dispatching maintenance team would be implemented here


# Example usage
if __name__ == "__main__":
    # Initialize PropertyManagement object for Regal Point Apartments
    regal_point_apartments = PropertyManagement("Regal Point Apartments")

    # Add available units
    regal_point_apartments.add_unit("101", "2-bedroom apartment")
    regal_point_apartments.add_unit("102", "1-bedroom apartment")

    # List available units
    regal_point_apartments.list_available_units()

    # Remove a unit
    regal_point_apartments.remove_unit("102")

    # List available units after removal
    regal_point_apartments.list_available_units()

    # Handle maintenance request
    regal_point_apartments.handle_maintenance_request("101", "Leaky faucet in the kitchen")
