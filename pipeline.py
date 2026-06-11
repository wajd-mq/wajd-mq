from prefect import flow, task

from extract import extract_weather
from transform import transform_weather
from load import load_to_csv


@task
def extract_task(city):
    return extract_weather(city)


@task
def transform_task(data):
    return transform_weather(data)


@task
def load_task(data):
    load_to_csv(data)


@flow(name="weather-etl-pipeline")
def weather_pipeline(city):

    raw_data = extract_task(city)

    transformed_data = transform_task(raw_data)

    load_task(transformed_data)

    return transformed_data


if __name__ == "__main__":
    weather_pipeline("Muscat")
    