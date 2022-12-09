import asyncio

from argparse import ArgumentParser


def main() -> None:
    parser = ArgumentParser(
        prog = "aioweatherlink",
        description = "Retrieve and parse data from Davis WeatherLink devices.",
        epilog = "github.com/leadzero/aioweatherlink"
    )

if __name__ == "main":
    main()