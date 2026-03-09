# 🐍 Python Mastery Curriculum

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive, production-oriented Python curriculum designed to bridge the gap between textbook knowledge and real-world software engineering.

## 🎯 Professional Value & Evaluation

This curriculum is meticulously designed **not just to teach syntax, but to forge industry-ready engineers.**

After completing this curriculum, a developer will possess the following professional capabilities:

- **Core Engineering:** Write robust, async, and concurrent Python code with optimal memory management and defensive programming techniques.
- **Backend Architecture:** Build scalable REST APIs (FastAPI/Flask-like), manage database connections, implement custom ORMs, and design microservice architectures.
- **Data Engineering:** Construct memory-efficient ETL pipelines, develop data quality frameworks, and perform time-series anomaly detection.
- **Security & Forensics:** Implement JWT authentication, build password hashing systems, create port scanners, and analyze forensic logs.
- **Advanced Technology:** Leverage AI Agents (ReAct, Tool-use), Computer Vision (OpenCV document scanning, steganography).
- **Quality & DevOps (_New!_):** Ensure code reliability with advanced `pytest` mocking, and deploy applications using Docker and GitHub Actions CI/CD pipelines.

By engaging with these exercises, learners bypass the typical "tutorial hell" and directly confront the engineering challenges faced in modern tech companies.

---

## 📚 Curriculum Structure

The curriculum is divided into three main sections, heavily inspired by foundational texts and industry standards:

### 📖 Book 1: Learn Python The Hard Way (Applied)

Focuses on structured programming, file parsing, algorithms, and core system design.
_Highlights: Log Parsers, Rate Limiters, Dependency Resolvers, Plugin Architectures._

### 📖 Book 2: Python Notes For Professionals

Dives deep into advanced Python mechanics, networking, and framework internals.
_Highlights: Priority Schedulers, Async HTTP Crawlers, JWT from scratch, Reactive Event Systems._

### 🚀 Career Tracks (Specializations)

Targeted exercises for specific industry roles:

1. **Backend Engineering**: _Production FastAPI Boilerplates, Async Task Queues._
2. **Data Analysis**: _Data Quality Frameworks, SQL Analyzers._
3. **Cybersecurity**: _Forensic Log Analyzers, Secure File Transfers._
4. **Computer Vision**: _Document Scanners, Steganography._
5. **AI Agent**: _Tool-Use Foundations, Multi-Step Reasoning Agents._
6. **Testing & QA**: _Advanced Pytest & Mocks._
7. **DevOps Engineering**: _Dockerized Microservices, CI/CD Pipelines._

---

## 🛠️ How to Use This Guide

This repository comes with a built-in CLI tracker to monitor your progress.

**1. Setup Environment**
Ensure you have Python 3.11+ installed.

**2. List All Exercises**

```bash
python python_curriculum/tracker.py list
```

**3. Check Exercise Details**

```bash
python python_curriculum/tracker.py get A-01
```

**4. Mark an Exercise as Complete**

```bash
python python_curriculum/tracker.py done A-01
```

**5. View Your Progress Report**

```bash
python python_curriculum/tracker.py report
```

### 📝 Exercise Format

Every markdown file in this curriculum follows a rigorous template:

- `🎯 Mục tiêu thực tế`: The real-world objective.
- `💡 Hint chiến lược`: Progressive hints (from direction to near-solution) to unblock you without spoiling the answer.
- `🔗 Kết nối thực tế`: How this connects to standard libraries and industry tools.
- `📈 Extension challenge`: Advanced challenges for those who want to push further.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](#).

## 📄 License

This project is licensed under the MIT License.
