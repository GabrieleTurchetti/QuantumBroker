from pytket.backends.backend import Backend as TK_Backend
from pytket.backends.status import StatusEnum

from . import Provider, Backend, BackendInfo, Result
from ..circuits import Circuit
from ..translator import Translator

from .IonQBackend.pytket.extensions.ionq.backends.ionq import IonQBackend as _IonQBackend

class IonQBackend(Backend):
    """IonQ backend."""
    
    def __init__(self, name: str, provider: 'IonQ', noise_model: str = "ideal", instance_name: str | None = None) -> None:
        """Initialize an IonQ backend."""
        super().__init__(name+"_"+noise_model, provider, instance_name)
        self._backend = _IonQBackend(device_name=name, api_key=provider._token, noise_model=noise_model)
        self._info = BackendInfo()
        self._noise_model = noise_model
    
    def run(self, circuits: Circuit | list[Circuit], shots: int | list[int] = 1, asynchronous: bool = False) -> Result | list[Result]:
        """Run the circuits on the backend."""
        
        translator = Translator()
        
        no_list = False
        if not isinstance(circuits, list):
            circuits = [circuits]
            no_list = True
            
        _circuits = []
            
        for circuit in circuits:
            if not isinstance(circuit, Circuit):
                circuit = Circuit(circuit)
            _circuits.append(circuit)
            
        circuits = _circuits
        
        cs = [translator.translate(c, "pytket").get() for c in circuits]
        cs = [self._backend.get_compiled_circuit(c, optimisation_level=0) for c in cs]
        
        for i,c in enumerate(cs):
            if not self.is_valid(c):
                raise ValueError(f"Circuit {i} {c} not valid for backend {self._name}")
            
        res = []
        if type(shots) is int:
            shots_ls: list[int] = [shots for _ in range(len(circuits))]
        elif type(shots) is list:
            shots_ls = shots
        else:
            raise ValueError("Invalid shots argument.")

        if not asynchronous:
            counts = [dict(result.get_counts()) for result in self._backend.run_circuits(cs, n_shots=shots)]
                
            for i,circ in enumerate(circuits):
                c = {}
                for k,v in counts[i].items():
                    k = tuple(str(i) for i in k) 
                    c["".join(k)] = int(v)
                r = Result(backend=self, circuit=circ, shots=shots_ls[i], data=c, completed=True)
                res.append(r)
        else:
            handlers = self._backend.process_circuits(cs, n_shots=shots)
            for i,circ in enumerate(circuits):
                r = Result(backend=self, circuit=circ, shots=shots_ls[i], data=handlers[i], completed=False)
                res.append(r)
                
        if no_list:
            return res[0]
        else:
            return res
    
    def is_valid(self, circuit: Circuit) -> bool:
        """Check if the circuit is valid for the backend."""
        
        if not isinstance(circuit, Circuit):
            circuit = Circuit(circuit)
        
        c = (Translator().translate(circuit, "pytket")).get()
        return bool(self._backend.valid_circuit(c))
    
    def is_ready(self, result: Result) -> bool:
        return self._backend.circuit_status(result._data).status == StatusEnum.COMPLETED
    
    def get_result(self, result: Result) -> Result:
        """Return the result of a circuit."""
        
        if result.backend() != self:
            raise ValueError("Result not from this backend.")
        
        if not self.is_ready(result):
            raise ValueError("Result is not ready.")
        counts = dict(self._backend.get_result(result._data).get_counts())
        c = {}
        for k,v in counts.items():
            k = tuple(str(i) for i in k) 
            c["".join(k)] = int(v)
        return Result(backend=self, circuit=result.circuit(), shots=result.shots(), data=c, completed=True)
    
    def info(self) -> BackendInfo:
        """Return information about the backend."""
        return self._info
    
    def noise_model(self) -> str:
        """Return the noise model."""
        return self._noise_model
    
    def noisy(self) -> bool:
        """Return True if the backend is noisy."""
        return self._noise_model != "ideal"
    
    def to_tk(self) -> TK_Backend:
        """Return the backend as a pytket backend."""
        return self._backend
    
    def __str__(self) -> str:
        """Return a string representation of the backend."""
        return f"{self.__class__.__name__}(name={self._name}, provider={self._provider}, noise_model={self._noise_model})"
    
    

class IonQ(Provider):
    
    def __init__(self, token: str) -> None:
        """Initialize an IonQ provider."""
        super().__init__(token)
        self._provider = _IonQBackend(device_name="simulator", api_key=token)
    
    def available_backends(self) -> list[Backend]:
        """Return a list of available backends."""
        backends = self._provider.available_devices()
        return [IonQBackend(name=device.device_name, provider=self) for device in backends if device is not None and device.device_name is not None]
    
    def get_backend(self, name: str) -> IonQBackend:
        """Return a backend."""
        return IonQBackend(name, self)
