import aiohttp
import asyncio
import json
import logging
import os

from argparse import ArgumentParser

from api import weatherlink_conditions_report


async def main() -> None:
    parser = ArgumentParser(
        description = "Retrieve and parse data from Davis WeatherLink devices.",
        epilog = "https://github.com/leadzero/aioweatherlink"
    )
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Increase level of verbosity (ex. -v for INFO, -vv for DEBUG')
    parser.add_argument('-H', '--host', default=os.environ.get('WEATHERLINK_HOSTNAME'), help='REST API host')
    #parser.add_argument('')

    args = parser.parse_args()

    if args.verbose == 1:
        logging.basicConfig(level=logging.INFO)
    elif args.verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    logging.debug(args)

    async with aiohttp.ClientSession() as session:
        url = f'http://{args.host}/v1/current_conditions'

        async with session.get(url) as response:
            js = await response.json()
            logging.debug(await response.json())
            conds = weatherlink_conditions_report.WeatherLinkConditionsReport.FromJson(js['data'])
            from pprint import pprint
            pprint(conds)

    


if __name__ == "__main__":
    asyncio.run(main())