from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.utils.capture import capture_output
from pathlib import Path

@magics_class
class CaptureMagic(Magics):
    @cell_magic
    def stream_code(self, line, cell):
        message = cell
        dest = Path.cwd() / "my_code.py"
        dest.write_text(message)
        with capture_output(stdout=True, stderr=False, display=False) as result:
            self.shell.run_cell(cell)