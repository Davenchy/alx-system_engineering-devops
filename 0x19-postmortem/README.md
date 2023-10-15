# 0x19-postmortem

### Postmortem: Server Failure



**Issue Summary:**

- **Duration:** The server failure occurred from 8:00 PM to 10:30 PM (UTC+0).

- **Impact:** The service that was affected was the customer login portal. Users experienced intermittent downtime and slow response times. Approximately 30% of the users were affected.

- **Root Cause:** The root cause of the server failure was a hardware failure in the main disk drive.



**Timeline:**

- **8:00 PM:** The issue was detected when the monitoring system sent an alert for high latency and increased error rates.

- **Actions taken:** The operations team initiated an investigation, focusing on the networking infrastructure and database servers. Assumptions were made that the issue could be related to network congestion or database overload.

- **Misleading investigation paths:** Due to the initial assumptions, significant time was spent investigating network switches and optimizing database queries.

- The incident was escalated to the infrastructure team and the database team for further investigation.

- **9:30 PM:** After extensive investigation, it was determined that the issue was not related to the network or database. Attention was redirected towards the server hardware.

- **10:00 PM:** The incident was escalated to the hardware team, who identified a faulty disk drive as the root cause of the server failure.

- **Resolution:** The faulty disk drive was replaced, and the server was brought back online at 10:30 PM.



**Root Cause and Resolution:**

The root cause of the server failure was a hardware failure in the main disk drive. The disk drive malfunctioned, causing intermittent downtime and slow response times. To resolve the issue, the faulty disk drive was replaced, restoring the server's functionality.



**Corrective and Preventative Measures:**

To prevent similar incidents in the future, the following measures will be implemented:

- Implement redundancy and failover mechanisms for critical server components.

- Enhance monitoring systems to proactively detect hardware failures.

- Develop clear incident escalation procedures to ensure swift and efficient resolution.

- Regularly conduct hardware health checks to identify potential issues before they escalate.

- Establish a comprehensive backup strategy to minimize data loss in the event of hardware failures.

- Document the incident and share lessons learned with the broader team to improve incident response and troubleshooting processes.



In conclusion, the server failure was caused by a hardware failure in the main disk drive. The issue was initially misdiagnosed, leading to delays in resolving the incident. To prevent similar incidents in the future, measures will be taken to improve hardware monitoring, implement redundancy, and enhance incident response procedures.
