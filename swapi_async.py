import asyncio
import aiohttp
import datetime
from models import Base, Session, SwapiPeople, engine
import requests

async def get_people(people_id):
    session = aiohttp.ClientSession()
    responce = await session.get(f"https://swapi.dev/api/people/{people_id}")
    json_data = await responce.json()
    json_data['person_id'] = str(people_id)
    await session.close()
    return json_data

def get_title(url_list):
    title_list = []
    for i in url_list:
        title_list.append(requests.get(i).json()['title'])
    return  title_list

def get_name(url_list):
    title_list = []
    for i in url_list:
        title_list.append(requests.get(i).json()['name'])
    return  title_list

def list_to_string(title_list):
    delim = ", "
    res = ''
    for i in title_list:
            res = res + str(i) + delim
    return res

async def insert_to_db(people_json_list):
    async with Session() as session:
        print(people_json_list)
        for i in people_json_list:
            if len(i) < 5:
                print()
            else:
                swapi_people_list = SwapiPeople(person_id=i['person_id'],
                                                name=i['name'],
                                                height = i['height'],
                                                mass = i['mass'],
                                                hair_color = i['hair_color'],
                                                skin_color = i['skin_color'],
                                                eye_color = i['eye_color'],
                                                birth_year = i['birth_year'],
                                                gender = i['gender'],
                                                homeworld = i['homeworld'],
                                                films = list_to_string(get_title(i['films'])),
                                                species = list_to_string(get_name(i['species'])),
                                                vehicles = list_to_string(get_name(i['vehicles'])),
                                                starships = list_to_string(get_name(i['starships']))
                )
                session.add(swapi_people_list)
                await session.commit()


async def main():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)
    coros = []
    for i in range(1, 90):
        coro = get_people(i)
        coros.append(coro)
    responces = await asyncio.gather(*coros)
    await insert_to_db(responces)

    await engine.dispose()

start = datetime.datetime.now()
asyncio.run(main())
print(datetime.datetime.now() - start)


