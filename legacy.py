import argparse
import asyncio


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
