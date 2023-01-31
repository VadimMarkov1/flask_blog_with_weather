from typing import List, Dict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.weather.models import Country
from weather.country_codes import read_codes_data_from_json, FILENAME
from config import config
from app import db


def get_path_to_db():
    """Get path to database"""
    return config['default'].SQLALCHEMY_DATABASE_URI


def convert_data_from_json_to_db(countries: List[Dict[str, str]], path_to_db: str):
    """Convert data from json file to db"""
    for country in countries:
        country_instance = Country(
            code=country['code'],
            name=country['name'],
            flag=f'https://www.countryflagicons.com/FLAT/32/{country["code"]}.png'
        )
        engine = create_engine(path_to_db, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(country_instance)
        session.commit()


def main(filename: str):
    """Main controller"""
    path_to_db = get_path_to_db()
    countries = read_codes_data_from_json(filename)
    convert_data_from_json_to_db(countries, path_to_db)


main(FILENAME)
