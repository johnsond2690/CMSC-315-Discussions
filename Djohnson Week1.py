
"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

This assignment demonstrates inheritance, namespaces,
shallow copying, and deep copying in Python.
"""

from copy import copy, deepcopy


# TODO 1: Create a parent class.
class ParentClass:
    # Class variable shared by instances unless overridden.
    manufacturer = "SecureTech"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        return (
            f"Device: {self.name}, "
            f"Location: {self.location}, "
            f"Manufacturer: {self.manufacturer}"
        )

    def __repr__(self):
        return (
            f"ParentClass(name={self.name!r}, "
            f"location={self.location!r})"
        )


# TODO 2: Create a child class that inherits from the parent.
class ChildClass(ParentClass):
    # New class variable.
    device_category = "Security Camera"

    def __init__(self, name, location, model, resolution):
        # Initialize the inherited instance variables.
        super().__init__(name, location)

        # New instance variables.
        self.model = model
        self.settings = {
            "resolution": resolution,
            "zones": ["Front Door", "Driveway"]
        }
        self.events = []

    # Override the parent's display_info() method.
    def display_info(self):
        return (
            f"Device: {self.name}, "
            f"Location: {self.location}, "
            f"Manufacturer: {self.manufacturer}, "
            f"Category: {self.device_category}, "
            f"Model: {self.model}, "
            f"Settings: {self.settings}"
        )

    # New child-class method.
    def record_event(self, event):
        self.events.append(event)
        return f"Event recorded: {event}"

    # Student-created extension.
    def clear_events(self):
        self.events.clear()
        return "All events cleared."

    def __repr__(self):
        return (
            f"ChildClass(name={self.name!r}, "
            f"location={self.location!r}, "
            f"model={self.model!r}, "
            f"settings={self.settings!r}, "
            f"events={self.events!r})"
        )


# TODO 3: Demonstrate class and instance namespaces.
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    camera1 = ChildClass(
        "Front Camera", "Front Door", "SC100", "1080p"
    )

    camera2 = ChildClass(
        "Back Camera", "Back Door", "SC200", "4K"
    )

    # Access the class variable through the class.
    print("Class access:", ChildClass.device_category)

    # Access the same class variable through an object.
    print("Object access:", camera1.device_category)

    # Add an attribute to only one object.
    camera1.status = "Online"

    # Display each object's instance namespace.
    print("\nCamera 1 namespace:", camera1.__dict__)
    print("Camera 2 namespace:", camera2.__dict__)

    # Display the class namespace.
    print("\nClass namespace:")
    print({
        key: value
        for key, value in ChildClass.__dict__.items()
        if not key.startswith("__")
    })

    print("\nCamera 1 status:", camera1.status)
    print(
        "Does camera 2 have its own status?",
        "status" in camera2.__dict__
    )


# TODO 4: Demonstrate shallow and deep copying.
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Copy Test Camera", "Garage", "SC300", "1080p"
    )

    # A shallow copy creates a new outer object, but nested
    # mutable objects are shared with the original.
    shallow_copy = copy(original)

    # A deep copy creates independent copies of nested data.
    deep_copy = deepcopy(original)

    # Modify nested data in the original object.
    original.settings["zones"].append("Backyard")
    original.settings["resolution"] = "4K"

    # Display all three objects.
    print("\nOriginal:", original)
    print("\nShallow copy:", shallow_copy)
    print("\nDeep copy:", deep_copy)

    print("\nOriginal zones:", original.settings["zones"])
    print("Shallow copy zones:", shallow_copy.settings["zones"])
    print("Deep copy zones:", deep_copy.settings["zones"])


# TODO 5: Complete the main function.
def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object.
    device = ParentClass("Main Alarm", "Living Room")

    print("\nParent object:")
    print(device.display_info())

    # Create and test a child object.
    camera = ChildClass(
        "Front Camera", "Front Door", "SC100", "1080p"
    )

    print("\nChild object:")
    print(camera.display_info())

    # Demonstrate inheritance and the child's new method.
    print("\nInheritance demonstration:")
    print(camera.record_event("Motion detected"))
    print("Recorded events:", camera.events)

    # Demonstrate the student-created extension.
    print(camera.clear_events())
    print("Events after clearing:", camera.events)

    # Run namespace and copying demonstrations.
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
