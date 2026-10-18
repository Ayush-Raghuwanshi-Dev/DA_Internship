# Task 1: Git & GitHub Basics Guide

**Student:** Ayush | B.Tech CSE (IoT) | PIEMR, Indore  
**Assignment:** Week 6: Git, GitHub & Final Data Analytics Project  
**Weightage:** 10 Marks  

---

## 1. What is Git & GitHub?
- **Git** is a distributed Version Control System (VCS) that tracks changes in source code and data files over time, allowing multiple collaborators to work simultaneously without conflict.
- **GitHub** is a cloud-based hosting platform for Git repositories that enables team collaboration, pull requests, automated CI/CD pipelines, and public portfolio showcase.

---

## 2. Core Git Architecture & Lifecycle
```
+------------------+       git add        +------------------+      git commit      +------------------+
|                  | -------------------> |                  | -------------------> |                  |
| Working Directory|                      |   Staging Area   |                      | Local Repository |
| (Untracked/Mods) | <------------------- |  (Index Cache)   | <------------------- |    (HEAD / .git) |
+------------------+      git restore     +------------------+      git reset       +------------------+
                                                                                             |
                                                                                    git push | git pull
                                                                                             v
                                                                                    +------------------+
                                                                                    | Remote Repository|
                                                                                    | (GitHub Cloud)   |
                                                                                    +------------------+
```

---

## 3. Essential Commands & Setup Walkthrough

### Step 1: Install & Verify Git
```bash
# Verify Git installation
git --version
# Expected: git version 2.40+ (windows)
```

### Step 2: Global Configuration
Configure identity attached to all cryptographic commits:
```bash
git config --global user.name "Ayush Raghuwanshi"
git config --global user.email "your-email@example.com"
git config --list
```

### Step 3: Initialize or Clone Repository
```bash
# Clone the remote internship repository
git clone https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git
cd DA_Internship
```

### Step 4: Tracking & Staging
```bash
# Inspect file statuses
git status

# Stage project files to index
git add week_6/
```

### Step 5: Creating Commits
```bash
# Record changes permanently with a descriptive commit message
git commit -m "feat(week_6): initialize final capstone project and git setup"
```

### Step 6: Remote Synchronization
```bash
# Push local commits to remote origin main branch
git push origin main
```

---

## 4. Verification Checkpoints
- [x] Git binary recognized in system PATH.
- [x] Remote URL configured to `https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git`.
- [x] Primary branch initialized to `main`.
- [x] Working tree clean and synchronized with remote upstream.
