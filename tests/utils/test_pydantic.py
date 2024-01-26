import uuid
from dataclasses import InitVar
from enum import Enum
from pprint import pprint
from typing import ClassVar, Literal, Protocol

import pytest
from pydantic import BaseModel, PositiveInt, validate_call, Field, ConfigDict, \
    ValidationError, PydanticUserError
from pydantic.dataclasses import dataclass
from pydantic.fields import FieldInfo


class Apple(BaseModel):
    id: PositiveInt
    quality: PositiveInt


def test_apple() -> None:
    apple = Apple(id=1, quality=5)

    fields = apple.model_fields.keys()
    for field in fields:
        getattr(apple, field)



@validate_call
def add(a: PositiveInt, b: PositiveInt) -> int:
    """
    Validate call is a way to strict static typing
    """

    return a + b


def test_add_validate_call() -> None:
    assert add(1, 1)


@dataclass
class MyModel:
    b: str = Field(kw_only=True)
    a: InitVar[str]


class Foo(BaseModel):
    model: MyModel


def test_model_init_var() -> None:
    foo = Foo(model={'a': 'wew', 'b': 'wre'})
    with pytest.raises(AttributeError):
        print(foo.model.a)


@dataclass
class MyModel2:
    b: str
    a: str = Field(init_var=True)


class Foo2(BaseModel):
    model: MyModel2


def test_model_init_var_in_field() -> None:
    foo = Foo2(model={'a': 'wew', 'b': 'wre'})
    assert isinstance(foo.model.a, FieldInfo)


class Foo3(BaseModel):
    a: ClassVar[int] = 3
    b: str


def test_model_class_var() -> None:
    foo3 = Foo3(b="3")
    Foo3.a = 4
    assert foo3.a is Foo3.a


class Cat(BaseModel):
    type: Literal['cat', 'kitty']
    age: PositiveInt


class Dog(BaseModel):
    type: Literal['dog', 'puppy']
    age: PositiveInt


class Model(BaseModel):
    """
    Discriminator allows you to know which model to use.
    Is a type of polymorphism
    """

    pet: Cat | Dog = Field(discriminator='type')


def test_model_discriminator() -> None:
    model = Model(pet={'type': 'dog', 'age': 1})

    assert model.pet.type == 'dog'
    assert model.pet.age == 1


class User(BaseModel):
    age: int = Field(strict=True)


def test_strict_mode_errors() -> None:
    with pytest.raises(ValidationError):
        User(age='13')


class UserNoStrict(BaseModel):
    age: int = Field(frozen=True)


def test_no_strict_mode() -> None:
    user = UserNoStrict(age='13')
    assert user.age == 13


def test_frozen_field() -> None:
    user = UserNoStrict(age='13')
    with pytest.raises(ValidationError):
        user.age = 3


class Pet(BaseModel):
    a: int = Field(
        title='Arg',
        description='The best Arg in the world',
        examples=[13],
    )
    b: int = Field(
        exclude=True,  # validation
        repr=False,  # representation
    )


def test_pet_exclude_field() -> None:
    pet = Pet(a=1, b=2)
    assert pet.model_dump() == {'a': 1}
    assert str(pet) == "a=1"


def test_json_schema() -> None:
    pet = Pet(a=1, b=1)
    pet.model_json_schema()


class YourModel(BaseModel):
    age: int = Field(default="an apple", validate_default=False)


def test_validate_default() -> None:
    model = YourModel()
    assert model.age == 'an apple'


class Post(BaseModel):
    model_config = ConfigDict(extra='allow')

    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
    title: str = Field(
        description='FROM ARG',
        json_schema_extra={
            'description': 'FROM JSON_SCHEMA_EXTRA',
            'name': 'Lera',
        }
    )

    def __post_init__(self, data: str) -> None:
        self.data = data



def test_model_extra_data() -> None:
    post = Post(title='Hello world!', name='Vlad')
    post.model_post_init('hello')

    assert post.model_extra == {'name': 'Vlad'}


def test_json_schema_extra() -> None:
    post = Post(title='Hello world!')
    post.model_json_schema()


class Bar(BaseModel):
    foo: 'Foo10'


def test_rebuild() -> None:
    with pytest.raises(PydanticUserError):
        Bar.model_json_schema()

    class Foo10(BaseModel):
        pass

    Bar.model_rebuild()
    Bar.model_json_schema()


class BaseConfig(BaseModel):
    model_config = ConfigDict(extra='forbid')


class NewModel(BaseConfig):
    a: int


def test_new_model_forbid() -> None:
    with pytest.raises(ValidationError):
        NewModel(a=1, b=3)


class Model1(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    kitty: str = Field(alias='cat')


def test_populate_by_name() -> None:
    m1 = Model1(kitty='dog')
    assert m1.model_dump() == {'kitty': 'dog'}


def test_populate_by_name_attr() -> None:
    m2 = Model1(cat='dog')
    assert m2.model_dump() == {'kitty': 'dog'}


class Class(BaseModel, validate_assignment=True):
    a: int = Field(serialization_alias='hi')


def test_validate_assignment_success() -> None:
    class_ = Class(a=2)
    class_.a = '3'  # because of strict = False


def test_validate_assignment_error() -> None:
    class_ = Class(a=2)
    with pytest.raises(ValidationError):
        class_.a = 'hi'


def test_model_json_schema_mode() -> None:
    assert (
        Class.model_json_schema(mode='validation')
        != Class.model_json_schema(mode='serialization')
    )


class Bora(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    a: str


def test_coerce_numbers_to_str() -> None:
    bora = Bora(a=1)
    print(bora.model_dump())


class Bora2(BaseModel):
    model_config = ConfigDict(hide_input_in_errors=True)
    a: str


def test_hidden_input_in_errors() -> None:
    try:
        Bora2(a=1)
    except ValidationError:
        """
        # Hidden input
        print(f'{exp=}')
        """


class Bora3(BaseModel):
    model_config = ConfigDict(json_schema_extra={'vlad': 'THE BEST GUY'})
    a: int = Field(json_schema_extra={'name': 'THE BEST GUY'})


def test_config_json_schema_extra() -> None:
    assert Bora3.model_json_schema(mode='validation') == {
        'properties': {
            'a': {
                'name': 'THE BEST GUY',
                'title': 'A',
                'type': 'integer',
            },
        },
        'required': ['a'],
        'title': 'Bora3',
        'type': 'object',
        'vlad': 'THE BEST GUY',
    }


class Card(Enum):
    F = 'FIRST'
    S = 'SECOND'


class Deck(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    cards: list[Card] = Field(default=Card.F)


def test_deck_schema() -> None:
    deck = Deck(cards=[Card.F])
    assert deck.model_dump() == {'cards': ['FIRST']}


class ICar(Protocol):
    mark: str


class Car:
    def __init__(self, mark: str) -> None:
        self.mark = mark

    def __eq__(self, other: ICar) -> bool:
        return self.mark == other.mark

    def __repr__(self) -> str:
        return self.mark


class Builder(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    car: Car
    age: int


def test_arbitrary_type_allowed() -> None:
    car = Car('BMW')
    builder = Builder(car=car, age=10)
    assert builder.model_dump() == {'car': Car('BMW'), 'age': 10}


@dataclass
class Human:
    name: str
    age: int


class Person(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    age: PositiveInt


def test_from_attributes() -> None:
    human = Human('vlad', 24)
    person = Person.model_validate(human)
    assert person.model_dump() == {'name': 'vlad', 'age': 24}


class SubHuman(BaseModel):
    name: str
    age: int


class SubPerson(BaseModel, revalidate_instances='always'):
    human: Human


def test_revalidate_instances_errors() -> None:
    human = SubHuman(name='Vlad', age=24)
    human.age = 'age'

    with pytest.raises(ValidationError):
        SubPerson(human=human)
