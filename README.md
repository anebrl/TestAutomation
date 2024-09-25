# Test Automation with Pytest

## Introduction

This project provides automated test cases using Python's pytest framework and Selenium WebDriver to validate login functionality on the Sauce Labs sample login application (https://www.saucedemo.com/v1/).

## Installation

Install required dependencies:
pip install pytest selenium

Download the appropriate WebDriver for your browser from https://chromedriver.chromium.org/ or the relevant WebDriver for your chosen browser. Place the WebDriver executable in a location accessible to your project.

## Usage

Navigate to your project directory in your terminal.

Run the tests using: pytest

## Test Cases

test_login_valido: Simulates a successful login scenario with valid credentials.
test_login_invalido: Simulates an unsuccessful login scenario with invalid credentials and verifies the expected error message.

## Additional Notes

This code utilizes a fixture (driver) to create a WebDriver instance for each test case, ensuring proper browser setup and teardown.
Asserts are used to verify expected behavior after user actions.
Feel free to expand the test suite to cover additional functionalities.
