"""
CLI script to seed or reset real TIET college data in the Workload Balancer database.

Usage:
  python seed.py                     # Seeds COE college data if not present
  python seed.py --reset             # Clears existing COE records and re-seeds fresh data
  python seed.py --branch COE        # Explicitly specify branch
  python seed.py --list-branches     # Lists supported academic branches
"""

import argparse
import asyncio
from pathlib import Path
import sys

_BACKEND_DIR = Path(__file__).resolve().parent
if str(_BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(_BACKEND_DIR))

from app.data.curriculum_catalog import get_available_branches
from app.services import demo_service


async def main():
    parser = argparse.ArgumentParser(description="Seed real TIET college dataset into Workload Balancer.")
    parser.add_argument("--branch", default="COE", help="Branch to seed (default: COE)")
    parser.add_argument("--reset", action="store_true", help="Clear existing college data for the branch and re-seed from scratch")
    parser.add_argument("--list-branches", action="store_true", help="List registered branches")
    args = parser.parse_args()

    if args.list_branches:
        print("Available branches:", ", ".join(get_available_branches()))
        return

    print(f"Initiating college data seed for {args.branch} (reset={args.reset})...")
    try:
        result = await demo_service.seed(reset=args.reset, branch_code=args.branch)
        print("\nSeed Completed Successfully:")
        for k, v in result.items():
            print(f"  - {k}: {v}")
    except Exception as exc:
        print(f"\n[ERROR] Seeding failed: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
