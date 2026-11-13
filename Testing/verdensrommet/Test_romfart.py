import pytest
from Romfart import beregn_avstand, beregn_drivstoff

def test_beregn_avstand():
    assert beregn_avstand(1000, 5) == 5000, "Feil avstand beregnet"

def test_beregn_drivstoff():
    assert beregn_drivstoff(1000,5) == 5000, "Feil drivstoff beregnet"

def test_avstand_med_null_timer_er_null():
    assert beregn_avstand(1000,0) == 0

def test_beregn_avstabd_med_mindre_enn_0_timer():
    with pytest.raises(ValueError):
        beregn_avstand(1000, -5)

def test_desimaltall():
    assert 0.1 + 0.2 == pytest.approx(0.3)