import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.scheduler import Scheduler
class TenantTests(unittest.TestCase):
    def test_separate_workers_and_quotas(self):
        with Scheduler(quota=1) as s:
            self.assertEqual(s.invoke('a','sum',[1])['status'],'ok');self.assertEqual(s.invoke('a','sum',[1])['status'],'limited');self.assertEqual(s.invoke('b','sum',[1])['status'],'ok');self.assertEqual(s.starts,2)
    def test_capacity_eviction(self):
        with Scheduler(max_workers=1) as s:s.invoke('a','sum',[1]);s.invoke('b','sum',[1]);self.assertEqual(list(s.workers),['b'])
