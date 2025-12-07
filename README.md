
# Banking Strands Demo Project

## Overview
This project demonstrates an AWS Strands agent for banking use cases. It can:
- Answer banking FAQs
- Calculate EMI
- Provide financial tips

## Setup
1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Deploy using AWS CDK:
   ```bash
   cdk bootstrap
   cdk deploy
   ```
