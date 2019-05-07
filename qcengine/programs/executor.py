import abc
from typing import Any, Dict, Optional

from pydantic import BaseModel

from ..util import which_import


class ProgramExecutor(BaseModel, abc.ABC):

    name: str
    scratch: bool
    thread_safe: bool
    thread_parallel: bool
    node_parallel: bool
    managed_memory: bool

    class Config:
        allow_mutation: False
        extra: "forbid"

    @abc.abstractmethod
    def compute(self, input_data: 'ResultInput', config: 'JobConfig') -> 'Result':
        pass

    @staticmethod
    @abc.abstractmethod
    def found(raise_error: bool=False) -> bool:
        """
        Checks if the program can be found.

        Parameters
        ----------
        raise_error : bool, optional
            If True, raises an error if the program cannot be found.

        Returns
        -------
        bool
            Returns True if the program was found, False otherwise.
        """
        pass

## Utility

    def get_version(self) -> str:
        """Finds program, extracts version, returns normalized version string.

        Returns
        -------
        str
            Return a valid, safe python version string.
        """
        pass

## Computers

    def build_input(self, input_model: 'ResultInput', config: 'JobConfig',
                    template: Optional[str]=None) -> Dict[str, Any]:
        raise ValueError("build_input is not implemented for {}.", self.__class__)

    def execute(self, inputs, extra_outfiles, extra_commands, scratch_name, timeout):
        raise ValueError("execute is not implemented for {}.", self.__class__)

    def parse_output(self, outfiles: Dict[str, str], input_model: 'ResultInput') -> 'Result':
        raise ValueError("parse_output is not implemented for {}.", self.__class__)
