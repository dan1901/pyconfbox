#!/usr/bin/env python3
"""Build all packages in the monorepo."""

import subprocess
import sys
from pathlib import Path

# Get the root directory
root_dir = Path(__file__).parent.parent
packages_dir = root_dir / "packages"

# List of all packages
packages = [
    "pyconfbox",
    "pyconfbox-django", 
    "pyconfbox-mysql",
    "pyconfbox-postgresql",
    "pyconfbox-mongodb"
]

def run_command(cmd: list[str], cwd: Path) -> bool:
    """Run a command and return success status."""
    try:
        result = subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)
        print(f"✓ {' '.join(cmd)} (in {cwd.name})")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {' '.join(cmd)} (in {cwd.name})")
        print(f"Error: {e.stderr}")
        return False

def build_package(package_name: str) -> bool:
    """Build a single package."""
    package_dir = packages_dir / package_name
    if not package_dir.exists():
        print(f"✗ Package directory {package_dir} does not exist")
        return False
    
    print(f"\n📦 Building {package_name}...")
    
    # Clean previous builds
    dist_dir = package_dir / "dist"
    if dist_dir.exists():
        run_command(["rm", "-rf", "dist"], package_dir)
    
    # Build the package using uv run
    return run_command(["uv", "run", "--project", str(root_dir), "python", "-m", "build"], package_dir)

def main():
    """Build all packages."""
    print("🚀 Building all PyConfBox packages...\n")
    
    failed_packages = []
    
    for package in packages:
        if not build_package(package):
            failed_packages.append(package)
    
    print(f"\n{'='*50}")
    if failed_packages:
        print(f"❌ Failed to build: {', '.join(failed_packages)}")
        sys.exit(1)
    else:
        print("✅ All packages built successfully!")

if __name__ == "__main__":
    main() 