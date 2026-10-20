# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming in Python, including inheritance, namespaces, and shallow and deep copying. I used a security-device example to demonstrate these concepts.

## Implementation

### Parent Class

I created a `ParentClass` with a class variable named `manufacturer` and instance variables named `name` and `location`. I implemented methods to display device information and provide a readable object representation.

### Child Class

I created a `ChildClass` that inherited from `ParentClass`. I used `super().__init__()` to initialize inherited attributes and added a device category, model, settings, and event list. I also overrode the display method and added methods to record and clear security events.

### Namespaces

I created two camera objects and accessed a class variable through both the class and an object. I added a status attribute to only one object and used `__dict__` to examine the instance and class namespaces.

### Shallow and Deep Copying

I used `copy()` and `deepcopy()` to compare how changes to nested data affected copied objects. The shallow copy shared nested mutable data with the original, while the deep copy maintained independent nested data.

### Student-Created Extension

I added a `clear_events()` method to remove recorded security events. This extended the class functionality and demonstrated how methods can manage an object's data.

## Testing

I ran the program to verify inheritance, method overriding, namespace behavior, and copying behavior. I checked that adding an attribute to one object did not add it to the other and that modifying nested data affected the shallow copy but not the deep copy.

## Conclusion

This assignment demonstrated how inheritance promotes code reuse, namespaces distinguish class attributes from instance attributes, and copying affects mutable data. These concepts support the development of organized and maintainable Python applications.