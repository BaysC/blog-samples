from bays_training import greeting


def test_greeting_basic_operation():
    actual = greeting.greet('Fatima', 'Smith')

    assert actual == 'Hello, Fatima Smith!'

