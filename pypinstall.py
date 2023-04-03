import sys
import os

package = sys.argv[1]

os.system(".\\.venv\\Scripts\\pip.exe install " + package)
