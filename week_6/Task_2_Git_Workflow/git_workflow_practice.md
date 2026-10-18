# Task 2: Git Workflow Practice Guide

**Student:** Ayush | B.Tech CSE (IoT) | PIEMR, Indore  
**Assignment:** Week 6: Git, GitHub & Final Data Analytics Project  
**Weightage:** 10 Marks  

---

## 1. Five Fundamental Git Workflow Commands

| Command | Syntax | Primary Purpose | Best Practice / Pro-Tip |
| :--- | :--- | :--- | :--- |
| **`git clone`** | `git clone <url>` | Downloads entire remote repository with complete commit history. | Always verify target directory before cloning. |
| **`git add`** | `git add <files>` | Stages working directory changes into staging index. | Use granular `git add <dir>` rather than blind `git add .` to avoid committing unwanted secrets or artifacts. |
| **`git commit`** | `git commit -m "msg"` | Captures staged snapshot with cryptographic SHA-1 hash and metadata. | Use semantic conventional commits (e.g. `feat:`, `fix:`, `docs:`). |
| **`git push`** | `git push origin <branch>` | Uploads local commits to remote tracking branch on GitHub. | Verify working tree is clean and builds pass before pushing. |
| **`git pull`** | `git pull origin <branch>` | Fetches and merges remote updates into local active branch. | Always pull before starting new work to prevent merge conflicts. |

---

## 2. Advanced Workflow Concepts

### Branching & Feature Isolation
```bash
# Create and switch to a feature branch
git checkout -b feature/data-cleaning-pipeline

# Check active branches
git branch -a
```

### Staging Inspection & Diffing
```bash
# View exact line changes between working directory and staging
git diff

# View staged changes against latest commit
git diff --staged
```

### Pulling with Fast-Forward vs Rebase
```bash
# Standard pull (fetch + merge)
git pull origin main

# Rebase pull (replay local commits cleanly atop remote changes)
git pull --rebase origin main
```

---

## 3. Capstone Project Commit Milestones
To fulfill the requirement of creating at least 3 meaningful commits during project development:

1. **Commit Milestone 1:**  
   `feat(week_6): initialize capstone project dataset selection, preparation, and Git workflow setup (Tasks 1-3)`
2. **Commit Milestone 2:**  
   `feat(week_6): implement comprehensive exploratory data analysis and data visualization (Tasks 4-5)`
3. **Commit Milestone 3:**  
   `feat(week_6): build interactive power bi dashboard, business insights, and strategic recommendations (Tasks 6-7)`
4. **Commit Milestone 4:**  
   `docs(week_6): complete capstone project documentation, presentation deck, output screenshots, and final pdf report (Task 8)`
