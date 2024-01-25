from config import settings


def test_env() -> None:
    assert settings.secret_key
