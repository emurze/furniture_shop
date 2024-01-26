import functools
from typing import Annotated, Any, Callable, Optional
from uuid import UUID, uuid4

from pydantic import AfterValidator, validate_call, BeforeValidator, \
    PlainValidator, WrapValidator, BaseModel, field_validator, Field, \
    model_validator, field_serializer, model_serializer, WrapSerializer, \
    ConfigDict
# from pydantic_core import PydanticCustomError
from pydantic_core.core_schema import SerializerFunctionWrapHandler


def wrap_map_validator(value: Any, handler: Callable) -> Any:
    assert value > 10
    result = handler(value)
    return result


def max_validator(value: Any) -> Any:
    assert value > 10
    return value


def make_validator(func: Callable, mode: str) -> Callable:
    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        print(mode)
        return func(*args, **kwargs)

    return inner


str_validation = Annotated[
    int,
    BeforeValidator(make_validator(max_validator, 'before-1')),
    WrapValidator(make_validator(wrap_map_validator, 'wrap-1')),
    BeforeValidator(make_validator(max_validator, 'before-2')),
    WrapValidator(make_validator(wrap_map_validator, 'wrap-2')),
    AfterValidator(make_validator(max_validator, 'after-2')),
    PlainValidator(make_validator(max_validator, 'plain-2')),
    BeforeValidator(make_validator(max_validator, 'before-3')),
    AfterValidator(make_validator(max_validator, 'after-3')),
    WrapValidator(make_validator(wrap_map_validator, 'wrap-3')),
    BeforeValidator(make_validator(max_validator, 'before-4')),
    WrapValidator(make_validator(wrap_map_validator, 'wrap-4')),
]


def test_after_validator() -> None:
    @validate_call
    def func(value: str_validation) -> Any:
        return value

    # func(15)


class UserModel(BaseModel):
    model_config = ConfigDict(validate_return=True)

    id: UUID = Field(default_factory=uuid4)
    name: str

    @field_validator('name', mode='after')
    @classmethod
    def check_after_name(cls, value: str) -> str:
        return value

    @model_validator(mode='before')
    @classmethod
    def check_before_model(cls, data: Any) -> str:
        return data

    @model_validator(mode='after')
    def check_after_model(self, data: Any) -> str:
        return data


def test_field_validator() -> None:
    model = UserModel(name='John')
    model.model_dump()


class User(BaseModel):
    id: UUID = Field(frozen=True, default_factory=uuid4)
    name: str = Field(min_length=3, serialization_alias="username")
    age: int = Field(gt=16)
    city: str = Field(min_length=3, default='London')
    zip_code: Optional[str] = Field(default=None)

    @field_serializer('name')
    def serialize_name(self, name: str) -> str:
        return f'{name} + Vlad'


def test_serialization() -> None:
    user = User(name='Arthas', age=28)
    assert (
        user.model_dump(
            include={'id', 'name', 'age', 'city', 'zip_code'},
            exclude={'age'},
            by_alias=True,
            exclude_defaults=True,
            exclude_unset=True,  # fields that you don't set manually,
            exclude_none=True,
        )
    ) == {'username': 'Arthas + Vlad'}


class Model(BaseModel):
    value: str

    @model_serializer
    def serialize_model(self) -> dict:
        return {'value': f'serialized {self.value}'}


def test_model_serializer() -> None:
    model = Model(value='Hello')
    assert model.model_dump() == {'value': 'serialized Hello'}


def serialize_int(value: Any, nxt: SerializerFunctionWrapHandler) -> str:
    return f"serialized {nxt(value)}"


FancyInt = Annotated[int, WrapSerializer(serialize_int)]


class Car(BaseModel):
    quantity: FancyInt


def test_serializer() -> None:
    car = Car(quantity=40)
    assert car.model_dump() == {'quantity': f'serialized 40'}
