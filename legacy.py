import argparse
import asyncio
import aiohttp
import json


async def is_legacy(username: str) -> bool:
    url = 'https://api.ashcon.app/mojang/v2/user{username}'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                json_data = json.loads(text)
                if 'legacy' in json_data:
                    if json_data['legacy'] == 'true':
                        return True
    except Exception as e:
        print(e)

    return False


async def main():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Check if usernames are on legacy accounts.')
    parser.add_argument('usernames_file', type=str,
                        help='file that contains usernames.')
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
