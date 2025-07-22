# Subnet Analysis Report

This report presents the results of analyzing a dataset of IP addresses and subnet masks as part of the Barq Systems DevOps Internship Task. The goal was to extract insights from the data, identify patterns in subnet usage, and provide optimization suggestions. Below are the answers to the required analysis questions based on the dataset.

---

## 1. Which subnet has the most hosts?

The subnets with the highest number of usable hosts are those using the **/22 CIDR**, which allow for **1022 usable hosts** each.

From the dataset, there are **8 occurrences** of subnets with a /22 prefix:

- `192.168.100.0/22`
- `10.2.0.0/22`
- `172.16.48.0/22`
- `10.20.4.0/22`
- `192.168.20.0/22`
- `10.3.0.0/22`
- `172.16.60.0/22`
- `10.15.4.0/22`

These subnets provide the highest address capacity among all entries.

---

## 2. Are there any overlapping subnets? If yes, which ones?

Yes, several subnets in the dataset **overlap** in terms of IP ranges. These overlapping subnets could potentially lead to routing conflicts or inefficient IP planning if not handled properly.

### Notable overlaps identified:
- `172.16.0.0/23` overlaps with `172.16.1.0/24`
- `192.168.6.0/23` overlaps with `192.168.7.0/24`

Further detailed overlap checks were performed using the `ipaddress` module's `overlaps()` method for accurate detection.

---

## 3. What is the smallest and largest subnet in terms of address space?

### Largest Subnets:
- Subnets with **CIDR /22**
- Provide **1024 total addresses** and **1022 usable hosts**
- Found 8 times in the dataset

### Smallest Subnets:
- Subnets with **CIDR /24**
- Provide **256 total addresses** and **254 usable hosts**
- Found 10 times in the dataset

Although /24 is a standard subnet size, it is the smallest subnet present in this dataset in terms of address space.

---

## 4. Suggest a subnetting strategy that could reduce wasted IPs in this network.

The current dataset shows frequent use of /22 and /23 subnets, which offer large address spaces. However, many of these subnets may be over-allocated if the actual number of used hosts is low.

### Suggested Strategy:

1. **Use Variable Length Subnet Masking (VLSM):**  
   Assign subnet sizes based on actual host requirements. For example:
   - Use /24 for departments with < 250 hosts
   - Use /25 or /26 for small teams or isolated devices

2. **Avoid assigning /22 unless absolutely necessary:**  
   It wastes ~800+ addresses if only 100–200 hosts are active.

3. **Group related IPs into contiguous ranges** to make summarization and routing more efficient.

4. **Apply subnet audits regularly** to detect underutilized IP blocks and reallocate as needed.

This strategy would help reduce address space waste, improve routing efficiency, and make the IP structure more maintainable.

---
