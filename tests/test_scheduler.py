import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.scheduler import Scheduler
class SchedulerTests(unittest.TestCase):
    def test_reuse_and_cleanup(self):
        with Scheduler() as s:
            self.assertEqual(s.invoke('a','sum',[1,2])['result'],3);s.invoke('a','sum',[2,3]);self.assertEqual(s.reuses,1)
        self.assertEqual(s.workers,{})
    def test_deadline_retires_process(self):
        with Scheduler(timeout=.01) as s:
            self.assertEqual(s.invoke('a','sleep-demo',.1)['status'],'timeout');self.assertEqual(s.workers,{})
