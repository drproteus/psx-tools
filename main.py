import re
import json
import click
from tools.title_id import get_psx_id
from tools.api import get_title_id


@click.group("psx-tools")
def cli():
    pass


@cli.command("lookup-disc")
@click.argument("filename", type=click.STRING)
def lookup_disc(filename):
    title_id = get_psx_id(filename)
    if not title_id:
        click.echo("[Error] Unable to detect title!", err=True)
        exit(2)
    try:
        data = get_title_id(title_id)
    except Exception as e:
        click.echo(e, err=True)
        exit(1)
    click.echo(json.dumps(data, indent=2))


@cli.command("detect-title")
@click.argument("filename", type=click.STRING)
@click.option(
    "--format",
    "-f",
    "_format",
    type=click.Choice(choices=(1, 2, 3)),
    help="""
1 -> SLUS_942.21,
2 -> SLUS94221,
3 -> SLUS-94221
""",
)
def detect_title(filename, _format):
    title_id = get_psx_id(filename)
    if not title_id:
        click.echo("[Error] Unable to detect title!", err=True)
        exit(2)
    if _format == "alpha":
        title_id = re.sub(r"[\.\-\_ ]*", "", title_id)
    if _format == "standard":
        title_id = re.sub(r"[\. ]*", "", title_id).replace("_", "-")
    click.echo(title_id)


if __name__ == "__main__":
    cli()
