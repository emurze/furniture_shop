import os
import importlib.util
from typing import cast

from importlib._bootstrap import ModuleSpec  # noqa
from pathlib import Path

from shared.infra.sqlalchemy_orm.core.ports import Contract


def import_contracts(directory: Path, filename: str) -> list[Contract]:
    _contracts = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename:
                module_name = cast(ModuleSpec, os.path.splitext(file)[0])

                spec = cast(
                    ModuleSpec,
                    importlib.util.spec_from_file_location(
                        module_name, os.path.join(root, file)
                    ),
                )

                module = importlib.util.module_from_spec(spec)

                spec.loader.exec_module(module)

                _contracts.append(module.contract)

    return _contracts
