import os
import sys
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import click

from qukit.components.circuits import Circuit
from qukit.components.virtual_provider import VirtualProvider
from qukit.components.translator import Translator
from qukit.components.dispatcher import Dispatch, Dispatcher
from qukit.components.compilation_manager import CompilationManager

from typing import Any

tokens: dict[str, str | bool] = {
    "IonQ": False, 
    "Braket": False,
    "IBMQ": "",
    "Local": True
}

vp = VirtualProvider(tokens)
translator = Translator()
dispatcher = Dispatcher(vp, translator)
cm = CompilationManager()

@click.group("vp")
def virtual_provider() -> None:
    """Virtual Provider commands."""
    pass

@virtual_provider.command("ls")
@click.option("--backends", "-b", is_flag=True, help="List available backends.")
def provider_ls(backends: bool) -> None:
    """List available providers."""
    if backends:
        for provider in vp.available_providers():
            click.echo(f"- {provider}")
            for backend in provider.available_backends():
                click.echo(f"    - {backend}")
    else:
        for provider in vp.available_providers():
            click.echo(f"- {provider}")
        
@virtual_provider.group("backend")
def provider_backend() -> None:
    """Provider backend commands."""
    pass

@provider_backend.command("ls")
@click.argument("provider", type=str)
def provider_backend_ls(provider: str) -> None:
    """List available backends."""
    for backend in vp.get_provider(provider).available_backends():
        click.echo(backend)
        
@provider_backend.command("info")
@click.argument("provider", type=str)
@click.argument("backend", type=str)
def provider_backend_info(provider: str, backend: str) -> None:
    """Show backend info."""
    click.echo(vp.get_backend(provider, backend).info())
    
@provider_backend.command("run")
@click.argument("provider", type=str)
@click.argument("backend", type=str)
@click.argument("circuit", type=click.File('r'))
@click.option("--shots", "-s", type=int, help="Number of shots.", default=100)
def provider_backend_run(provider: str, backend: str, circuit: click.File, shots: int) -> None:
    """Show backend info."""
    click.echo((vp.get_backend(provider, backend).run(circuit.read(), shots, False)).counts()) # type: ignore
    
@click.command("translate")
@click.argument("circuit", type=click.File('r'))
@click.option("--language", "-l", type=str, help="Language to translate to.", default="qiskit")
@click.option("--output", "-o", type=click.File('w'), help="Output file.", default=sys.stdout.buffer)
def translate(circuit: click.File, language: str, output: click.File) -> None:
    """Translate a circuit."""
    c = translator.translate(circuit.read(), language) # type: ignore
    if output == sys.stdout.buffer:
        output.write(str(c.get()).encode()) # type: ignore
    else:
        output.write(str(c.get())) # type: ignore

@click.command("dispatch")
@click.option("--file", "-f", type=click.File('r'), help="File to dispatch.", multiple=True)
@click.option("--task", "-t", type=click.Tuple([str, str, click.File('r'), int]), help="Task to dispatch.", multiple=True)
@click.option("--output", "-o", type=click.File('w'), help="Output file.", default=sys.stdout.buffer)
def dispatch(file: tuple[click.File, ...], task: tuple[tuple[str, str, click.File, int], ...], output=click.File) -> None:
    """Dispatch tasks."""
    d = Dispatch()
    circuits = {}
    for f in file:
        f = json.load(f) # type: ignore
        for provider in f: # type: ignore
            for backend in f[provider]: # type: ignore
                for circuit_file,shots in f[provider][backend]: # type: ignore
                    circuit = (os.open(circuit_file, "r")).read() # type: ignore
                    d.add_task(backend=vp.get_backend(provider, backend), circuit=Circuit(str(circuit)), shots=shots)
                    circuits[circuit] = circuit_file
    for t in task:
        circuit_file = t[2]
        circuit = circuit_file.read()
        d.add_task(backend=vp.get_backend(t[0], t[1]), circuit=circuit, shots=t[3])
        circuits[circuit] = circuit_file.name
        
    res = dispatcher.run(d, False)
    
    counts : dict[str, dict[str, dict[str, list[dict[str, Any]]]]] = {}
    for result in res:
        provider = result.backend().provider().name()
        backend = result.backend().name()
        circuit = result.circuit().get()
        circuit = circuits[circuit]
        shots = result.shots()
        data = result.counts()
        if provider not in counts:
            counts[provider] = {}
        if backend not in counts[provider]:
            counts[provider][backend] = {}
        if circuit not in counts[provider][backend]:
            counts[provider][backend][circuit] = []
        counts[provider][backend][circuit].append({"shots": shots, "counts": data})
        
    counts = json.dumps(counts, indent=4) # type: ignore
        
    if output == sys.stdout.buffer:
        output.write(counts.encode()) # type: ignore
    else:
        output.write(counts) # type: ignore
            

@click.command("compile")
@click.argument("circuit", type=click.File('r'))
@click.option("--backend", "-b", type=str, help="Backend to compile for (provider.backend).", default=None)
@click.option("--optimisation-level", "-l", type=int, help="Optimisation level.", default=0)
@click.option("--output", "-o", type=click.File('w'), help="Output file.", default=sys.stdout.buffer)
def compile(circuit: click.File, backend: str, optimisation_level: int, output: click.File) -> None:
    """Compile a circuit."""
    provider, backend = backend.split(".")
    backend = vp.get_backend(provider, backend) # type: ignore 
    c = cm.compile(circuit.read(), backend, optimisation_level) # type: ignore
    if output == sys.stdout.buffer: 
        output.write(str(c.get()).encode()) # type: ignore
    else:
        output.write(str(c.get()))  # type: ignore
            


@click.group()
def main() -> None:
    """Qukit CLI.\n
Quantum ToolKit - A Python library for Quantum Computing."""

if __name__ == "__main__":
    main.add_command(virtual_provider)
    main.add_command(translate)
    main.add_command(dispatch)
    main.add_command(compile)
    main() 
    