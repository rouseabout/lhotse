import click

from lhotse.bin.modes import download, prepare
from lhotse.recipes.atco2 import download_atco2, prepare_atco2
from lhotse.utils import Pathlike

__all__ = ["atco2"]


@download.command(context_settings=dict(show_default=True))
@click.argument("target_dir", type=click.Path())
def atco2(target_dir: Pathlike):
    """ATCO2 download."""
    download_atco2(target_dir)


@prepare.command(context_settings=dict(show_default=True))
@click.argument("corpus_dir", type=click.Path(exists=True, dir_okay=True))
@click.argument("output_dir", type=click.Path())
@click.option("--foreign-sym", type=str, default="<unk>")
@click.option("--partial-sym", type=str, default="<unk>")
@click.option("--hesitation-sym", type=str, default="<unk>")
@click.option("--unknown-sym", type=str, default="<unk>")
def atco2(
    corpus_dir: Pathlike,
    output_dir: Pathlike,
    foreign_sym: str,
    partial_sym: str,
    hesitation_sym: str,
    unknown_sym: str,
):
    """ATCO2 data preparation."""
    prepare_atco2(
        corpus_dir,
        output_dir=output_dir,
        foreign_sym=foreign_sym,
        partial_sym=partial_sym,
        hesitation_sym=hesitation_sym,
        unknown_sym=unknown_sym,
    )
