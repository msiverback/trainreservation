from abc import ABC, abstractmethod


###############################################
# This is an abstract class for retrieving
# booking references
class BookingReferenceServiceIf(ABC):
    def get_booking_reference(self):
        pass
