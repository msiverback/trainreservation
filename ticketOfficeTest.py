import json
import unittest
from unittest.mock import MagicMock

from BookingReferenceServiceIf import BookingReferenceServiceIf
from ticketOffice import TicketOffice


class MyTestCase(unittest.TestCase):

    def test_two_seats_not_available_shall_return_empty_booking(self):
        # this booking_reference_service is an abstract class which does not implement the
        # get_booking_reference method
        booking_reference_service = BookingReferenceServiceIf()
        # by using MagicMock from the unit test framework we can let get_booking_reference return a
        # specific value, in this case an empty string
        booking_reference_service.get_booking_reference = MagicMock(return_value="")
        # we give the ticket office its booking reference service when we create it
        ticket_office = TicketOffice(booking_reference_service)
        train_id = "express_2000"
        reservation = ticket_office.make_reservation(train_id, 2)
        # we decide that the representation of the reservation is a dict
        expected_reservation = dict(train_id="express_2000", booking_reference="", seats=[])
        self.assertDictEqual(reservation, expected_reservation)

    def test_one_seat_available_shall_return_booking(self):
        # Same thing as in the previous test but we let the booking_reference_server return a reference
        booking_reference_service = BookingReferenceServiceIf()
        booking_reference_service.get_booking_reference = MagicMock(return_value="d75bcd15")
        ticket_office = TicketOffice(booking_reference_service)
        train_id = "express_2000"
        reservation = ticket_office.make_reservation(train_id, 1)
        # this test case fails because it does not assign a seat to the booking
        # your task is to fix this
        expected_reservation = dict(train_id="express_2000", booking_reference="d75bcd15", seats=["1A"])
        self.assertDictEqual(reservation, expected_reservation)


if __name__ == '__main__':
    unittest.main()
