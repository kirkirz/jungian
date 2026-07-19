import sys
from pathlib import Path

# Add src/ to Python path so jungian can be imported
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
