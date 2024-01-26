from contextlib import suppress
from dataclasses import dataclass
from enum import StrEnum
from pprint import pprint
from typing import Any, Literal, Annotated
from timeit import timeit

import pytest
import sqlalchemy as sa
import yaml
from pydantic import TypeAdapter, ValidationError, BaseModel, ConfigDict, \
    Field, Json, Strict
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, mapper
from typing_extensions import TypedDict

from utils.annotations import Str


@pytest.mark.parametrize(
    "value",
    (
        "",
        10,
    )
)
def test_type_adapter_errors(value: Any) -> None:
    type_adapter = TypeAdapter(Str)

    with pytest.raises(ValidationError):
        type_adapter.validator.validate_python(value)


def test_type_adapter_success() -> None:
    type_adapter = TypeAdapter(Str)
    type_adapter.validator.validate_python("hello")


class Model(BaseModel):
    """Use literal not enum. It's in 3 times faster"""

    greeting: Literal["hi", "hello"]


def test_literal_errors() -> None:
    with pytest.raises(ValidationError):
        Model(greeting="h")


def test_timeit() -> None:
    # timeit

    ta = TypeAdapter(Literal['a', 'b'])
    _result1 = timeit(lambda: ta.validate_python('a'), number=10000)

    class AB(StrEnum):
        a: str = 'a'
        b: str = 'b'

    ta = TypeAdapter(AB)
    _result2 = timeit(lambda: ta.validate_python('a'), number=10000)
    # _result2 / _result1 -> 3+ times


class Hi(TypedDict):
    a: int
    b: int


class User(BaseModel):
    id: int
    hi: Hi
    name: str = 'hi'


def test_user():
    user = User(id='123', hi=Hi(a=1, b=1))
    assert user.id == 123
    assert isinstance(user.id, int)
    assert user.model_fields_set == {'id', 'hi'}
    assert user.model_dump() == {
        'id': 123,
        'name': 'hi',
        'hi': {'a': 1, 'b': 1},
    }
    assert isinstance(user.hi["a"], int)

    assert User.model_construct(id='123', hi=Hi(a=1, b=1))

    assert id(user.model_copy(deep=True)) != id(user)

    assert user.model_dump_json() == (
        '{"id":123,"hi":{"a":1,"b":1},"name":"hi"}'
    )

    assert user.model_json_schema()  # json model representation

    assert isinstance(
        user.model_validate({'id': '123', 'hi': {'a': 1, 'b': 1}}), User
    )
    assert isinstance(User(**{'id': '123', 'hi': {'a': 1, 'b': 1}}), User)

    assert user.model_validate_json(
        '{"id":123,"hi":{"a":1,"b":1},"name":"hi"}'
    )
    with pytest.raises(ValidationError):
        user.model_validate_json('{"id":123,"hi":{"a":1,"b":"I"},"name":"hi"}')


class Base(DeclarativeBase):
    pass


class Company(Base):
    __tablename__ = 'company'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class CompanyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


def first_mapper(model: type[BaseModel], orm_entity: DeclarativeBase):
    return model.model_validate(orm_entity)


def test_first_mapper() -> None:
    company = Company(id=1, name='Vlad')
    company_model = first_mapper(CompanyModel, company)
    assert company_model.model_dump() == {'id': 1, 'name': 'Vlad'}


class MyModel(Base):
    __tablename__ = 'my_model'

    id: Mapped[int] = mapped_column(primary_key=True)
    _metadata: Mapped[dict | list] = mapped_column('metadata', sa.JSON)


class MyDomainModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    metadata: Annotated[dict | list, Field(alias='_metadata')]


def test_domain_model() -> None:
    model = MyModel(id=1, _metadata={'name': 'Vlad'})
    domain_model = MyDomainModel.model_validate(model)

    assert domain_model.model_dump() == {'id': 1, 'metadata': {'name': 'Vlad'}}
    assert (
        domain_model.model_dump(by_alias=True)
        == {'id': 1, '_metadata': {'name': 'Vlad'}}
    )


yaml_data = """
services:
    my_service:
        build: .
        image: my_service:1
        container_name: my_service
"""


class Service(TypedDict):
    """
    Useful when you want to validate ad save object as dict.
    You can validate slower in 3 times, but more sugar syntax using BaseModel
    """

    build: str
    image: str
    container_name: str


class Data(BaseModel):
    services: dict[str, Service]


def test_yaml_validation() -> None:
    data: dict = yaml.safe_load(yaml_data)
    data_model = Data.model_validate(data)
    assert data_model == Data(
        services={
            'my_service': {
                'build': '.',
                'image': 'my_service:1',
                'container_name': 'my_service'
            }
        }
    )


class YourModel(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    value: int
    age: int


def test_model_construct() -> None:
    model = YourModel.model_construct(value='example123', age='Lersk')
    assert model.value == 'example123'
    assert model.age == 'Lersk'


def test_your_model() -> None:
    model = YourModel(value=1, age=24)
    with pytest.raises(ValidationError):
        model.value = 'hi'


StrRange10 = Annotated[
    str,
    Field(min_length=1),
    Field(max_length=10),
]
str_range_ta = TypeAdapter(StrRange10)


@pytest.mark.parametrize(
    "value",
    (
        '',
        'lerka' * 3,
    )
)
def test_multiple_annotations_errors(value: str) -> None:
    with pytest.raises(ValidationError):
        str_range_ta.validator.validate_python(value)


def test_multiple_annotations_success() -> None:
    str_range_ta.validator.validate_python("lerka")


class NewModel(BaseModel):
    json_field: Json[list[str]]
    is_done: Annotated[bool, Strict()]


def test_strict_bool_errors() -> None:
    with pytest.raises(ValidationError):
        NewModel(json_field='["open", "door"]', is_done='er')
