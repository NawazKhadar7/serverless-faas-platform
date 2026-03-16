import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
import importlib.util
class WasmTests(unittest.TestCase):
    @unittest.skipUnless(importlib.util.find_spec('wasmtime'),'optional wasmtime unavailable')
    def test_import_free_add(self):
        from syslab.wasm_runtime import add
        self.assertEqual(add((ROOT/'native/add.wat').read_text(),3,4),7)
    def test_default_untrusted_disabled(self):self.assertFalse(run_case({'id':'a','family':'warm','size':2,'seed':1})['metrics']['untrusted_code_enabled'])
