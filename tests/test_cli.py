import json
import subprocess
import sys
import unittest


class CliTests(unittest.TestCase):
    def run_cli(self, *arguments):
        return subprocess.run([sys.executable, "-m", "csf_basics", *arguments],
                              capture_output=True, text=True, timeout=30)

    def test_formula_output(self):
        result = self.run_cli("path", "3")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "3*e[3] + e[2]*e[1]")

    def test_machine_readable_range(self):
        result = self.run_cli("verify", "--min-order", "4", "--max-order", "4")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["cases"]["three_legged_spiders"], 1)

    def test_invalid_range_exits_nonzero(self):
        result = self.run_cli("verify", "--max-order", "20", "--max-edges", "18")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("increase max_edges", result.stderr)


if __name__ == "__main__":
    unittest.main()

