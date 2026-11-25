"""Tests for the Temperature class. Run with: pytest -v"""

import pytest

from temperature import Temperature

TOL = 1e-9

# The same physical temperature in (Celsius, Fahrenheit, Kelvin)
REFERENCE_POINTS = [
    pytest.param(-273.15, -459.67, 0.0, id="absolute_zero"),
    pytest.param(-40.0, -40.0, 233.15, id="c_f_crossover"),
    pytest.param(0.0, 32.0, 273.15, id="water_freezes"),
    pytest.param(37.0, 98.6, 310.15, id="body_temperature"),
    pytest.param(100.0, 212.0, 373.15, id="water_boils"),
]


# --- 1. Initialization ---------------------------------------------------------


def test_default_unit_is_celsius() -> None:
    assert Temperature(20).unit == "C"


@pytest.mark.parametrize("unit", ["c", "C", "f", "F", "k", "K"])
def test_unit_is_case_insensitive(unit: str) -> None:
    assert Temperature(300, unit).unit == unit.upper()


def test_value_is_read_only() -> None:
    t = Temperature(20, "C")
    with pytest.raises(AttributeError):
        t.value = 30  # type: ignore[misc]


def test_unit_is_read_only() -> None:
    t = Temperature(20, "C")
    with pytest.raises(AttributeError):
        t.unit = "F"  # type: ignore[misc]


# --- 2. Validation -------------------------------------------------------------


@pytest.mark.parametrize("unit", ["X", "", "Celsius", "CF"])
def test_invalid_unit_raises(unit: str) -> None:
    with pytest.raises(ValueError):
        Temperature(0, unit)


@pytest.mark.parametrize("value, unit", [(-273.16, "C"), (-459.68, "F"), (-0.01, "K")])
def test_below_absolute_zero_raises(value: float, unit: str) -> None:
    with pytest.raises(ValueError):
        Temperature(value, unit)


@pytest.mark.parametrize("value, unit", [(-273.15, "C"), (-459.67, "F"), (0.0, "K")])
def test_exactly_absolute_zero_is_allowed(value: float, unit: str) -> None:
    Temperature(value, unit)  # Must not raise, even with floating-point rounding


def test_convert_to_invalid_unit_raises() -> None:
    with pytest.raises(ValueError):
        Temperature(0, "C").convert_to("X")


# --- 3. Conversions ------------------------------------------------------------


# Two parametrize decorators: every reference point is tested from every source unit (5 x 3 = 15 tests)
@pytest.mark.parametrize("celsius, fahrenheit, kelvin", REFERENCE_POINTS)
@pytest.mark.parametrize("source_unit", ["C", "F", "K"])
def test_conversions(source_unit: str, celsius: float, fahrenheit: float, kelvin: float) -> None:
    value = {"C": celsius, "F": fahrenheit, "K": kelvin}[source_unit]
    t = Temperature(value, source_unit)
    assert t.to_celsius() == pytest.approx(celsius, abs=TOL)
    assert t.to_fahrenheit() == pytest.approx(fahrenheit, abs=TOL)
    assert t.to_kelvin() == pytest.approx(kelvin, abs=TOL)


@pytest.mark.parametrize("celsius, fahrenheit, kelvin", REFERENCE_POINTS)
def test_convert_to_returns_new_temperature(celsius: float, fahrenheit: float, kelvin: float) -> None:
    original = Temperature(celsius, "C")
    in_f = original.convert_to("f")
    assert isinstance(in_f, Temperature)
    assert in_f.unit == "F"
    assert in_f.value == pytest.approx(fahrenheit, abs=TOL)
    assert original.unit == "C"  # The original is unchanged


# --- 4. Round-trip conversions -------------------------------------------------


@pytest.mark.parametrize("celsius", [-273.15, -40.0, 0.0, 37.0, 100.0])
def test_round_trip_c_f_k_c(celsius: float) -> None:
    original = Temperature(celsius, "C")
    result = original.convert_to("F").convert_to("K").convert_to("C")
    assert result.unit == "C"
    assert result == original


# --- 5. Cross-unit comparisons -------------------------------------------------


@pytest.mark.parametrize("celsius, fahrenheit, kelvin", REFERENCE_POINTS)
def test_equal_across_units(celsius: float, fahrenheit: float, kelvin: float) -> None:
    c = Temperature(celsius, "C")
    f = Temperature(fahrenheit, "F")
    k = Temperature(kelvin, "K")
    assert c == f
    assert f == k
    assert c == k


def test_not_equal_across_units() -> None:
    assert Temperature(0, "C") != Temperature(0, "F")


def test_ordering_across_units() -> None:
    cold = Temperature(0, "F")  # about -17.78 °C
    warm = Temperature(0, "C")  # 32 °F
    assert cold < warm
    assert cold <= warm
    assert warm > cold
    assert warm >= cold


def test_le_and_ge_when_equal() -> None:
    a = Temperature(0, "C")
    b = Temperature(32, "F")
    assert a <= b
    assert a >= b
    assert not a < b
    assert not a > b


def test_comparison_with_other_type_returns_not_implemented() -> None:
    t = Temperature(0, "C")
    assert t.__eq__(0) is NotImplemented
    assert t.__lt__(0) is NotImplemented
    assert t != 0
    with pytest.raises(TypeError):
        _ = t < 0


# --- 6. Formatting -------------------------------------------------------------


def test_repr() -> None:
    assert repr(Temperature(25, "C")) == "Temperature(25.0, 'C')"
    assert repr(Temperature(32, "f")) == "Temperature(32.0, 'F')"


@pytest.mark.parametrize(
    "value, unit, expected",
    [(25, "C", "25.00 °C"), (98.6, "f", "98.60 °F"), (273.15, "K", "273.15 K"), (-40.456, "C", "-40.46 °C")],
)
def test_str(value: float, unit: str, expected: str) -> None:
    assert str(Temperature(value, unit)) == expected
