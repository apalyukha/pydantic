from pydantic import BaseModel, ValidationError


class Tag(BaseModel):
    id: int
    tag: str


class City(BaseModel):
    city_id: int
    name: str
    tags: list[Tag]
    # population: int


input_json = """
{
    "city_id" : "79052",
    "name" : "Lviv",
    "tags" : [{
        "id" : 1, "tag" : "capital"
    },{
        "id" : 2, "tag" : "big city"
    }]
} """

try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print("Exception", e.json())
else:
    tag = city.tags[1]
    print(tag.json())
