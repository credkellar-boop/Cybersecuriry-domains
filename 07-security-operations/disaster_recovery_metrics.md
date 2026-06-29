# Disaster Recovery Key Metrics

When drafting a Disaster Recovery Plan (DRP), these two metrics dictate the strategy, backup frequency, and infrastructure design.

## RTO: Recovery Time Objective
*   **Definition:** The maximum tolerable amount of time a system, network, or application can be down after a failure or disaster occurs.
*   **Focus:** Downtime and operational restoration.
*   **Example:** If the RTO is 4 hours, systems must be back online within 4 hours of the outage. 

## RPO: Recovery Point Objective
*   **Definition:** The maximum targeted period in which data might be lost due to a major incident. It dictates how often backups must occur.
*   **Focus:** Data loss tolerance.
*   **Example:** If the RPO is 1 hour, backups must be taken at least every hour so that no more than 60 minutes of data is ever lost.
*   
