Postmortem: Web stack Outage Incident.
0x19. Postmortem - ALX SWE.

Issue Summary:

Duration:

Start time: Friday January 20th 2023/ 20:00 Hrs EAT.

End time: Saturday January 20th 2023/ 00:00 Hrs EAT.

Impact:

The outage affected the availability of our core web application services for approximately four hours. Users experienced slow response times and, in some cases, complete unavailability of the platform. Approximately [Y%] of users were affected during the incident.

Root cause:

The root cause of the outage was identified as a misconfiguration in the load balancer settings, causing an overload on the application servers and subsequent service degradation.

Timeline:

Detection Time:

The issue was detected at 01/20/2024 at 20:30 hrs when an alert from our monitoring system indicated a significant increase in response times and error rates.

Issue Detection:

Monitoring alerts flagged the abnormal behavior, prompting the on-call engineer to investigate.

Actions Taken:

The initial investigation focused on the application servers, checking for potential issues with the application code or server configurations.

Assumptions were made about a possible database bottleneck, leading to a deep dive into database performance metrics.

Despite these efforts, no conclusive evidence was found in the application or database layers.

Misleading Paths:

The misleading paths included exploring potential issues with third-party services and cloud infrastructure, diverting attention from the actual misconfiguration in the load balancer.

Escalation:

As the issue persisted, the incident was escalated to the DevOps and Networking teams to further investigate network-related configurations.

Resolution:

The root cause was identified as a misconfigured load balancer that was not evenly distributing traffic, causing certain servers to handle more requests than others. The issue was resolved by adjusting the load balancer settings and redistributing the traffic load.

Root Cause and Resolution:

Root Cause Explanation:

The misconfiguration in the load balancer settings led to uneven distribution of traffic, overloading specific application servers and degrading overall system performance.

Resolution Details:

The issue was resolved by adjusting the load balancer configuration to evenly distribute traffic among all available application servers. Additionally, monitoring thresholds were refined to trigger alerts in case of similar anomalies in the future.

Corrective and Preventative Measures:

Improvements/Fixes:

Implement regular audits of load balancer configurations to ensure proper distribution of traffic.

Enhance monitoring alerts to provide more granular details on performance metrics, aiding in quicker root cause identification.

Tasks to Address the Issue:

Schedule regular load balancer configuration reviews to prevent similar issues.

Conduct a comprehensive review of monitoring thresholds and update them for better accuracy.

Provide additional training for the operations team on effective debugging techniques to streamline future incident responses.

This incident postmortem serves as a valuable learning experience, emphasizing the importance of thorough investigation, accurate monitoring, and prompt resolution to ensure the reliability of our web stack.
