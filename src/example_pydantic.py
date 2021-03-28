from pydantic import BaseModel


class City(BaseModel):
    city_id: int
    name: str
    population: int


input_json = """
{
    "city_id" : 123,
     "name" : "Lviv",
      "population" : 1000000
}
"""

# city = City.parse_raw(
#     """{"city_id" : 123, "name" : "Lviv", "population" : 1000000}"""
# )

city = City.parse_raw(input_json)
print(city)
