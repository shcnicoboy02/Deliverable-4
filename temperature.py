"""Temperature class that supports Celsius ("C"), Fahrenheit ("F") and Kelvin ("K")."""

from __future__ import annotations  # Lets "-> Temperature" be used inside the class on Python < 3.14

VALID_UNITS = ("C", "F", "K")
TOLERANCE = 1e-9  # Floating-point tolerance used in validation and comparisons


class Temperature:
    """A temperature with a value and a unit. The attributes are read-only."""

    def __init__(self, value: float, unit: str = "C") -> None:
        self._unit = self._normalise_unit(unit)
        self._value = float(value)

        # Allow tiny rounding errors: -459.67 °F can become about -1e-14 K after conversion.
        if self.to_kelvin() < -TOLERANCE:
            raise ValueError(f"{value} {self._unit} is below absolute zero (0 K)")

    @staticmethod
    def _normalise_unit(unit: str) -> str:
        """Return the unit in upper case, or raise ValueError if it is not C, F or K."""
        if not isinstance(unit, str) or unit.upper() not in VALID_UNITS:
            raise ValueError(f"Invalid unit {unit!r}, must be one of {VALID_UNITS}")
        return unit.upper()

    # --- Read-only attributes (property without a setter) ---------------------

    @property
    def value(self) -> float:
        """The temperature value, in its own unit."""
        return self._value

    @property
    def unit(self) -> str:
        """The unit: "C", "F" or "K"."""
        return self._unit

    # --- Conversions ------------------------------------------------------------

    def to_celsius(self) -> float:
        """Return the temperature in degrees Celsius."""
        if self._unit == "K":
            return self._value - 273.15
        if self._unit == "F":
            return (self._value - 32) * 5 / 9
        return self._value

    def to_fahrenheit(self) -> float:
        """Return the temperature in degrees Fahrenheit."""
        if self._unit == "C":
            return self._value * 9 / 5 + 32
        if self._unit == "K":
            return (self._value - 273.15) * 9 / 5 + 32
        return self._value

    def to_kelvin(self) -> float:
        """Return the temperature in Kelvin."""
        if self._unit == "C":
            return self._value + 273.15
        if self._unit == "F":
            return (self._value - 32) * 5 / 9 + 273.15
        return self._value

    def convert_to(self, target_unit: str) -> Temperature:
        """Return a new Temperature in target_unit (case-insensitive). Raises ValueError if the unit is invalid."""
        target = self._normalise_unit(target_unit)
        if target == "C":
            return Temperature(self.to_celsius(), "C")
        if target == "F":
            return Temperature(self.to_fahrenheit(), "F")
        return Temperature(self.to_kelvin(), "K")

    # --- String representations -------------------------------------------------

    def __repr__(self) -> str:
        """Unambiguous representation, e.g. Temperature(25.0, 'C')."""
        return f"Temperature({self._value!r}, {self._unit!r})"

    def __str__(self) -> str:
        """Human-readable representation with two decimals, e.g. 25.00 °C."""
        symbol = "K" if self._unit == "K" else f"°{self._unit}"  # Kelvin has no degree sign
        return f"{self._value:.2f} {symbol}"

    # --- Comparisons (done in Kelvin, so mixed units work) ----------------------

    def _difference(self, other: Temperature) -> float:
        """Return self minus other, measured in Kelvin."""
        return self.to_kelvin() - other.to_kelvin()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self._difference(other)) <= TOLERANCE

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self._difference(other)) > TOLERANCE

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._difference(other) < -TOLERANCE

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._difference(other) <= TOLERANCE

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._difference(other) > TOLERANCE

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._difference(other) >= -TOLERANCE
