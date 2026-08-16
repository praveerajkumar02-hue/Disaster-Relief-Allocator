# Disaster Relief Resource Allocator
## Architecture, Design and User Guide

---

## 1. Project Overview

The Disaster Relief Resource Allocator is a Streamlit-based application designed to help relief organizations allocate limited resources such as food, water, and shelter to verified disaster relief requests.

The system prioritizes vulnerable groups and ensures that available resources are allocated efficiently.

The application provides:

- Request validation
- Duplicate request detection
- Vulnerability-based prioritization
- Full resource allocation
- Partial resource allocation
- Pending requests when resources are unavailable
- Zero and negative quantity validation
- Relief operations dashboard
- Automated testing

---

## 2. Problem Statement

During disaster situations, relief organizations may receive many requests for essential resources while having limited supplies.

Manual allocation can lead to:

- Incorrect resource distribution
- Delays in responding to vulnerable groups
- Duplicate requests
- Allocation beyond available inventory
- Difficulty tracking pending requests

This application provides a simple automated system for managing and allocating available relief resources.

---

## 3. Objectives

The main objectives are:

1. Verify incoming relief requests.
2. Prevent duplicate requests.
3. Prioritize vulnerable groups.
4. Allocate resources based on availability.
5. Support full and partial allocation.
6. Mark requests as pending when resources are unavailable.
7. Reject zero and negative quantity requests.
8. Provide a clear dashboard for relief operations.
9. Provide automated tests for core allocation logic.

---

# 4. System Architecture

The application follows a modular architecture.

```text
                   +----------------------+
                   |       User           |
                   |  Relief Request Form |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   |     Streamlit UI     |
                   |       app.py         |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   | Request Validation   |
                   |   validation.py      |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   | Duplicate Detection  |
                   | & Request Processing  |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   | Resource Allocation  |
                   |    allocator.py      |
                   +----------+-----------+
                              |
                +-------------+-------------+
                |             |             |
                v             v             v
          Allocated     Partially       Pending
                         Allocated
                              |
                              v
                   +----------------------+
                   | Operations Dashboard |
                   +----------------------+