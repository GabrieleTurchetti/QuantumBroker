from .circuits.languages import *
from .circuits import Circuit

from typing import Any

from threading import Lock

lock = Lock()

class Translator:
    
    def __init__(self) -> None:
        """Initialize a translator."""
        self._languages : dict[str, Language] = {}
        self._circuit_types : dict[type, list[Language]] = {}
        
        for g in globals():
            try:
                g = globals()[g]
                if issubclass(g, Language) and g is not Language: # type: ignore
                    self.register_language(g)
            except TypeError:
                pass
                
    def register_language(self, language: Any) -> None:
        """Register a language."""
        self._languages[language.__name__.lower()] = language
        circuit_type = language.circuit_type()
        if circuit_type not in self._circuit_types:
            self._circuit_types[circuit_type] = []
        self._circuit_types[circuit_type].append(language)
        
    def which(self, circuit: Circuit) -> Language:
        """Return a list of languages that can be used to represent the circuit."""
        with lock:
            if not isinstance(circuit, Circuit):
                circuit = Circuit(circuit)
            try:
                l_ls = self._circuit_types[circuit.circuit_type()]
                if len(l_ls) == 0:
                    return None
                elif len(l_ls) == 1:
                    return l_ls[0]
                else:
                    for l in l_ls:
                        if l.can_translate(circuit):
                            return l
            except KeyError:
                return None
            return None
    
    def translate(self, circuit: Circuit, language: Language | str | Circuit) -> Circuit:
        """Translate a circuit to another language."""
        if not isinstance(circuit, Circuit):
            circuit = Circuit(circuit)
        source_language = self.which(circuit)
        
        if source_language is None:
            raise ValueError(f"Could not determine source language of circuit {circuit}")
        
        try:
            intermediate = source_language.translate(circuit)
        except Exception as e:
            raise ValueError(f"Could not translate {circuit} from {source_language} to intermediate language: {e}")
            
        if isinstance(language, str):
            language = language.lower()
            if language not in self._languages:
                language += "language"
                if language not in self._languages:
                    raise ValueError(f"Unknown language: {language}")
            language = self._languages[language]
            
        elif isinstance(language, Circuit):
            language = self.which(language)
            if language is None:
                raise ValueError(f"Could not determine language of circuit {circuit}")
            
        elif isinstance(language, type) and not issubclass(language, Language):
            try:
                languages = self._circuit_types[language]
            except KeyError:
                raise ValueError(f"Unknown circuit type: {language}")
            if len(languages) == 0:
                raise ValueError("Could not determine language of circuit")
            elif len(languages) > 1:
                for l in languages:
                    if l.can_translate(intermediate):
                        language = l
                        break
                if not isinstance(language, Language):
                    raise ValueError(f"Could not determine language of circuit {circuit}")
            else:
                language = languages[0]
        else:
            if not issubclass(language, Language):
                raise ValueError(f"Unknown language: {language}")
        
        try:
            return language.translate(intermediate)
        except Exception as e:
            raise ValueError(f"Could not translate {intermediate} from intermediate language to {language}: {e}")
            