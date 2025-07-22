import pandas as pd
import ipaddress as ipd
import matplotlib.pyplot as plt

# Step 1: Load IP data from Excel file.
subnet_analysis_df = pd.read_excel('ip_data.xlsx')

# Initialize empty lists to store calculated subnet information.
CIDR_Notaion = []
Network_Address = []
Broadcast_Address = []
Num_Usable_Hosts = []
Network_Address_Merge_CIDR = []
Num_Address = []

# Step 2: Iterate over each row to compute subnet details
for index , row in subnet_analysis_df.iterrows():
    try:
      ip = row ['IP Address']
      mask = row ['Subnet Mask']
    
      # Create an IPv4 network object.
      Network_CIDR = ipd.IPv4Network(f"{ip}/{mask}" , strict = False)

      # Append calculated values to respective lists.
      CIDR_Notaion.append(str(Network_CIDR.prefixlen))
      Network_Address.append(str(Network_CIDR.network_address))
      Network_Address_Merge_CIDR.append(str(Network_CIDR))
      Num_Address.append(Network_CIDR.num_addresses)
      Broadcast_Address.append(str(Network_CIDR.broadcast_address))
    

      if Network_CIDR.prefixlen < 31:
        Num_Usable_Hosts.append(Network_CIDR.num_addresses - 2)
      else:
        Num_Usable_Hosts.append(Network_CIDR.num_addresses)

    except Exception as e:
        print(f" error in row : {index}: {e}")
        CIDR_Notaion.append ("Error")
        Network_Address.append ("Error")
        Broadcast_Address.append ("Error")
        Num_Usable_Hosts. append ("Error")
        Network_Address_Merge_CIDR.append ("None")
        
# Step 3: Add calculated subnet columns back to the original DataFrame.
subnet_analysis_df['CIDR'] = CIDR_Notaion  
subnet_analysis_df['Network_address'] = Network_Address
subnet_analysis_df['Network_Address_Merge_CIDR'] = Network_Address_Merge_CIDR
subnet_analysis_df['Num_Address'] = Num_Address
subnet_analysis_df['Broadcast_address'] = Broadcast_Address
subnet_analysis_df['Usable_hosts'] = Num_Usable_Hosts


print("=== IP/Subnet Analysis Snapshot (First 10 Rows) ===\n")
print(subnet_analysis_df.to_string(index=False))

# Step 4: Export dataset with subnet info to CSV
subnet_analysis_df.to_csv('ip_subnet_analyzer.csv', index = False)


# Step 5: Group data by CIDR notation to get counts of hosts per subnet.
Grouped_By_CIDR = subnet_analysis_df.groupby('CIDR')
Go_Num_Host = Grouped_By_CIDR.size().reset_index( name = 'Number of Host')

print("=== Summary of Number of Hosts per Subnet (CIDR) ===\n")
print(Go_Num_Host.to_string(index=False))


# Step 6: Export summary report showing count of IPs per CIDR subnet.
Go_Num_Host.to_csv('Subnet_Group_Summary.csv', index = False)


# Step 7: Visualize the number of hosts per subnet using a bar chart.
plt.figure(figsize = (4 , 5))  
plt.bar(Go_Num_Host['CIDR'], Go_Num_Host['Number of Host'], color = 'mediumseagreen', edgecolor = 'gold')

plt.xlabel('CIDR Notation', fontsize = 12, fontweight = 'bold')
plt.ylabel('Number of Hosts', fontsize = 12, fontweight = 'bold')
plt.title ('Number of Hosts per Subnet (CIDR)', fontsize = 14, fontweight = 'bold')

plt.xticks(rotation = 20, fontsize = 12) 
plt.yticks(fontsize = 12)

plt.grid(axis = 'y', linestyle = '--', alpha = 0.9)  

plt.tight_layout()
plt.savefig('subnet_chart.png', dpi=300)

print("\nSubnet analysis completed successfully.")
print("=" * 50)

print("Detailed results have been saved to 'ip_subnet_analysis.csv' and 'Subnet_Group_Summary.csv'.")
print("=" * 50)

print("A bar chart visualization has been saved as 'subnet_chart.png'.")