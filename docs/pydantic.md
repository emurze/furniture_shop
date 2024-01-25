# Pydantic

### Config

### Methods

* .model_construct() - build without validation

```python
class YourModel(BaseModel):
    value: int


def test_model_construct() -> None:
    model = YourModel.model_construct(value='hi')
    assert model.value == 'hi'
```

* .model_validate() - you can pass any format, but firstly convert it to dict
* .model_validate_json() - fast build-in validation


* .model_dump()  params #####
* .model_dump_json()


* .model_copy()


* .model_extra() - Field set during validation  #####


* .model_parametrized_name() - name with Generic


* .model_perform_post_init()  #####


* .model_fields - dict('field_1': FieldInfo(), 'field_2': FieldInfo())
* .model_fields_set - ('id', 'title'')


* .model_json_schema - Pydantic model presentation
* .model_rebuild()  #####
  ```python
  
  ```

### Field


* helpers
  - AliasPath('names', 0)
  - AliasChoices('first_alias', 'second_alias')


* default
  - default
  - default_factory


* alias
  - alias - becomes general for validation_alias and serialization_alias
  - validation_alias - init, model_validate
  - serialization_alias - model_dump, model_dump_json


* hide
  - exclude = True - exclude from model_dump
  - repr = False - exclude from representation


* docs
  - title   
  - description
  - examples

  
* pydantic dataclass
  - init_var - or InitVar - error if it doesn't exist
  - kw_only - pydantic dataclass


* string
  - min_length
  - max_length
  - pattern


* number
  - gt
  - ge
  - lt
  - le
  - multiple_of
  - allow_inf_nan


* decimal
  - decimal_places
  - max_digits


* union polymorphism
  - discriminator
  ```python
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
    ```


* strict (table) '1' -> 1 parsing


* frozen, useful for Entity id


* validate_default

  ```python
  class YourModel(BaseModel):
      age: int = Field(default="an apple", validate_default=False)


  def test_validate_default() -> None:
      model = YourModel()
      assert model.age == 'an apple'
  ```
  
* json_schema_extra - add field like title, description, or examples

  ```python
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
  ```

### Annotations

```python
Annotated[
    int,
    Field(...),
    Field(...),
]
```

### Performance

* list | tuple rather than Sequence


* Use Literal, not Enum - 3 times performance


* Use TypedDict over nested models


* TypeAdapter to namespace or definition area
