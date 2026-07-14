import typer

app = typer.Typer()


@app.callback()
def callback():
    """
    This is a simple CLI application using Typer.
    """
    pass


@app.command()
def generate():
    typer.echo("Generating report from TRO...")
