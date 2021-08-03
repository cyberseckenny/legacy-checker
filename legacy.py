import argparse
import asyncio
import aiohttp
import json
from colorama import Fore, init
from os.path import exists

init()


async def is_legacy(username: str) -> bool:
    url = f'https://api.ashcon.app/mojang/v2/user/{username}'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                json_data = json.loads(text)
                if 'legacy' in json_data:
                    if json_data['legacy'] == True:
                        print(
                            f'Found legacy account {Fore.LIGHTYELLOW_EX}{username}{Fore.RESET}.')
                        return True
    except Exception as e:
        print(e)

    return False


async def main(username_file: str):
    if exists(username_file):
        usernames: list[str] = list()

        with open(username_file) as uf:
            for l in uf.readlines():
                line = l.strip()
                if not line == '':
                    usernames.append(line)

        coroutines = [is_legacy(username) for username in usernames]
        await asyncio.gather(*coroutines, return_exceptions=True)

    else:
        print(f'{Fore.LIGHTRED_EX}File {username_file} does not exist.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Check if usernames are on legacy accounts.')
    parser.add_argument('username_file', type=str,
                        help='file that contains usernames.')
    args = parser.parse_args()
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main(args.username_file))
