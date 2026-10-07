"""
HireX - Root Launcher
Delegates execution to hirex_resume_analyzer/app.py
"""
import sys
from pathlib import Path

# Add hirex_resume_analyzer directory to sys.path
module_dir = Path(__file__).resolve().parent / "hirex_resume_analyzer"
sys.path.insert(0, str(module_dir))

# Import and run app from hirex_resume_analyzer
from app import app

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 5000))
    debug_mode = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "yes")
    print("\n" + "=" * 60)
    print("  HIREX – AI RESUME ANALYZER MODULE (ROOT LAUNCHER)")
    app.run(host="0.0.0.0", port=port, debug=False)
