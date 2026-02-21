"""
reservation.py

Defines the Reservation class used in the reservation system.
"""

from datetime import datetime


class Reservation:
    """
    Represents a reservation entity connecting a customer and a hotel.
    """

    def __init__(
        self,
        reservation_id,
        customer_id,
        hotel_id,
        check_in,
        check_out
    ):
        """
        Initialize a Reservation instance.

        :param reservation_id: Unique identifier
        :param customer_id: Customer ID
        :param hotel_id: Hotel ID
        :param check_in: Check-in date (YYYY-MM-DD)
        :param check_out: Check-out date (YYYY-MM-DD)
        """
        if not isinstance(reservation_id, str) or not reservation_id.strip():
            raise ValueError("reservation_id must be a non-empty string")

        if not isinstance(customer_id, str) or not customer_id.strip():
            raise ValueError("customer_id must be a non-empty string")

        if not isinstance(hotel_id, str) or not hotel_id.strip():
            raise ValueError("hotel_id must be a non-empty string")

        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.check_in = self._validate_date(check_in)
        self.check_out = self._validate_date(check_out)

        if self.check_out < self.check_in:
            raise ValueError("check_out cannot be before check_in")

    @staticmethod
    def _validate_date(date_str):
        """
        Validate date string format YYYY-MM-DD.

        :param date_str: str
        :return: datetime.date
        """
        if not isinstance(date_str, str):
            raise ValueError("date must be a string YYYY-MM-DD")

        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as exc:
            raise ValueError(
                "Date must be in YYYY-MM-DD format"
            ) from exc

    def to_dict(self):
        """
        Convert Reservation instance to dictionary.

        :return: dict
        """
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
            "check_in": self.check_in.isoformat(),
            "check_out": self.check_out.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create Reservation instance from dictionary.

        :param data: dict
        :return: Reservation instance
        """
        required_fields = {
            "reservation_id",
            "customer_id",
            "hotel_id",
            "check_in",
            "check_out",
        }
        if not required_fields.issubset(data.keys()):
            raise ValueError("Missing required reservation fields")

        return cls(
            data["reservation_id"],
            data["customer_id"],
            data["hotel_id"],
            data["check_in"],
            data["check_out"],
        )

    def display(self):
        """
        Return formatted string with reservation information.

        :return: str
        """
        return (
            f"Reservation ID: {self.reservation_id}\n"
            f"Customer ID: {self.customer_id}\n"
            f"Hotel ID: {self.hotel_id}\n"
            f"Check-in: {self.check_in}\n"
            f"Check-out: {self.check_out}"
        )
