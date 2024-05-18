import click
from datetime import datetime, timedelta


class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = timedelta()
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = datetime.now() - self.elapsed_time
            self.running = True
            click.echo("Stopwatch started")

    def stop(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            self.running = False
            click.echo(f"Stopwatch stopped at {self.elapsed_time}")

    def reset(self):
        self.start_time = None
        self.elapsed_time = timedelta()
        self.running = False
        click.echo("Stopwatch reset")

    def display(self):
        if self.running:
            elapsed = datetime.now() - self.start_time
        else:
            elapsed = self.elapsed_time
        click.echo(f"Elapsed time: {elapsed}")


stopwatch = Stopwatch()


@click.group()
def cli():
    """Stopwatch CLI"""
    pass


@cli.command()
def start():
    """Start the stopwatch"""
    stopwatch.start()


@cli.command()
def stop():
    """Stop the stopwatch"""
    stopwatch.stop()


@cli.command()
def reset():
    """Reset the stopwatch"""
    stopwatch.reset()


@cli.command()
def display():
    """Display the current elapsed time"""
    stopwatch.display()


if __name__ == "__main__":
    cli()
