# 🚀 Evaluating and Analyzing the Defense Mechanisms against Jailbreaking Attempts on LLMs

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-Academic%20Use%20Only-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📚 About the Project

This research and study project was conducted as part of **CPSC 8570: Network Technologies Security** at **Clemson University** during **Spring 2025**.

> **Course Context:**  
> This course introduced foundational cybersecurity concepts, research seminars, hands-on security labs, and required a semester-long research project with a final conference-style paper and presentation.

---

## 📁 Table of Contents

- [About the Project](#-about-the-project)
- [Objective](#-objective)
- [Main Contributions](#-main-contributions)
- [Dataset](#-dataset)
- [How to Run](#-how-to-run)
- [Evaluation](#-evaluation)
- [Authors](#-authors)
- [Acknowledgements](#-acknowledgements)

---

## 🌟 Objective

- Analyze and exploit the defense mechanisms of commercial LLMs (e.g., GPT-3.5, GPT-4, GPT-4o, o3-mini).
- Conduct black-box evaluation to test LLM vulnerabilities using jailbreak prompts.
- Categorize failure modes (Timeout, Exception, AI Denial) to infer internal filtering strategies.

---

## 🛠 Main Contributions

- 📚 Replicated and extended the **MASTERKEY** jailbreak framework.
- 🔎 Developed a **custom multi-category jailbreak dataset** based on public sources.
- 🛡 Built a **modular evaluation pipeline**:
  - `run_jailbreak.py`: Automates prompt execution and logs output.
  - `evaluate_results.py`: Computes Query Success Rate (QSR) and category-level success.
  - `analyze_failures.py`: Categorizes failures (timeout, exceptions, AI content refusals).
- ⚡ Enabled **live tracking** of latency, token usage, and failure causes.
- 💬 Designed **black-box evaluation** with no internal model access.

---

## 📊 Dataset

- 13 Policy Violation Categories:
  - Illegal Activity, Hate Speech, Malware, Economic Harm, Fraud, Privacy Violation, and more.
- Augmented using:
  - [jailbreak_llms GitHub repository](https://github.com/verazuo/jailbreak_llms)
  - Additional custom augmentations for completeness.

---

## 🏃 How to Run

### 1. Clone the Repository
```bash
git clone <repository-link>
cd <repository-folder>
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Set OpenAI API Key
- **Linux/macOS:**
  ```bash
  export OPENAI_API_KEY='your-api-key'
  ```
- **Windows (CMD):**
  ```bash
  set OPENAI_API_KEY=your-api-key
  ```
- **Windows (PowerShell):**
  ```powershell
  $env:OPENAI_API_KEY="your-api-key"
  ```

### 4. Run Jailbreak Prompts
```bash
python run_jailbreak.py --model gpt-3.5-turbo --max_per_category 10
```
- Models Supported: `gpt-3.5-turbo`, `gpt-4`, `gpt-4o`, `o3-mini`
- Results saved under `/results/`
- Errors logged under `/logs/`

### 5. Evaluate Success Rate
```bash
python evaluate_results.py --input results/<result-file.csv>
```

### 6. Analyze Failure Reasons
```bash
python analyze_failures.py --input results/<result-file.csv>
```

---

## 📊 Evaluation

- **Query Success Rate (QSR):** Percentage of successful jailbreaks.
- **Failure Type Analysis:** Breakdown into Timeout, Exception, and AI Response Refusals.
- **Token Cost Monitoring:** Track token usage to manage API budget efficiently.

---

## 👨‍💻 Authors

- **Aditya More**
- **Atharva Jadhav**
- **Prasad Jadhav**
- **Shubham Narale**

**Clemson University | Spring 2025**

---

## 🏅 Acknowledgements

- Masterkey Paper:  
  _V. Zuo et al., MASTERKEY: Automated Jailbreaking of Large Language Model Chatbots, 2024._
- Dataset Reference:  
  _V. Zuo, [jailbreak_llms GitHub repository](https://github.com/verazuo/jailbreak_llms)._

---

> **Disclaimer:** This project was conducted strictly for academic research purposes. No malicious activity was performed using the findings.
