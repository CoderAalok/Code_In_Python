import sys 
from pathlib import Path

# Add Detective_X folder path to sys.path
package_dir = Path(__file__).parent / "Detective_X"
sys.path.insert(0, str(package_dir))

# Import main game engine
import Detective_X.detective_x as detective

# Drive main
if __name__ == "__main__":
    detective.PlayerGround().get_start()
