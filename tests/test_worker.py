import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.worker import handle
class HandlerTests(unittest.TestCase):
    def test_known_handlers(self):self.assertEqual(handle('sum',[1,2]),3);self.assertEqual(handle('upper','hi'),'HI')
    def test_no_eval(self):
        with self.assertRaises(ValueError):handle('__import__("os")',[])
        with self.assertRaises(ValueError):handle('sum',[float('nan')])
