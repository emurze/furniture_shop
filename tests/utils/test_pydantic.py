import uuid
from dataclasses import InitVar
from pprint import pprint
from typing import ClassVar, Literal

import pytest
from pydantic import BaseModel, PositiveInt, validate_call, Field, ConfigDict, \
    ValidationError
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
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
    title: str = Field(
        description='FROM ARG',
        json_schema_extra={
            'description': 'FROM JSON_SCHEMA_EXTRA',
            'name': 'Lera',
        }
    )


def test_json_schema_extra() -> None:
    post = Post(title='Hello world!')
    pprint(post.model_json_schema())
