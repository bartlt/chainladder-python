from chainladder.utils.ci_smoke import ci_smoke_check


def test_ci_smoke_check() -> None:
    assert ci_smoke_check() is True
