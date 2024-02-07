import importlib.util
import os
from importlib._bootstrap import ModuleSpec  # noqa
from pathlib import Path
from typing import cast

from shared.infra.sqlalchemy_orm.common.config import WORKDIR
from shared.infra.sqlalchemy_orm.common.ports import Contract

SRC = Path(f"{WORKDIR}src")
PATH = "modules/"
FILENAME = "db_contract.py"


def import_contracts(directory: Path) -> list[Contract]:
    print(directory)
    print(directory.parent)

    assert directory.is_dir()

    _contracts = []

    for root, dirs, files in os.walk(directory):
        print(root, dirs, files)
        for file in files:
            print(file)
            if file == FILENAME:
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


contracts = import_contracts(SRC / PATH)
