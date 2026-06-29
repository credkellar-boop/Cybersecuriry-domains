# Media Sanitization Guidelines (NIST SP 800-88)

Properly disposing of data and hardware is critical to prevent data leaks. Use these three standard methods depending on the media type and data classification.

## 1. Clear
*   **Definition:** Overwriting data using standard read/write commands so it cannot be retrieved using standard recovery tools.
*   **Use Case:** Repurposing a hard drive for another user within the same organization.
*   **Methods:** Single or multi-pass wiping algorithms.

## 2. Purge
*   **Definition:** Protecting data against a laboratory attack using advanced recovery methods.
*   **Use Case:** Donating or selling hardware outside the organization.
*   **Methods:** Cryptographic Erase (CE), Degaussing (for magnetic media), Block Erase (for SSDs).

## 3. Destroy
*   **Definition:** Physical destruction of the media, making it entirely unusable.
*   **Use Case:** Highly restricted/classified data, or media that has failed and cannot be purged.
*   **Methods:** Shredding, pulverizing, melting, or incinerating.
*   
