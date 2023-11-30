import pytest
from animal_class import Animal

@pytest.fixture
def cat():
    return Animal("Cat", 70, 200, 20, 2)

def test_move_to(cat):
    cat.move_to(10)
    assert cat.position == 10
    assert cat.current_fead == 50

def test_move_to_not_enough_feed():
    dog = Animal("Dog", 20, 50, 15, 1)
    dog.move_to(25)
    assert dog.position == 0
    assert dog.current_fead == 20

def test_feed(cat):
    cat.feed(50)
    assert cat.current_fead == 120

def test_feed_too_much():
    rabbit = Animal("Rabbit", 40, 80, 10, 1)
    rabbit.feed(50)
    assert rabbit.current_fead == 40

def test_str_representation(cat):
    expected_str = "Cat Feed: 70/200 Speed: 20 Loss: 2 | Position: 0"
    assert str(cat) == expected_str

if __name__ == "__main__":
    pytest.main()