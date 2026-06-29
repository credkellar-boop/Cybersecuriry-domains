# Secure Code Review Checklist

Use this checklist during pull requests (PRs) or manual code reviews to catch vulnerabilities before they reach production.

## Authentication & Session Management
*   [ ] Are passwords hashed using strong algorithms (e.g., Argon2, bcrypt) with salt?
*   [ ] Are session tokens securely generated, randomized, and invalidated upon logout?
*   [ ] Are authentication credentials transmitted only over TLS/HTTPS?

## Input Validation & Encoding
*   [ ] Is all user input validated on the server-side against a strict allowlist?
*   [ ] Is output encoding applied to prevent Cross-Site Scripting (XSS)?
*   [ ] Are parameterized queries or ORMs used exclusively to prevent SQL Injection?

## Error Handling & Logging
*   [ ] Do error messages avoid revealing sensitive system or application information?
*   [ ] Are security-relevant events (logins, failures, access control changes) logged?
*   [ ] Are logs sanitized to prevent log injection and the storage of PII/credentials?

## Configuration & Deployment
*   [ ] Are hardcoded secrets, API keys, and credentials removed from the source code?
*   [ ] Are dependencies and third-party libraries checked for known vulnerabilities?
*   [ ] 
