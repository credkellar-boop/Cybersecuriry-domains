# Firewall Rule Review Checklist

Perform this review bi-annually or quarterly to ensure network perimeters remain secure.

## Preparation
*   [ ] Export the current firewall rule set.
*   [ ] Obtain the most recent network topology diagram.
*   [ ] Gather documentation for approved business justifications for all open ports.

## Rule Analysis
*   [ ] **Cleanup:** Identify and remove disabled, unused, or expired rules.
*   [ ] **Shadowing:** Identify rules that are overridden or masked by previous, broader rules.
*   [ ] **Least Privilege:** Ensure "ANY" is not used in Source, Destination, or Service fields unless explicitly required and documented (e.g., public web server).
*   [ ] **Inbound Traffic:** Verify all inbound rules terminate in a DMZ, not the internal network.
*   [ ] **Management Ports:** Ensure management ports (SSH, RDP, HTTPS) are restricted to specific IP addresses or management VLANs.

## Finalization
*   [ ] Document all changes made during the review.
*   [ ] Backup the new configuration.
*   [ ] Schedule the next review.
*   [ ] 
