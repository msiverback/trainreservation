import json
from typing import Dict, List, Any, Union

from BookingReferenceServiceIf import BookingReferenceServiceIf


class TicketOffice(object):
    def __init__(self, booking_service):
        assert isinstance(booking_service, object)
        self.booking_service = booking_service

    def make_reservation(self, train_id, param):
        booking = {"train_id": train_id, "booking_reference": self.booking_service.get_booking_reference(),
                   "seats": []}
        return booking
