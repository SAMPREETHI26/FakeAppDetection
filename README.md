# Mobile App Forensic Analysis 

## Overview
This project is a **Flask-based web application** that integrates with the **MobSF (Mobile Security Framework) API** to automate the forensic analysis of mobile applications.
It streamlines the detection of malicious apps by handling **automated uploads, scans, and report generation**, with integrated pattern recognition for enhanced threat detection.

---

## Key Features
- **Automated Forensic Scans:** Upload APK/IPA files and trigger MobSF scans via API.
- **Report Generation:** Automatically retrieves and generates detailed security reports.
- **Pattern Recognition:** Detects malicious patterns and risky behaviors in apps.
- **Seamless API Integration:** Utilizes the MobSF REST API for backend analysis.
- **User-Friendly Interface:** Simple Flask web interface for easy uploads and results viewing.

---

## Tech Stack
- **Backend:** Python (Flask)
- **API:** MobSF REST API
- **Libraries:** requests, json, os
- **Frontend:** HTML, CSS, Bootstrap (for web UI)

---

## How It Works
1. **Upload:** User uploads an APK or IPA file through the Flask web interface.
2. **API Integration:** The backend interacts with MobSF’s REST API to initiate scans.
3. **Analysis & Detection:** The app analyzes the scan output for malicious patterns.
4. **Report Generation:** A detailed report is fetched and displayed/downloaded for review.
