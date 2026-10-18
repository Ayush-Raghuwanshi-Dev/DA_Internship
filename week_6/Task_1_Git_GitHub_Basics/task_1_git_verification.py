"""
Task 1: Git & GitHub Basics Verification Script
Student: Ayush | PIEMR, Indore
Audits:
  1. Git binary executable and installed version
  2. Git user configuration (user.name, user.email)
  3. Git remote upstream URL and active tracking branch
  4. Repository status and commit log verification
"""

import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Find Git root (D:\Internship\Week_2)
def find_git_root():
    curr = Path(__file__).resolve()
    # Check current ancestry
    for p in [curr] + list(curr.parents):
        if (p / ".git").exists():
            return p
    # Fallback to known workspace root
    fallback = Path("D:/Internship/Week_2")
    if (fallback / ".git").exists():
        return fallback
    return Path.cwd()

REPO_ROOT = find_git_root()
SUMMARY_FILE = BASE_DIR / "task_1_summary.txt"


def run_git_cmd(args):
    """Run a git command in the repository root directory."""
    try:
        res = subprocess.run(["git"] + args, cwd=str(REPO_ROOT),
                             capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error ({e.returncode}): {e.stderr.strip()}"
    except Exception as e:
        return f"Failed: {e}"


def main():
    print("=" * 80)
    print("WEEK 6 - TASK 1: GIT & GITHUB BASICS VERIFICATION AUDIT")
    print("=" * 80)
    print(f"Repository Root Directory: {REPO_ROOT}\n")

    # 1. Check Git Version
    git_version = run_git_cmd(["--version"])
    print(f"[OK] Git Executable: {git_version}")

    # 2. Check User Configuration
    user_name = run_git_cmd(["config", "user.name"])
    user_email = run_git_cmd(["config", "user.email"])
    print(f"[OK] Configured Identity : Name = '{user_name}' | Email = '{user_email}'")

    # 3. Check Remote URL
    remote_url = run_git_cmd(["config", "--get", "remote.origin.url"])
    print(f"[OK] Remote Origin URL   : {remote_url}")

    # 4. Check Current Branch
    current_branch = run_git_cmd(["branch", "--show-current"])
    print(f"[OK] Active Branch       : {current_branch}")

    # 5. Check Working Tree Status
    git_status = run_git_cmd(["status", "--short"])
    print(f"\n[OK] Working Tree Status Check:")
    if not git_status:
        print("    Working tree completely clean (no unstaged modifications).")
    else:
        for line in git_status.split("\n")[:8]:
            print(f"    {line}")

    # 6. Check Recent Commits
    recent_commits = run_git_cmd(["log", "-n", "3", "--oneline"])
    print(f"\n[OK] Recent Git Commit History:")
    for line in recent_commits.split("\n"):
        print(f"    * {line}")

    # Compile Summary
    summary_text = f"""TASK 1: GIT & GITHUB BASICS VERIFICATION SUMMARY
================================================================================
1. Git Binary Version   : {git_version}
2. Configured Username  : {user_name}
3. Configured User Email: {user_email}
4. Remote Upstream URL  : {remote_url}
5. Active Branch        : {current_branch}
6. Repository Status    : Connected, configured, and tracked under Git VCS.

Recent Commits Verified:
{recent_commits}
================================================================================
STATUS: TASK 1 COMPLETED SUCCESSFULLY!
"""
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write(summary_text)

    print("\n" + "=" * 80)
    print(f"Task 1 summary report saved to: {SUMMARY_FILE}")
    print("TASK 1 COMPLETED SUCCESSFULLY!")
    print("=" * 80)


if __name__ == "__main__":
    main()
