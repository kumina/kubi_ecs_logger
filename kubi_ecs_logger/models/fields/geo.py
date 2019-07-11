from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Geo(FieldSet):

    def __init__(self,
                 city_name: str = None,
                 continent_name: str = None,
                 country_iso_code: str = None,
                 country_name: str = None,
                 location: dict = None,
                 name: str = None,
                 region_iso_code: str = None,
                 region_name: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_name = city_name
        self.continent_name = continent_name
        self.country_iso_code = country_iso_code
        self.country_name = country_name
        self.location = location
        self.name = name
        self.region_iso_code = region_iso_code
        self.region_name = region_name


class GeoSchema(FieldSetSchema):
    city_name = fields.String()
    continent_name = fields.String()
    country_iso_code = fields.String()
    country_name = fields.String()
    location = fields.Dict()
    name = fields.String()
    region_iso_code = fields.String()
    region_name = fields.String()

