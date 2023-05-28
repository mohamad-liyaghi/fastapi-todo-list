from core.security.password import PasswordHandler


def test_password_hashing():
    password = 'password'
    hashed_password = PasswordHandler.hash(password)
    assert isinstance(hashed_password, str)
    assert hashed_password != ""
    assert hashed_password != password


def test_password_verification():
    password = "password"
    hashed_password = PasswordHandler.hash(password)
    assert PasswordHandler.verify(hashed_password, password) is True

    incorrect_password = "wrong_password"
    assert PasswordHandler.verify(hashed_password, incorrect_password) is False
